import Link from 'next/link';
import { getPhysique } from '../../lib/physique';

export const metadata = { title: 'Physique — Cause, effets, finalité' };

export default function Physique() {
  const { front, parts } = getPhysique();
  const n = parts.reduce((a, p) => a + p.chapters.length, 0);
  return (
    <div id="home">
      <div className="ck">Physique et chimie</div>
      <h1>Cause, effets, finalité</h1>
      <p className="lead">D’après les Feynman Lectures on Physics et Physique-Chimie MPSI.</p>
      <p className="st">
        {parts.length} parties · {n} chapitres
      </p>
      <ul className="chl">
        {front.map((f) => (
          <li key={f.key}>
            <Link href={`/physique/${f.key}/`}>
              <span>{f.title}</span>
            </Link>
          </li>
        ))}
      </ul>
      {parts.map((p, i) => (
        <section key={p.title} className="bs">
          <h2>
            Partie {i + 1} · {p.title}
          </h2>
          <ul className="chl">
            {p.chapters.map((c) => (
              <li key={c.key}>
                <Link href={`/physique/${c.key}/`}>
                  <span className="k">{c.key}</span>
                  <span>{c.title}</span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  );
}
