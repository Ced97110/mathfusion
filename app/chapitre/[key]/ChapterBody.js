'use client';
// Charge le fichier du chapitre (public/chapters/chNN.html) et l'affiche.
// Le chapitre n'est pas inclus dans la page elle-même : un chapitre pèse 3 à 7 Mo,
// et l'inclure ferait copier ce poids plusieurs fois dans le site construit.
import { useEffect, useRef, useState } from 'react';

/** @param {{ file: string, dir?: string }} props  dir: folder of public/ holding the file */
export default function ChapterBody({ file, dir = 'chapters' }) {
  const ref = useRef(null);
  const [state, setState] = useState('loading');
  useEffect(() => {
    let alive = true;
    // Vercel (trailingSlash) serves public/chapters/chNN.html at /chapters/chNN/ only:
    // try the file name first, then the clean URL.
    const get = (url) => fetch(url).then((r) => { if (!r.ok) throw new Error(String(r.status)); return r.text(); });
    get(`/${dir}/${file}`)
      .catch(() => get(`/${dir}/${file.replace(/\.html$/, '/')}`))
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
  }, [file, dir]);
  return (
    <>
      {state === 'loading' && <p id="load">Chargement du chapitre…</p>}
      {state === 'error' && <p id="load">Ce chapitre n’a pas pu être chargé. Rechargez la page.</p>}
      {/* discretes uses the main book layout (cover, sections); other books use the .livre style */}
      <div id="chap" className={dir === 'chapters' || dir === 'discretes' ? undefined : 'livre'} ref={ref} />
    </>
  );
}
