'use client';
// Le lecteur d'un chapitre : charge public/chapters/chNN.html, suit la fiche en cours,
// et permet de passer d'une fiche ou d'une partie à l'autre.
// Le chapitre n'est pas inclus dans la page elle-même : il pèse 2 à 7 Mo,
// et l'inclure ferait copier ce poids plusieurs fois dans le site construit.
import { useCallback, useEffect, useRef, useState } from 'react';
import Link from 'next/link';

const READ_LINE = 0.4; // part de la hauteur de la fenêtre : la fiche qui touche cette ligne est la fiche en cours

const fetchText = (url) =>
  fetch(url).then((r) => { if (!r.ok) throw new Error(String(r.status)); return r.text(); });

function Goto({ id, onGo, message }) {
  return (
    <form className="goto" onSubmit={(e) => { e.preventDefault(); onGo(new FormData(e.currentTarget).get('fiche') || ''); }}>
      <label htmlFor={id}>Aller à la fiche</label>
      <input id={id} name="fiche" placeholder="06-012" inputMode="numeric" autoComplete="off" aria-describedby={`${id}-msg`} />
      <button type="submit">Aller</button>
      <p id={`${id}-msg`} className="gmsg" role="status">{message}</p>
    </form>
  );
}

function Parts({ parts, current, onPick }) {
  return (
    <ol className="parts">
      {parts.map((p, i) => (
        <li key={p.id}>
          <a href={`#${p.id}`} className={i === current ? 'on' : undefined} aria-current={i === current ? 'true' : undefined} onClick={onPick}>
            <span className="pt" dangerouslySetInnerHTML={{ __html: p.title }} />
            <span className="pc">{p.n}</span>
          </a>
        </li>
      ))}
    </ol>
  );
}

