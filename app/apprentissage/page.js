import Link from 'next/link';
import { getMl, mlNum, ML_TITLE } from '../../lib/ml';

export const metadata = { title: `${ML_TITLE} — sommaire` };

function Item({ c }) {
  const num = mlNum(c);
  return (
    <li>
      <Link href={`/apprentissage/${c.key}/`}>
        <span className="k">{num}</span>
        <span>{c.title}</span>
      </Link>
    </li>
  );
}

export default function MlHome() {
  const toc = getMl();
  const n = toc.parts.reduce((a, p) => a + p.chapters.filter((c) => mlNum(c)).length, 0);
  return (
    <div id="home">
      <div className="ck">Algèbre linéaire, analyse, probabilités et statistiques</div>
      <h1>{ML_TITLE}</h1>
      <p className="lead">Cause, effets, finalité. Texte français, traduction anglaise en bleu.</p>
      <p className="st">{n} chapitres · d’après Jorge Brasil, Before Machine Learning, vol. 1 à 3</p>
      <ul className="chl">
        {toc.front.map((c) => <Item key={c.key} c={c} />)}
      </ul>
      {toc.parts.map((p) => (
        <section key={p.title} className="bs">
          <h3 className="bt">{p.num} · {p.title}</h3>
          {p.en && <div className="mlen">{p.en}</div>}
          <ul className="chl">
            {p.chapters.map((c) => <Item key={c.key} c={c} />)}
          </ul>
        </section>
      ))}
    </div>
  );
}
