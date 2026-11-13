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

// content/branches.json : the chapters grouped by branch of mathematics (domains, then sections).
// Every chapter 1-80 must appear exactly once; the build fails otherwise.
// A branch with a "book" field lists the pages of another book (e.g. "discretes", see lib/discretes.js):
// its keys are that book's keys and are not checked against the 80 chapters.
export function getBranches() {
  const branches = JSON.parse(fs.readFileSync(path.join(dir, 'branches.json'), 'utf8'));
  const seen = branches.filter((b) => !b.book).flatMap((b) => b.sections.flatMap((s) => s.chapters));
  const expected = Array.from({ length: 80 }, (_, i) => String(i + 1));
  const missing = expected.filter((k) => !seen.includes(k));
  const extra = seen.filter((k, i) => !expected.includes(k) || seen.indexOf(k) !== i);
  if (missing.length || extra.length) {
    throw new Error(`content/branches.json: chapitres manquants ${missing} ; en trop ou en double ${extra}`);
  }
  return branches;
}
export function branchOf(key) {
  return getBranches().find((b) => !b.book && b.sections.some((s) => s.chapters.includes(String(key))));
}
