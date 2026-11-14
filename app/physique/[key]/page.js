import Link from 'next/link';
import { notFound } from 'next/navigation';
import { physiquePages } from '../../../lib/physique';
import ChapterBody from '../../chapitre/[key]/ChapterBody';

// One static page per chapter of the physics book.
export function generateStaticParams() {
  return physiquePages().map((c) => ({ key: c.key }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }) {
  const { key } = await params;
  const c = physiquePages().find((x) => x.key === key);
  return c ? { title: `Physique — ${c.title}` } : {};
}

export default async function PhysiqueChapter({ params }) {
  const { key } = await params;
  const pages = physiquePages();
  const i = pages.findIndex((c) => c.key === key);
  if (i < 0) notFound();
  const c = pages[i];
  const prev = pages[i - 1];
  const next = pages[i + 1];
  const nav = (
    <nav className="pn" aria-label="Chapitres voisins">
      {prev ? <Link href={`/physique/${prev.key}/`}>‹ {prev.label}</Link> : <span />}
      {next ? <Link href={`/physique/${next.key}/`}>{next.label} ›</Link> : <span />}
    </nav>
  );
  return (
    <>
      <p className="crumb">
        <Link href="/physique/">Physique</Link>
        {c.part && ` · ${c.part}`}
      </p>
      {nav}
      {/* Texte du livre en HTML ; formules, encadrés et figures découpés du PDF en SVG. */}
      <ChapterBody file={c.file} dir="physique" />
      {nav}
    </>
  );
}
