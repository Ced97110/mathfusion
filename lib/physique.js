// Section « Physique » : le livre « Cause, effets, finalité » (physique et chimie).
// content/physique.json est écrit par tools/physique/build.py ; le contenu d'un chapitre
// est dans public/physique/cNNN.html.
import fs from 'node:fs';
import path from 'node:path';

export function getPhysique() {
  return JSON.parse(fs.readFileSync(path.join(process.cwd(), 'content', 'physique.json'), 'utf8'));
}

/** Every page in reading order: front matter, then the chapters of each part. */
export function physiquePages() {
  const { front, parts } = getPhysique();
  return [
    ...front.map((f) => ({ ...f, label: f.title })),
    ...parts.flatMap((p) => p.chapters.map((c) => ({ ...c, part: p.title, label: `Chapitre ${c.key}` }))),
  ];
}
