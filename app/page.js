import Link from 'next/link';
import { getToc, slugOf, labelOf, getFiche } from '../lib/book';

// La fiche montrée en vitrine. Si elle disparaît, la première fiche du premier chapitre la remplace.
const SHOWCASE = { file: 'ch06.html', id: 'f06-025' };

const RUBRIQUES = [
  ['cas', 'Le cas concret', 'Une situation avec des nombres précis.'],
  ['signes', 'La lecture des signes', 'Ce que veut dire chaque signe nouveau.'],
  ['fig', 'La figure', 'Elle reprend les nombres du cas concret.'],
  ['question', 'La question', 'La question à laquelle le concept répond.'],
  ['reponse', 'La réponse', 'La réponse, en phrases courtes.'],
  ['limite', 'La limite', 'Ce que la fiche ne dit pas.'],
  ['lien', 'Le lien', 'La fiche à lire avec celle-ci.'],
];

const ROLES = [
  ['#d6e4f2', '#1f4e79', 'Bleu', 'l’objet que la fiche définit'],
  ['#fbe3cf', '#b8500a', 'Orange', 'ce qui change, l’action'],
  ['#eceef1', '#5f6773', 'Gris', 'ce qui ne change pas'],
  ['#d5eedd', '#1a7445', 'Vert', 'ce qu’on obtient, ce qui est vrai'],
  ['#f8d9d6', '#b3261e', 'Rouge', 'ce qui est faux, le contre-exemple'],
  ['#e6daf3', '#6d3fa0', 'Violet', 'un second objet, comparé au premier'],
];

function showcase(done) {
  const wanted = done.find((c) => c.file === SHOWCASE.file);
  const fiche = wanted && getFiche(SHOWCASE.file, SHOWCASE.id);
  if (fiche) return { fiche, chapter: wanted };
  const first = done[0];
  if (!first) return null;
  const id = `f${first.file.replace(/^ch|\.html$/g, '')}-001`;
  const fallback = getFiche(first.file, id);
  return fallback ? { fiche: fallback, chapter: first } : null;
}

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
  const fiches = done.reduce((a, c) => a + c.n, 0);
  const shown = showcase(done);
  const first = done[0];
  return (
    <div id="home">
      <section className="hero">
        <h1>Une fiche par concept. Une figure par fiche.</h1>
        <p className="sub">
          Un livre de mathématiques en fiches illustrées.{' '}
          <span className="wide">Il part du comptage des nombres entiers et va jusqu’aux groupes et à la théorie de Galois.{' '}</span>
          {fiches}&nbsp;fiches sont publiées,
          dans {done.length}&nbsp;chapitres sur {toc.length}.
        </p>
        <div className="cta">
          {first && <Link className="btn" href={`/chapitre/${slugOf(first)}/`}>Commencer au chapitre&nbsp;{first.key}</Link>}
          <a className="lk" href="#chapitres">Voir les {done.length} chapitres publiés</a>
        </div>
      </section>

      {shown && (
        <section className="vitrine" id="lire" aria-label={`Fiche ${shown.fiche.code}`}>
          <div className="vt">
            <div className="code"><span className="cid">Fiche {shown.fiche.code}</span><span>{labelOf(shown.chapter)}</span></div>
            <h2 dangerouslySetInnerHTML={{ __html: shown.fiche.title }} />
            <div className="rub cas">
              <h3 className="r cas"><span className="n">1</span>Le cas concret</h3>
              <div dangerouslySetInnerHTML={{ __html: shown.fiche.cas }} />
            </div>
            <Link className="lk" href={`/chapitre/${slugOf(shown.chapter)}/#${shown.fiche.id}`}>
              Lire la fiche entière dans le chapitre&nbsp;{shown.chapter.key}
            </Link>
          </div>
          <figure dangerouslySetInnerHTML={{ __html: shown.fiche.figure }} />
        </section>
      )}

      <section className="how">
        <div>
          <h2>Toutes les fiches ont le même plan</h2>
          <ol className="plan">
            {RUBRIQUES.map(([k, name, text]) => (
              <li key={name} className={k}>
                <b>{name}</b>
                <span className="d">{text}</span>
              </li>
            ))}
          </ol>
        </div>
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
        <h2>Chapitres publiés</h2>
        <ul id="chl">
          {done.map((c) => (
            <li key={c.key}>
              <Link href={`/chapitre/${slugOf(c)}/`}>
                <span className="k">{c.key}</span>
                <span className="ti">{c.title}</span>
                <span className="c">{c.n} fiches</span>
              </Link>
            </li>
          ))}
        </ul>
        {todo.length > 0 && <p className="avt">{upcoming(todo)}</p>}
        {first && <Link className="btn" href={`/chapitre/${slugOf(first)}/`}>Commencer au chapitre&nbsp;{first.key}</Link>}
      </section>

      <footer className="foot">Des nombres aux structures — fiches illustrées</footer>
    </div>
  );
}
