// Section « Mathématiques discrètes » : le livre « Mathématiques discrètes : cause, effets, finalité »
// (d'après Oscar Levin, Discrete Mathematics: An Open Introduction).
// content/discretes.json est écrit par tools/discretes/build.py ; le contenu d'une page
// est dans public/discretes/cNNN.html.
import fs from 'node:fs';
import path from 'node:path';

export function getDiscretes() {
  return JSON.parse(fs.readFileSync(path.join(process.cwd(), 'content', 'discretes.json'), 'utf8'));
}

/** Every page in reading order: front matter, chapters, appendices. */
export function discretesPages() {
  const { front, chapters, annexes } = getDiscretes();
  return [...front, ...chapters, ...annexes].map((c) => ({ ...c, label: c.label || c.title }));
}
