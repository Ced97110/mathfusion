import Link from 'next/link';
import { getBranches } from '../../lib/book';

/** Menu of the branches of mathematics, shown under the top bar on every page. */
export default function BranchMenu() {
  return (
    <nav id="br" aria-label="Branches des mathématiques">
      {getBranches().map((b) => (
        <Link key={b.slug} href={`/branche/${b.slug}/`}>
          {b.title}
        </Link>
      ))}
    </nav>
  );
}
