import { notFound } from 'next/navigation';
import Link from 'next/link';
import { getToc, slugOf, labelOf, prefixOf, getParts, branchOf } from '../../../lib/book';
import Reader from './Reader';

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

const link = (c) => (c ? { href: `/chapitre/${slugOf(c)}/`, label: labelOf(c) } : null);

export default async function Chapter({ params }) {
  const { key } = await params;
  const done = getToc().filter((c) => c.file);
  const i = done.findIndex((c) => slugOf(c) === key);
  if (i < 0) notFound();
  const c = done[i];
  const parts = getParts(c.file);
  const branch = branchOf(c.key);
  return (
    <>
      {branch && (
        <p className="crumb">
          <Link href={`/branche/${branch.slug}/`}>{branch.title}</Link>
        </p>
      )}
      <Reader
      file={c.file}
      prefix={prefixOf(c)}
      label={labelOf(c)}
      title={c.title}
      parts={parts}
      total={parts.reduce((a, p) => a + p.n, 0)}
      chapters={done.map((d) => ({ prefix: prefixOf(d), slug: slugOf(d) }))}
      prev={link(done[i - 1])}
      next={link(done[i + 1])}
      />
    </>
  );
}
