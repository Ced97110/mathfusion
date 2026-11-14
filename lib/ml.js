// Second book: « Avant l'apprentissage automatique — cause, effets, finalité ».
// content/ml.json is written by tools/ml/build.py; chapter files are in public/ml/cNNN.html.
import fs from 'node:fs';
import path from 'node:path';

export const ML_TITLE = 'Avant l’apprentissage automatique';

/** Table of contents, keeping only the chapters whose file is present (chapters are committed one by one). */
export function getMl() {
  const toc = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'content', 'ml.json'), 'utf8'));
  const has = (c) => fs.existsSync(path.join(process.cwd(), 'public', 'ml', c.file));
  return {
    front: toc.front.filter(has),
    parts: toc.parts.map((p) => ({ ...p, chapters: p.chapters.filter(has) })).filter((p) => p.chapters.length),
  };
}

/** Every page of the book in reading order: front texts, then the chapters of each part. */
export function mlEntries() {
  const toc = getMl();
  return [
    ...toc.front.map((c) => ({ ...c, part: null })),
    ...toc.parts.flatMap((p) => p.chapters.map((c) => ({ ...c, part: p }))),
  ];
}

/** Chapter number, or '' for the opening texts (keys 01, 02) and the « Contrôle final ». */
export function mlNum(c) {
  return /^\d{3}$/.test(c.key) ? Number(c.key) : '';
}

export function mlLabel(c) {
  return mlNum(c) ? `Chapitre ${mlNum(c)}` : c.title;
}
