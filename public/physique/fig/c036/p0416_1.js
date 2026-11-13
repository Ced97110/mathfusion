// Fig. 36.1 : spring + mass, and the curve x(t). The slider changes the mass m: the period T changes.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const K = 8, M0 = 2, C = 0.1; // book: k = 8 N/m, m = 2 kg, C = 0.1 m
const PX = 167 / Math.PI, X0 = 300, Y0 = 331, AMP = 2000 * C; // px per second ; px for C
const TMAX = (668 - X0) / PX;

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 36.1. À gauche, un ressort accroché en haut porte une masse m écartée de x vers le bas par rapport au repos O ; la flèche rouge F pointe vers O. À droite, la courbe de x en fonction du temps t : période T, amplitude C, pente maximale quand la courbe passe par zéro.');
  const fix = add(root, 'g');
  add(fix, 'line', { x1: 75, y1: 69, x2: 225, y2: 69, stroke: '#000', 'stroke-width': 9 });
  const spring = [];
  for (let i = 0; i <= 160; i++) { const s = i / 160; spring.push([150 + 30 * Math.cos(2 * Math.PI * 8 * s + 0.4), 72 + 225 * s]); }
  poly(fix, spring, { stroke: COL.grey, 'stroke-width': 6, 'stroke-linejoin': 'round' });
  add(fix, 'rect', { x: 113, y: 295, width: 74, height: 90, fill: COL.blue });
  add(fix, 'line', { x1: 45, y1: 226, x2: 255, y2: 226, stroke: COL.grey, 'stroke-width': 4, 'stroke-dasharray': '14 9' });
  txt(fix, 38, 208, 'O', { size: 50 });
  txt(fix, 36, 295, 'F', { size: 50, fill: COL.red });
  arrow(fix, [85, 335], [85, 237], { c: COL.red, w: 7, h: 26 });
  arrow(fix, [238, 230], [238, 332], { w: 5, h: 22 });
  txt(fix, 246, 285, 'x', { size: 50 });
  txt(fix, 196, 348, 'm', { size: 50 });
  arrow(fix, [300, 553], [300, 38], { w: 5, h: 26 });
  arrow(fix, [290, Y0], [706, Y0], { w: 5, h: 26 });
  txt(fix, 306, 40, 'x', { size: 36 });
  txt(fix, 682, 352, 't', { size: 44 });
  const dyn = add(root, 'g');

  const draw = (m) => {
    clear(dyn);
    const w = Math.sqrt(K / m), T = (2 * Math.PI) / w;
    const pts = [];
    for (let i = 0; i <= 300; i++) { const t = (TMAX * i) / 300; pts.push([X0 + PX * t, Y0 - AMP * Math.cos(w * t)]); }
    poly(dyn, pts, { stroke: COL.blue, 'stroke-width': 8, 'stroke-linecap': 'round' });
    const tx = X0 + (PX * T) / 4, slope = (AMP * w) / PX, dx = 215 / slope;
    add(dyn, 'line', { x1: tx - dx, y1: Y0 - 215, x2: tx + dx, y2: Y0 + 215, stroke: COL.red, 'stroke-width': 5, 'stroke-dasharray': '14 8' });
    add(dyn, 'circle', { cx: tx, cy: Y0, r: 10, fill: COL.red });
    arrow(dyn, [X0 + 5, 92], [X0 + PX * T - 5, 92], { w: 5, h: 20, both: true });
    txt(dyn, X0 + (PX * T) / 2 - 12, 74, 'T', { size: 44 });
    txt(dyn, 386, 112, 'pente', { size: 30, fill: COL.red, it: false });
    txt(dyn, 386, 150, 'max.', { size: 30, fill: COL.red, it: false });
    add(dyn, 'line', { x1: X0 + PX * T, y1: Y0 + 8, x2: X0 + PX * T, y2: Y0 + AMP - 6, stroke: '#000', 'stroke-width': 6, 'stroke-dasharray': '1 12', 'stroke-linecap': 'round' });
    txt(dyn, X0 + PX * T + 12, Y0 + AMP + 4, 'C', { size: 44 });
    readout(dyn, [`k = ${K} N/m   m = ${fr(m, 1)} kg   C = ${fr(C, 1)} m`, `ω₀ = √(k/m) = ${fr(w)} rad/s   T = 2π/ω₀ = ${fr(T)} s`], 612);
  };
  const inp = slider(el, { label: 'Masse m', min: 1, max: 4, step: 0.1, value: M0, unit: 'kg', onInput: draw });
  resetButton(el, () => { inp.value = M0; inp.dispatchEvent(new Event('input')); });
}
