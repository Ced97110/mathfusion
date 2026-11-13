'use client';
// Charge le fichier du chapitre (public/chapters/chNN.html) et l'affiche.
// Le chapitre n'est pas inclus dans la page elle-même : un chapitre pèse 3 à 7 Mo,
// et l'inclure ferait copier ce poids plusieurs fois dans le site construit.
import { useEffect, useRef, useState } from 'react';

export default function ChapterBody({ file }) {
  const ref = useRef(null);
  const [state, setState] = useState('loading');
  useEffect(() => {
    let alive = true;
    fetch(`/chapters/${file}`)
      .then((r) => { if (!r.ok) throw new Error(String(r.status)); return r.text(); })
      .then((html) => {
        if (!alive || !ref.current) return;
        ref.current.innerHTML = html;
        setState('ready');
        const id = decodeURIComponent(window.location.hash.slice(1));
        const el = id && document.getElementById(id);
        if (el) el.scrollIntoView();
      })
      .catch(() => alive && setState('error'));
    return () => { alive = false; };
  }, [file]);
  return (
    <>
      {state === 'loading' && <p id="load">Chargement du chapitre…</p>}
      {state === 'error' && <p id="load">Ce chapitre n’a pas pu être chargé. Rechargez la page.</p>}
      <div id="chap" ref={ref} />
    </>
  );
}
