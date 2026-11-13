import { notFound } from 'next/navigation';
import { getToc, getBranches } from '../../../lib/book';
import ChapterList from '../../components/ChapterList';

// One static page per branch of mathematics.
export function generateStaticParams() {
  return getBranches().map((b) => ({ slug: b.slug }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }) {
  const { slug } = await params;
  const b = getBranches().find((x) => x.slug === slug);
  return b ? { title: `${b.title} — Des nombres aux structures` } : {};
}

export default async function Branch({ params }) {
  const { slug } = await params;
  const b = getBranches().find((x) => x.slug === slug);
  if (!b) notFound();
  const toc = new Map(getToc().map((c) => [String(c.key), c]));
  const all = b.sections.flatMap((s) => s.chapters.map((k) => toc.get(k)).filter(Boolean));
  const done = all.filter((c) => c.file);
  return (
    <div id="home">
      <div className="ck">Branche</div>
      <h1>{b.title}</h1>
      <p className="st">
        {done.length} chapitres disponibles sur {all.length} · {done.reduce((a, c) => a + c.n, 0)} fiches illustrées
      </p>
      {b.sections.map((s) => (
        <section key={s.title} className="bs">
          <h2>{s.title}</h2>
          <ChapterList chapters={s.chapters.map((k) => toc.get(k)).filter(Boolean)} />
        </section>
      ))}
    </div>
  );
}
