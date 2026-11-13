import Link from 'next/link';
import { notFound } from 'next/navigation';
import { mlEntries, mlLabel, ML_TITLE } from '../../../lib/ml';
import ChapterBody from '../../chapitre/[key]/ChapterBody';

// One static page per chapter of the machine learning book.
export function generateStaticParams() {
  return mlEntries().map((c) => ({ key: c.key }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }) {
  const { key } = await params;
  const c = mlEntries().find((x) => x.key === key);
  return c ? { title: `${mlLabel(c)} — ${c.title}` } : {};
}

export default async function MlChapter({ params }) {
  const { key } = await params;
  const all = mlEntries();
  const i = all.findIndex((c) => c.key === key);
  if (i < 0) notFound();
  const c = all[i];
  const prev = all[i - 1];
  const next = all[i + 1];
  const nav = (
    <nav className="pn" aria-label="Chapitres voisins">
      {prev ? <Link href={`/apprentissage/${prev.key}/`}>‹ {mlLabel(prev)}</Link> : <span />}
      {next ? <Link href={`/apprentissage/${next.key}/`}>{mlLabel(next)} ›</Link> : <span />}
    </nav>
  );
  return (
    <>
      <p className="crumb">
        <Link href="/apprentissage/">{ML_TITLE}</Link>
        {c.part && ` · ${c.part.num} ${c.part.title}`}
      </p>
      {nav}
      {/* HTML written by tools/ml/build.py: the book's text plus SVG bands cut out of the PDF. */}
      <div className="ml">
        <ChapterBody file={c.file} dir="ml" />
      </div>
      {nav}
    </>
  );
}
