'use client';
// Molette tactile du cap : on tourne l'aiguille du doigt (au degré), les boutons règlent au dixième.
import { useRef } from 'react';
import { formatDeg } from '../../../lib/niveau_vent.js';

const R = 80;
const C = 100;
// Coordonnées arrondies au centième : le serveur et le navigateur doivent écrire le même texte (hydratation).
const r2 = (v) => Math.round(v * 100) / 100;
const norm = (d) => Math.round((((d % 360) + 360) % 360) * 10) / 10;

/** @param {{ cap: number, bloque: boolean, onChange: (cap:number) => void }} props */
export default function Molette({ cap, bloque, onChange }) {
  const svgRef = useRef(null);
  const glisse = useRef(false);

  function capDepuis(e) {
    const svg = svgRef.current;
    const pt = svg.createSVGPoint();
    pt.x = e.clientX;
    pt.y = e.clientY;
    const p = pt.matrixTransform(svg.getScreenCTM().inverse());
    const deg = (Math.atan2(p.x - C, -(p.y - C)) * 180) / Math.PI;
    return norm(Math.round(deg));
  }
  function bas(e) {
    if (bloque) return;
    glisse.current = true;
    e.currentTarget.setPointerCapture(e.pointerId);
    onChange(capDepuis(e));
  }
  function bouge(e) {
    if (glisse.current && !bloque) onChange(capDepuis(e));
  }
  function haut() {
    glisse.current = false;
  }
  function clavier(e) {
    if (bloque) return;
    const pas = e.shiftKey ? 0.1 : 1;
    if (e.key === 'ArrowRight' || e.key === 'ArrowUp') onChange(norm(cap + pas));
    else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') onChange(norm(cap - pas));
    else return;
    e.preventDefault();
  }

  const a = (cap * Math.PI) / 180;
  const graduations = [];
  for (let d = 0; d < 360; d += 10) {
    const r = (d * Math.PI) / 180;
    const long = d % 90 === 0 ? 12 : 6;
    graduations.push(
      <line
        key={d}
        x1={r2(C + R * Math.sin(r))}
        y1={r2(C - R * Math.cos(r))}
        x2={r2(C + (R - long) * Math.sin(r))}
        y2={r2(C - (R - long) * Math.cos(r))}
        stroke="var(--gris)"
        strokeWidth={d % 90 === 0 ? 2 : 1}
      />,
    );
  }

  return (
    <div className={`nv-molette${bloque ? ' nv-bloque' : ''}`}>
      <svg
        ref={svgRef}
        viewBox="0 0 200 200"
        role="slider"
        tabIndex={bloque ? -1 : 0}
        aria-label="Cap de l'avion"
        aria-valuemin={0}
        aria-valuemax={359.9}
        aria-valuenow={cap}
        aria-valuetext={formatDeg(cap)}
        aria-disabled={bloque}
        onPointerDown={bas}
        onPointerMove={bouge}
        onPointerUp={haut}
        onPointerCancel={haut}
        onKeyDown={clavier}
      >
        <circle cx={C} cy={C} r={R} fill="#fff" stroke="var(--gris)" strokeWidth="1.5" />
        {graduations}
        {[
          ['N', 0],
          ['E', 90],
          ['S', 180],
          ['O', 270],
        ].map(([t, d]) => (
          <text
            key={t}
            x={r2(C + (R - 24) * Math.sin((d * Math.PI) / 180))}
            y={r2(C - (R - 24) * Math.cos((d * Math.PI) / 180) + 5)}
            textAnchor="middle"
            fontSize="14"
            fill="var(--gris)"
          >
            {t}
          </text>
        ))}
        <line x1={C} y1={C} x2={r2(C + (R - 4) * Math.sin(a))} y2={r2(C - (R - 4) * Math.cos(a))} stroke="var(--orange)" strokeWidth="4" strokeLinecap="round" />
        <circle cx={C} cy={C} r="6" fill="var(--orange)" />
      </svg>
      <div className="nv-cap" aria-live="polite">
        Cap <b>{formatDeg(cap)}</b>
      </div>
      <div className="nv-fin">
        {[
          ['−1°', -1],
          ['−0,1°', -0.1],
          ['+0,1°', 0.1],
          ['+1°', 1],
        ].map(([t, d]) => (
          <button key={t} type="button" disabled={bloque} onClick={() => onChange(norm(cap + d))}>
            {t}
          </button>
        ))}
      </div>
    </div>
  );
}
