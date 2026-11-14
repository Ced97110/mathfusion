import { notFound } from 'next/navigation';
import Link from 'next/link';
import { getToc, slugOf, labelOf, branchOf } from '../../../lib/book';
import ChapterBody from './ChapterBody';

// Une page statique par section du livre (avant-propos, chapitres 1 à 80, annexe).
export function generateStaticParams() {
  return getToc().filter((c) => c.file).map((c) => ({ key: slugOf(c) }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }) {
  const { key } = await params;
  const c = getToc().find((x) => slugOf(x) === key);
  return c ? { title: `${labelOf(c)} — ${c.title}` } : {};
}

export default async function Chapter({ params }) {
  const { key } = await params;
  const done = getToc().filter((c) => c.file);
  const i = done.findIndex((c) => slugOf(c) === key);
  if (i < 0) notFound();
  const c = done[i];
  const branch = branchOf(c.key);
  const prev = done[i - 1];
  const next = done[i + 1];
  const nav = (
    <nav className="pn" aria-label="Chapitres voisins">
      {prev ? <Link href={`/chapitre/${slugOf(prev)}/`}>‹ {labelOf(prev)}</Link> : <span />}
      {next ? <Link href={`/chapitre/${slugOf(next)}/`}>{labelOf(next)} ›</Link> : <span />}
    </nav>
  );
  return (
    <div className="lecture">
      {branch && (
        <p className="crumb">
          <Link href={`/branche/${branch.slug}/`}>{branch.title}</Link>
        </p>
      )}
      {nav}
      {/* HTML written by tools/livre/build.py: the book's text plus SVG bands cut out of the PDF. */}
      <ChapterBody file={c.file} />
      {nav}
    </div>
  );
}
