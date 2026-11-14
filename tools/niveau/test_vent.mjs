// Test de bout en bout du niveau « Vent de travers » dans Chrome (playwright-core).
// Usage : PW=<dossier>/node_modules/playwright-core/index.mjs node tools/niveau/test_vent.mjs <url du site construit> [dossier captures]
// Valeurs attendues recopiées de lib/niveau_vent.js (testé par Vitest) : cap 090° → 24,46 km au sud ; cap 083,6° → 35 m, gagné.
import { mkdirSync } from 'node:fs';

const { chromium } = await import(process.env.PW);
const base = (process.argv[2] || 'http://127.0.0.1:8765').replace(/\/$/, '');
const captures = process.argv[3] || '.';
mkdirSync(captures, { recursive: true });
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

const resultats = [];
const verifier = (nom, ok, detail = '') => {
  resultats.push({ nom, ok });
  console.log(`${ok ? 'OK ' : 'ÉCHEC'} ${nom}${detail ? ` — ${detail}` : ''}`);
};

async function essai(page, { capVise, attendu, gagne }) {
  // régler le cap avec les boutons, depuis la valeur affichée
  const depart = Number((await page.locator('.nv-cap b').textContent()).replace('°', '').replace(',', '.'));
  const pas = Math.round((capVise - depart) * 10);
  const unites = Math.trunc(pas / 10);
  const dixiemes = pas - unites * 10;
  for (let i = 0; i < Math.abs(unites); i += 1) await page.getByRole('button', { name: unites < 0 ? '−1°' : '+1°', exact: true }).click();
  for (let i = 0; i < Math.abs(dixiemes); i += 1) await page.getByRole('button', { name: dixiemes < 0 ? '−0,1°' : '+0,1°', exact: true }).click();
  const capTexte = await page.locator('.nv-cap b').textContent();
  verifier(`cap affiché ${capVise}`, capTexte === `${capVise.toFixed(1).padStart(5, '0').replace('.', ',')}°`, capTexte);

  verifier('lancer bloqué sans prédiction', await page.getByRole('button', { name: 'Lancer le vol' }).isDisabled());
  const carte = page.locator('svg.nv-carte');
  const b = await carte.boundingBox();
  await carte.click({ position: { x: b.width * 0.85, y: b.height * 0.55 } });
  await page.getByRole('button', { name: 'Lancer le vol' }).click();
  verifier('cap bloqué pendant le vol', await page.getByRole('button', { name: '+1°', exact: true }).isDisabled());
  await page.getByRole('button', { name: 'Nouvel essai' }).waitFor({ timeout: 30000 });
  const titre = await page.locator('.nv-bilan h1').textContent();
  verifier(`résultat ${capVise}`, titre === (gagne ? 'Posé sur la piste' : 'À côté de la piste'), titre);
  const legende = await page.locator('.nv-seuil figcaption').textContent();
  verifier(`écart au seuil ${capVise}`, legende.includes(attendu), legende);
  verifier('formule KaTeX rendue', (await page.locator('.nv-formule .katex').count()) >= 1);
  const fps = await page.locator('.nv-bilan .nv-petit').last().textContent();
  return fps;
}

const navigateur = await chromium.launch({ executablePath: CHROME });
for (const [nom, options] of [
  ['telephone', { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true }],
  ['bureau', { viewport: { width: 1280, height: 900 } }],
]) {
  console.log(`\n— ${nom}`);
  const contexte = await navigateur.newContext(options);
  const page = await contexte.newPage();
  const erreurs = [];
  page.on('pageerror', (e) => erreurs.push(e.message));
  // /favicon.ico manque sur tout le site (hors du niveau) : ignoré ici
  page.on('console', (m) => m.type() === 'error' && !m.location().url.endsWith('/favicon.ico') && erreurs.push(m.text()));
  page.on('response', (r) => r.status() >= 400 && !r.url().endsWith('/favicon.ico') && erreurs.push(`${r.status()} ${r.url()}`));
  await page.goto(`${base}/niveau/vent-de-travers/?fps=1`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: `${captures}/${nom}-depart.png`, fullPage: true });
  const largeur = await page.evaluate(() => [document.documentElement.scrollWidth, window.innerWidth]);
  verifier('pas de défilement horizontal', largeur[0] <= largeur[1], `${largeur[0]} ≤ ${largeur[1]}`);

  await essai(page, { capVise: 90, attendu: '24,46 km au sud', gagne: false });
  await page.screenshot({ path: `${captures}/${nom}-cap090.png`, fullPage: true });
  await page.getByRole('button', { name: 'Nouvel essai' }).click();
  await essai(page, { capVise: 83.6, attendu: '35 m', gagne: true });
  await page.screenshot({ path: `${captures}/${nom}-cap0836.png`, fullPage: true });

  const stock = await page.evaluate(() => JSON.parse(localStorage.getItem('niveau-vent-tentatives') || '[]'));
  verifier('2 tentatives enregistrées en JSON', stock.length === 2 && stock[1].gagne === true && stock[0].gagne === false, JSON.stringify(stock[1]));

  if (nom === 'telephone') {
    // garde-fou seulement : processeur ralenti ×4 ; l'épreuve réelle se fait sur un vrai téléphone Android
    const cdp = await contexte.newCDPSession(page);
    await cdp.send('Emulation.setCPUThrottlingRate', { rate: 4 });
    await page.getByRole('button', { name: 'Nouvel essai' }).click();
    await page.getByRole('button', { name: '+1°', exact: true }).click();
    const fps = await essai(page, { capVise: 84.6, attendu: 'au', gagne: false });
    console.log(`  garde-fou ×4 : ${fps}`);
  }
  verifier('aucune erreur dans la console', erreurs.length === 0, erreurs.join(' | '));
  await contexte.close();
}
await navigateur.close();
const echecs = resultats.filter((r) => !r.ok).length;
console.log(`\n${resultats.length - echecs}/${resultats.length} vérifications réussies`);
process.exit(echecs ? 1 : 0);
