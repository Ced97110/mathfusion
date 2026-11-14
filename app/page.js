import Link from 'next/link';
import { getToc, slugOf, labelOf, getBranches } from '../lib/book';
import ChapterList from './components/ChapterList';

const ROLES = [
  ['#d6e4f2', '#1f4e79', 'Bleu', 'l’objet défini'],
  ['#fbe3cf', '#b8500a', 'Orange', 'ce qui change, l’action'],
  ['#eceef1', '#5f6773', 'Gris', 'ce qui ne change pas'],
  ['#d5eedd', '#1a7445', 'Vert', 'ce qu’on obtient, ce qui est vrai'],
  ['#f8d9d6', '#b3261e', 'Rouge', 'ce qui est faux, le contre-exemple'],
  ['#e6daf3', '#6d3fa0', 'Violet', 'un second objet, comparé au premier'],
];

// Une phrase pour les chapitres qui ne sont pas encore publiés.
function upcoming(todo) {
  const numbers = todo.map((c) => Number(c.key)).filter((n) => !Number.isNaN(n));
  const others = todo.filter((c) => Number.isNaN(Number(c.key))).map((c) => labelOf(c).toLowerCase());
  const range = numbers.length ? [`les chapitres ${Math.min(...numbers)} à ${Math.max(...numbers)}`] : [];
  return `À venir : ${[...range, ...others.map((o) => `l’${o}`)].join(', ')}.`;
}

export default function Home() {
  const toc = getToc();
  const done = toc.filter((c) => c.file);
  const todo = toc.filter((c) => !c.file);
  const first = done.find((c) => c.key === '1') ?? done[0];
  const byKey = new Map(toc.map((c) => [String(c.key), c]));
  return (
    <div id="home">
      <section className="hero">
        <h1>Une figure avant chaque formule.</h1>
        <p className="sub">
          Arithmétique, algèbre, trigonométrie, algèbre abstraite : un livre unique tiré de six ouvrages.{' '}
          <span className="wide">Il part du comptage des nombres entiers et va jusqu’aux groupes et à la théorie de Galois.{' '}</span>
          {done.length}&nbsp;sections publiées sur {toc.length}.
        </p>
        <div className="cta">
          {first && <Link className="btn" href={`/chapitre/${slugOf(first)}/`}>Commencer au chapitre&nbsp;{first.key}</Link>}
          <a className="lk" href="#chapitres">Voir tous les chapitres</a>
        </div>
      </section>

      <section className="how">
        <div>
          <h2>Une couleur garde le même rôle</h2>
          <div className="roles">
            {ROLES.map(([bg, fg, name, role]) => (
              <div key={name}>
                <i style={{ background: bg, borderColor: fg }} />
                <b style={{ color: fg }}>{name}</b> {role}
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="chap" id="chapitres">
        <h2>Chapitres par branche</h2>
        <ChapterList chapters={toc.filter((c) => c.key === 'AP')} />
        {getBranches().map((b) => (
          <section key={b.slug} className="bs">
            <h3 className="bt">
              <Link href={`/branche/${b.slug}/`}>{b.title}</Link>
            </h3>
            {b.sections.map((sec) => (
              <div key={sec.title}>
                {b.sections.length > 1 && <div className="ss">{sec.title}</div>}
                <ChapterList chapters={sec.chapters.map((k) => byKey.get(k)).filter(Boolean)} />
              </div>
            ))}
          </section>
        ))}
        <ChapterList chapters={toc.filter((c) => c.key === 'A')} />
        {todo.length > 0 && <p className="avt">{upcoming(todo)}</p>}
        {first && <Link className="btn" href={`/chapitre/${slugOf(first)}/`}>Commencer au chapitre&nbsp;{first.key}</Link>}
      </section>

      <footer className="foot">Des nombres aux structures — cause, effets, finalité</footer>
    </div>
  );
}
