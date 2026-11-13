import Link from 'next/link';
import { slugOf, labelOf } from '../../lib/book';

/**
 * One list of chapters: done chapters are links, the others are greyed out.
 * base: URL prefix of a chapter page (another book, e.g. "/discretes/").
 */
export default function ChapterList({ chapters, base = '/chapitre/' }) {
  return (
    <ul className="chl">
      {chapters.map((c) => (
        <li key={c.key}>
          {c.file ? (
            <Link href={`${base}${slugOf(c)}/`}>
              <span className="k">{c.num ?? c.key}</span>
              <span>{c.title}</span>
              {c.n ? <span className="c">{c.n} fiches</span> : null}
            </Link>
          ) : (
            <span className="na">
              <span className="k">{c.key}</span>
              <span>{labelOf(c)}</span>
              <span className="c">à venir</span>
            </span>
          )}
        </li>
      ))}
    </ul>
  );
}