export default function Reader({ file, prefix, label, title, parts, total, chapters, prev, next }) {
  const body = useRef(null);
  const articles = useRef([]);
  const tops = useRef([]);
  const idxRef = useRef(-1);
  const [state, setState] = useState('loading');
  const [idx, setIdx] = useState(-1);
  const [sheet, setSheet] = useState(false);
  const [message, setMessage] = useState('');

  const locate = useCallback(() => {
    const y = window.scrollY + window.innerHeight * READ_LINE;
    const t = tops.current;
    let lo = 0;
    let hi = t.length - 1;
    let found = -1;
    while (lo <= hi) {
      const mid = (lo + hi) >> 1;
      if (t[mid] <= y) { found = mid; lo = mid + 1; } else { hi = mid - 1; }
    }
    if (found !== idxRef.current) { idxRef.current = found; setIdx(found); }
  }, []);

  const measure = useCallback(() => {
    tops.current = articles.current.map((a) => a.getBoundingClientRect().top + window.scrollY);
    locate();
  }, [locate]);

  // Chargement du chapitre.
  useEffect(() => {
    let alive = true;
    // Vercel (trailingSlash) sert public/chapters/chNN.html à /chapters/chNN/ seulement :
    // on essaie le nom du fichier, puis l'adresse sans extension.
    fetchText(`/chapters/${file}`)
      .catch(() => fetchText(`/chapters/${file.replace(/\.html$/, '/')}`))
      .then((html) => {
        if (!alive || !body.current) return;
        body.current.innerHTML = html;
        articles.current = [...body.current.querySelectorAll('article.fiche')];
        setState('ready');
        const target = decodeURIComponent(window.location.hash.slice(1));
        const el = target && document.getElementById(target);
        if (el) el.scrollIntoView();
      })
      .catch(() => alive && setState('error'));
    return () => { alive = false; };
  }, [file]);

  // Suivi de la fiche en cours.
  useEffect(() => {
    if (state !== 'ready') return undefined;
    let frame = 0;
    const onScroll = () => {
      if (frame) return;
      frame = requestAnimationFrame(() => { frame = 0; locate(); });
    };
    const observer = new ResizeObserver(measure);
    observer.observe(body.current);
    window.addEventListener('scroll', onScroll, { passive: true });
    measure();
    return () => {
      observer.disconnect();
      window.removeEventListener('scroll', onScroll);
      if (frame) cancelAnimationFrame(frame);
    };
  }, [state, locate, measure]);

  const show = useCallback((el) => {
    el.scrollIntoView();
    window.history.replaceState(null, '', `#${el.id}`);
  }, []);

  // Passe à la fiche précédente (-1) ou suivante (+1). Au bout du chapitre, la page bouge un peu et revient.
  const step = useCallback((dir) => {
    const list = articles.current;
    const to = idxRef.current + dir;
    if (to >= 0 && to < list.length) { show(list[to]); return; }
    if (to < 0 && idxRef.current === 0) { window.scrollTo(0, 0); return; }
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    body.current.animate(
      [{ transform: 'translateX(0)' }, { transform: `translateX(${dir * -12}px)` }, { transform: 'translateX(0)' }],
      { duration: 200, easing: 'ease-out' },
    );
  }, [show]);

  const goTo = useCallback((text) => {
    const m = String(text).trim().match(/^(?:(\d{1,2})\s*[-.\s]\s*)?(\d{1,3})$/);
    if (!m) { setMessage('Écrivez un numéro de fiche, par exemple 06-012.'); return; }
    const chap = m[1] ? m[1].padStart(2, '0') : prefix;
    const code = `${chap}-${m[2].padStart(3, '0')}`;
    if (chap === prefix) {
      const el = document.getElementById(`f${code}`);
      if (!el) { setMessage(`La fiche ${code} n’existe pas dans ce chapitre.`); return; }
      setMessage('');
      setSheet(false);
      show(el);
      return;
    }
    const other = chapters.find((c) => c.prefix === chap);
    if (!other) { setMessage(`Le chapitre ${Number(chap)} n’est pas encore publié.`); return; }
    window.location.href = `/chapitre/${other.slug}/#f${code}`;
  }, [prefix, chapters, show]);

  // Touches ← et → : fiche précédente, fiche suivante. Échap ferme la liste des parties.
  useEffect(() => {
    const onKey = (e) => {
      if (e.key === 'Escape') { setSheet(false); return; }
      if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
      if (e.target.closest && e.target.closest('input, textarea, select')) return;
      if (e.key === 'ArrowLeft') step(-1);
      if (e.key === 'ArrowRight') step(1);
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [step]);

  // La liste des parties en plein écran bloque le défilement de la page.
  useEffect(() => {
    document.body.style.overflow = sheet ? 'hidden' : '';
    return () => { document.body.style.overflow = ''; };
  }, [sheet]);

  let current = -1;
  parts.forEach((p, i) => { if (idx >= p.start && p.n > 0) current = i; });
  const code = idx >= 0 && articles.current[idx] ? articles.current[idx].id.slice(1) : '';
  const chapterNav = (
    <nav className="pn" aria-label="Chapitres voisins">
      {prev ? <Link href={prev.href}>‹ {prev.label}</Link> : <span />}
      {next ? <Link href={next.href}>{next.label} ›</Link> : <span />}
    </nav>
  );

  return (
    <div className="reader">
      <aside className="rail" aria-label="Parties du chapitre">
        <div className="rk">{label}</div>
        <div className="rt">{title}</div>
        <Parts parts={parts} current={current} />
        {chapterNav}
      </aside>

      <div className="rcol">
        <div className="rbar">
          <button type="button" className="ib" onClick={() => step(-1)} aria-label="Fiche précédente">‹</button>
          <div className="pos">
            {code ? <><b>{code}</b><span>fiche {idx + 1} sur {total}</span></> : <span>{label} · {total} fiches</span>}
          </div>
          <Goto id="goto-bar" onGo={goTo} message={message} />
          <button type="button" className="pb" onClick={() => setSheet(true)} aria-haspopup="dialog">Parties</button>
          <button type="button" className="ib" onClick={() => step(1)} aria-label="Fiche suivante">›</button>
        </div>
        {state === 'loading' && <p id="load">Chargement du chapitre…</p>}
        {state === 'error' && <p id="load">Ce chapitre n’a pas pu être chargé. Rechargez la page.</p>}
        <div id="chap" ref={body} />
        {state === 'ready' && chapterNav}
      </div>

      <div className={sheet ? 'sheet on' : 'sheet'} role="dialog" aria-modal="true" aria-label="Parties du chapitre" inert={!sheet}>
        <div className="sh">
          <div>
            <div className="rk">{label}</div>
            <div className="rt">{title}</div>
          </div>
          <button type="button" className="pb" onClick={() => setSheet(false)}>Fermer</button>
        </div>
        <Goto id="goto-sheet" onGo={goTo} message={message} />
        <Parts parts={parts} current={current} onPick={() => setSheet(false)} />
        {chapterNav}
      </div>
    </div>
  );
}
