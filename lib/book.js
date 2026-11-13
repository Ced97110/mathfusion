// Lecture du contenu du livre au moment de la construction du site.
// content/toc.json : la liste des 82 chapitres. Le contenu d'un chapitre fait est dans public/chapters/chNN.html.
import fs from 'node:fs';
import path from 'node:path';

const dir = path.join(process.cwd(), 'content');

export function getToc() {
  return JSON.parse(fs.readFileSync(path.join(dir, 'toc.json'), 'utf8'));
}
export function slugOf(c) { return String(c.key).toLowerCase(); }
export function labelOf(c) {
  return c.key === 'AP' ? 'Avant-propos' : c.key === 'A' ? 'Annexe' : `Chapitre ${c.key}`;
}
