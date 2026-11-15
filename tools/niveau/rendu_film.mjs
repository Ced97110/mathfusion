// Copyright: Your Name. Apache 2.0
// Offline render of the film « Vent de travers » (public/anim/vent-de-travers) to an MP4.
// Each frame: window.film.rendre(t, { largeur, hauteur, echantillons }) in headless Chrome (accumulated
// sub-frames: anti-aliasing and motion blur), a PNG screenshot piped straight into ffmpeg's stdin
// (no frame is written to disk), then the two real recordings are mixed with the gain envelopes of
// son.js (ffmpeg volume expressions) and muxed.
//
// Usage:
//   PW=<dir>/node_modules/playwright-core/index.mjs node tools/niveau/rendu_film.mjs \
//     --largeur 1920 --hauteur 1080 --ips 30 --echantillons 16 --debut 0 --fin 58 --sortie film.mp4 [--vertical]
//   --vertical : 9:16 layout (?format=vertical), 1080x1920 unless --largeur/--hauteur are given.
//   CHROME=<path to Chrome> overrides the browser.

import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { dirname, extname, join, normalize, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const ICI = dirname(fileURLToPath(import.meta.url));
const RACINE = resolve(ICI, '../../public/anim/vent-de-travers');
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

// ------------------------------------------------------------------ arguments
function lireArguments(argv) {
  const a = { ips: 30, echantillons: 16, debut: 0, fin: null, sortie: 'vent-de-travers.mp4', vertical: false };
  for (let i = 0; i < argv.length; i += 1) {
    const cle = argv[i].replace(/^--/, '');
    if (cle === 'vertical') { a.vertical = true; continue; }
    const v = argv[i + 1];
    if (v === undefined) throw new Error(`valeur manquante pour --${cle}`);
    i += 1;
    if (cle === 'sortie') a.sortie = v;
    else if (['largeur', 'hauteur', 'ips', 'echantillons', 'debut', 'fin'].includes(cle)) {
      const n = Number(v);
      if (!Number.isFinite(n) || n < 0) throw new Error(`--${cle} : nombre attendu, reçu « ${v} »`);
      a[cle] = n;
    } else throw new Error(`option inconnue : --${cle}`);
  }
  a.largeur = Math.round(a.largeur || (a.vertical ? 1080 : 1920));
  a.hauteur = Math.round(a.hauteur || (a.vertical ? 1920 : 1080));
  if (a.largeur % 2 || a.hauteur % 2) throw new Error('largeur et hauteur doivent être paires (yuv420p)');
  a.echantillons = Math.max(1, Math.round(a.echantillons));
  return a;
}

// ------------------------------------------------------------------ static server (ES modules need http)
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8',
  '.json': 'application/json', '.mp3': 'audio/mpeg', '.svg': 'image/svg+xml', '.png': 'image/png', '.md': 'text/plain; charset=utf-8',
};
function servir(racine) {
  const serveur = createServer(async (req, res) => {
    try {
      const chemin = decodeURIComponent(new URL(req.url, 'http://x').pathname);
      const fichier = normalize(join(racine, chemin.endsWith('/') ? `${chemin}index.html` : chemin));
      if (!fichier.startsWith(racine + sep) && fichier !== racine) { res.writeHead(403).end(); return; }
      await stat(fichier);
      res.writeHead(200, { 'content-type': TYPES[extname(fichier)] || 'application/octet-stream', 'cache-control': 'no-store' });
      res.end(await readFile(fichier));
    } catch {
      res.writeHead(404).end();
    }
  });
  return new Promise((ok) => serveur.listen(0, '127.0.0.1', () => ok(serveur)));
}

// ------------------------------------------------------------------ audio graph from son.js
async function chargerSon() {
  // the page folder has no package.json "type": load son.js (no imports) as a data URL module
  const src = await readFile(join(RACINE, 'son.js'), 'utf8');
  return import(`data:text/javascript;base64,${Buffer.from(src).toString('base64')}`);
}

/** filter_complex producing [a]: both recordings placed, enveloped by son.js, cut to [debut, fin). */
function grapheAudio(son, debut, fin) {
  const parties = [];
  const etiquettes = [];
  const placer = (entree, piste, nom) => {
    piste.segments.forEach((s, i) => {
      const ms = Math.round(s.film * 1000);
      const e = `${nom}${i}`;
      parties.push(`[${entree}:a]atrim=start=${s.source}:duration=${s.duree},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,adelay=${ms}|${ms}[${e}]`);
      etiquettes.push(e);
    });
    const liste = etiquettes.filter((x) => x.startsWith(nom));
    const brut = `${nom}brut`;
    if (liste.length === 1) parties.push(`[${liste[0]}]anull[${brut}]`);
    else parties.push(`${liste.map((x) => `[${x}]`).join('')}amix=inputs=${liste.length}:normalize=0:duration=longest[${brut}]`);
    parties.push(`[${brut}]volume='${son.expressionFfmpeg(son.CLES[nom])}':eval=frame[${nom}]`);
  };
  placer(1, son.PISTES.vent, 'vent');
  placer(2, son.PISTES.moteur, 'moteur');
  parties.push(`[vent][moteur]amix=inputs=2:normalize=0:duration=longest,apad,atrim=start=${debut}:end=${fin},asetpts=PTS-STARTPTS[a]`);
  return parties.join(';');
}

