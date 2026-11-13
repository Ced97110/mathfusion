import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getToc, slugOf, labelOf, branchOf } from '../../../lib/book';
import ChapterBody from './ChapterBody';

// Une page statique par chapitre déjà fait.
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
  const prev = done[i - 1];
  const next = done[i + 1];
  const branch = branchOf(c.key);
  const nav = (
    <nav className="pn" aria-label="Chapitres voisins">
      {prev ? <Link href={`/chapitre/${slugOf(prev)}/`}>‹ {labelOf(prev)}</Link> : <span />}
      {next ? <Link href={`/chapitre/${slugOf(next)}/`}>{labelOf(next)} ›</Link> : <span />}
    </nav>
  );
  return (
    <>
      {branch && (
        <p className="crumb">
          <Link href={`/branche/${branch.slug}/`}>{branch.title}</Link>
        </p>
      )}
      {nav}
      {/* Le contenu du chapitre est du HTML produit par le kit (texte du livre + figures SVG). */}
      <ChapterBody file={c.file} />
      {nav}
    </>
  );
}
