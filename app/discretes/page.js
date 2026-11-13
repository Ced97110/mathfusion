import Link from 'next/link';
import { getDiscretes } from '../../lib/discretes';

export const metadata = { title: 'Mathématiques discrètes — cause, effets, finalité' };

function Entries({ items }) {
  return (
    <ul className="chl">
      {items.map((c) => (
        <li key={c.key}>
          <Link href={`/discretes/${c.key}/`}>
            {c.label && <span className="k">{c.label.replace(/^(Chapitre|Annexe) /, '')}</span>}
            <span>{c.title}</span>
          </Link>
        </li>
      ))}
    </ul>
  );
}

export default function Discretes() {
  const { front, chapters, annexes } = getDiscretes();
  return (
    <div id="home">
      <div className="ck">Mathématiques discrètes</div>
      <h1>Cause, effets, finalité</h1>
      <p className="lead">D’après Oscar Levin, Discrete Mathematics: An Open Introduction.</p>
      <p className="st">{chapters.length} chapitres · {annexes.length} annexes</p>
      <Entries items={front} />
      <section className="bs">
        <h2>Chapitres</h2>
        <Entries items={chapters} />
      </section>
      <section className="bs">
        <h2>Annexes</h2>
        <Entries items={annexes} />
      </section>
    </div>
  );
}
