import Link from 'next/link';
import { slugOf, labelOf } from '../../lib/book';

/** One list of chapters: done chapters are links, the others are greyed out. */
export default function ChapterList({ chapters }) {
  return (
    <ul className="chl">
      {chapters.map((c) => (
        <li key={c.key}>
          {c.file ? (
            <Link href={`/chapitre/${slugOf(c)}/`}>
              <span className="k">{c.key}</span>
              <span>{c.title}</span>
              <span className="c">{c.n} fiches</span>
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
