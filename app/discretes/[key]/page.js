import Link from 'next/link';
import { notFound } from 'next/navigation';
import { discretesPages } from '../../../lib/discretes';
import ChapterBody from '../../chapitre/[key]/ChapterBody';

// One static page per chapter of the discrete mathematics book.
export function generateStaticParams() {
  return discretesPages().map((c) => ({ key: c.key }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }) {
  const { key } = await params;
  const c = discretesPages().find((x) => x.key === key);
  return c ? { title: `Mathématiques discrètes — ${c.title}` } : {};
}

export default async function DiscretesChapter({ params }) {
  const { key } = await params;
  const pages = discretesPages();
  const i = pages.findIndex((c) => c.key === key);
  if (i < 0) notFound();
  const prev = pages[i - 1];
  const next = pages[i + 1];
  const nav = (
    <nav className="pn" aria-label="Chapitres voisins">
      {prev ? <Link href={`/discretes/${prev.key}/`}>‹ {prev.label}</Link> : <span />}
      {next ? <Link href={`/discretes/${next.key}/`}>{next.label} ›</Link> : <span />}
    </nav>
  );
  return (
    <>
      <p className="crumb">
        <Link href="/discretes/">Mathématiques discrètes</Link>
      </p>
      {nav}
      {/* Texte du livre en HTML ; formules, encadrés, tableaux et figures découpés du PDF en SVG. */}
      <ChapterBody file={pages[i].file} dir="discretes" />
      {nav}
    </>
  );
}
