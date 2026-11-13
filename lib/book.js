// Lecture du contenu du livre au moment de la construction du site.
// content/toc.json : la liste des 82 chapitres. Le contenu d'un chapitre fait est dans public/chapters/chNN.html.
import fs from 'node:fs';
import path from 'node:path';

const dir = path.join(process.cwd(), 'content');
const chaptersDir = path.join(process.cwd(), 'public', 'chapters');

export function getToc() {
  return JSON.parse(fs.readFileSync(path.join(dir, 'toc.json'), 'utf8'));
}
export function slugOf(c) { return String(c.key).toLowerCase(); }
export function labelOf(c) {
  return c.key === 'AP' ? 'Avant-propos' : c.key === 'A' ? 'Annexe' : `Chapitre ${c.key}`;
}
// "ch06.html" -> "06" : le préfixe des codes de fiche du chapitre (06-025).
export function prefixOf(c) { return c.file.replace(/^ch|\.html$/g, ''); }

function readChapter(file) {
  return fs.readFileSync(path.join(chaptersDir, file), 'utf8');
}

// Les parties d'un chapitre : identifiant, titre (HTML), nombre de fiches, rang de la première fiche.
export function getParts(file) {
  const chunks = readChapter(file).split('<section class="sec" id="').slice(1);
  let start = 0;
  return chunks.map((chunk) => {
    const id = chunk.slice(0, chunk.indexOf('"'));
    const title = (chunk.match(/<h1>([\s\S]*?)<\/h1>/) || [, id])[1];
    const n = (chunk.match(/<article class="fiche" id="/g) || []).length;
    const part = { id, title, n, start };
    start += n;
    return part;
  });
}

// Une fiche d'un chapitre, découpée pour la vitrine de l'accueil. Rend null si elle n'existe pas.
export function getFiche(file, id) {
  let html;
  try { html = readChapter(file); } catch { return null; }
  const from = html.indexOf(`<article class="fiche" id="${id}">`);
  if (from < 0) return null;
  const art = html.slice(from, html.indexOf('</article>', from));
  const pick = (re) => (art.match(re) || [, ''])[1];
  const fiche = {
    id,
    code: id.slice(1),
    title: pick(/<h2>([\s\S]*?)<\/h2>/),
    cas: pick(/<div class="rub cas">[\s\S]*?<\/h3>([\s\S]*?)<\/div><div class="rub signes/),
    figure: pick(/<figure>([\s\S]*?)<\/figure>/),
  };
  return fiche.title && fiche.figure ? fiche : null;
}