// ------------------------------------------------------------------ main
const a = lireArguments(process.argv.slice(2));
if (!process.env.PW) throw new Error('PW doit pointer vers playwright-core/index.mjs');
const { chromium } = await import(process.env.PW);
const son = await chargerSon();
const DUREE = 58;
const fin = Math.min(DUREE, a.fin ?? DUREE);
const debut = Math.min(a.debut, fin);
const premiere = Math.round(debut * a.ips);
const derniere = Math.ceil(fin * a.ips); // exclusive
const total = derniere - premiere;
if (total <= 0) throw new Error('intervalle vide');

const serveur = await servir(RACINE);
const port = serveur.address().port;
const url = `http://127.0.0.1:${port}/index.html?rendu=1${a.vertical ? '&format=vertical' : ''}`;
// the last frame (the final rule on its plate) is held 3 s when the render reaches the end of the film
const TENUE = fin >= DUREE ? 3 : 0;
const grapheVideo = TENUE > 0 ? `[0:v]tpad=stop_mode=clone:stop_duration=${TENUE}[v]` : '[0:v]null[v]';

const ffmpeg = spawn('ffmpeg', [
  '-hide_banner', '-loglevel', 'error', '-y',
  '-f', 'image2pipe', '-framerate', String(a.ips), '-c:v', 'png', '-i', '-',
  '-i', join(RACINE, son.PISTES.vent.fichier),
  '-i', join(RACINE, son.PISTES.moteur.fichier),
  '-filter_complex', `${grapheVideo};${grapheAudio(son, debut, fin + TENUE)}`,
  '-map', '[v]', '-map', '[a]',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', String(a.ips),
  '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart',
  a.sortie,
], { stdio: ['pipe', 'inherit', 'inherit'] });
const finFfmpeg = new Promise((ok, ko) => {
  ffmpeg.on('error', ko);
  ffmpeg.on('close', (code) => (code === 0 ? ok() : ko(new Error(`ffmpeg a échoué (code ${code})`))));
});
const ecrire = (buf) => new Promise((ok, ko) => {
  if (ffmpeg.stdin.write(buf)) { ok(); return; }
  const suite = (err) => {
    ffmpeg.stdin.off('drain', suite);
    ffmpeg.stdin.off('error', suite);
    if (err) ko(err); else ok();
  };
  ffmpeg.stdin.on('drain', suite);
  ffmpeg.stdin.on('error', suite);
});

const navigateur = await chromium.launch({
  executablePath: CHROME,
  args: ['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist', '--autoplay-policy=no-user-gesture-required'],
});
let erreur = null;
try {
  const page = await navigateur.newPage({ viewport: { width: a.largeur, height: a.hauteur }, deviceScaleFactor: 1 });
  page.on('pageerror', (e) => console.error(`[page] ${e.message}`));
  page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') console.error(`[page ${m.type()}] ${m.text().slice(0, 300)}`); });
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForFunction(() => window.film && window.film.pret, null, { timeout: 120000 });
  await page.evaluate(() => window.film.pret);
  console.log(`Rendu ${a.largeur}×${a.hauteur}, ${a.ips} images/s, ${a.echantillons} sous-images, t = ${debut} à ${fin} s : ${total} images → ${a.sortie}`);

  const t0 = Date.now();
  for (let i = 0; i < total; i += 1) {
    const t = (premiere + i) / a.ips;
    const ti = Date.now();
    await page.evaluate(([tt, o]) => window.film.rendre(tt, o), [t, { largeur: a.largeur, hauteur: a.hauteur, echantillons: a.echantillons }]);
    const png = await page.screenshot({ type: 'png', clip: { x: 0, y: 0, width: a.largeur, height: a.hauteur } });
    await ecrire(png);
    const s = (Date.now() - ti) / 1000;
    const moy = (Date.now() - t0) / 1000 / (i + 1);
    const reste = Math.round(moy * (total - i - 1));
    process.stdout.write(`\rimage ${i + 1}/${total}  t = ${t.toFixed(2)} s  ${s.toFixed(2)} s/image (moyenne ${moy.toFixed(2)})  reste ${Math.floor(reste / 60)} min ${reste % 60} s   `);
  }
  process.stdout.write('\n');
  console.log(`Images : ${((Date.now() - t0) / 1000).toFixed(1)} s, ${((Date.now() - t0) / 1000 / total).toFixed(2)} s par image.`);
} catch (e) {
  erreur = e;
} finally {
  await navigateur.close();
  ffmpeg.stdin.end();
  serveur.close();
}
if (erreur) { ffmpeg.kill('SIGKILL'); throw erreur; }
await finFfmpeg;
console.log(`Écrit : ${a.sortie}`);
