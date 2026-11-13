import Link from 'next/link';
import { getToc, slugOf, labelOf } from '../lib/book';

const ROLES = [
  ['#d6e4f2', '#1f4e79', 'Bleu', 'l’objet que la fiche définit'],
  ['#fbe3cf', '#b8500a', 'Orange', 'ce qui change, l’action'],
  ['#eceef1', '#5f6773', 'Gris', 'ce qui ne change pas'],
  ['#d5eedd', '#1a7445', 'Vert', 'ce qu’on obtient, ce qui est vrai'],
  ['#f8d9d6', '#b3261e', 'Rouge', 'ce qui est faux, le contre-exemple'],
  ['#e6daf3', '#6d3fa0', 'Violet', 'un second objet, comparé au premier'],
];

export default function Home() {
  const toc = getToc();
  const done = toc.filter((c) => c.file);
  const fiches = done.reduce((a, c) => a + c.n, 0);
  return (
    <div id="home">
      <div className="ck">Fiches illustrées</div>
      <h1>Des nombres aux structures</h1>
      <p className="lead">Une fiche par concept, une figure par fiche.</p>
      <p className="st">{done.length} chapitres disponibles sur {toc.length} · {fiches} fiches illustrées</p>

      <h2>Comment lire une figure</h2>
      <p>Chaque fiche contient une figure, placée après le cas concret et la lecture des signes. La figure reprend les nombres du cas concret. Sous la figure, la rubrique « lecture » dit ce que chaque élément représente.</p>
      <p>Dans toutes les figures, une couleur garde le même rôle :</p>
      <div className="roles">
        {ROLES.map(([bg, fg, name, role]) => (
          <div key={name}>
            <i style={{ background: bg, borderColor: fg }} />
            <b style={{ color: fg }}>{name}</b> {role}
          </div>
        ))}
      </div>

      <h2>Chapitres</h2>
      <ul id="chl">
        {toc.map((c) => (
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
    </div>
  );
}
