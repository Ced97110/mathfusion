// Fig. 13.1 : slope field of y' = -y / tau and the solution from y0. Sliders change y0 and tau (relative to the book figure).
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, fr, poly } from '../kit.js';

const OX = 47, OY = 612, TAU = 200, H0 = 427, XEND = 650; // px measured on the book figure: origin, tau, start height, end of curve
const COLS = Array.from({ length: 10 }, (_, k) => 68 + 60 * k), ROWS = Array.from({ length: 7 }, (_, j) => 35.4 + 70.8 * j);
const HALF = 23; // half the horizontal extent of a slope mark, measured

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 13.1. Champ de pentes de y point = −y/τ : en chaque point, un petit trait gris donne la pente de la courbe qui passe par là. Plus y est grand, plus la pente est raide vers le bas. La courbe bleue part de y0 et suit les traits : c’est la solution.');
  const fix = add(root, 'g');
  arrow(fix, [OX, 610], [OX, 40], { w: 6, h: 26 });
  arrow(fix, [OX - 2, OY - 0], [703, OY], { w: 6, h: 26 });
  txt(fix, 50, 32, 'y', { size: 36 });
  txt(fix, 500, 596, [{ t: 't' }, { t: ' (min)', it: false }], { size: 38 });
  txt(fix, 390, 400, 'solution', { size: 42, fill: COL.blue, it: false });
  const dyn = add(root, 'g');
  const draw = (r0, rt) => {
    clear(dyn);
    const tau = TAU * rt, h0 = H0 * r0;
    for (const x of COLS) for (const h of ROWS) {
      const m = -h / tau;
      add(dyn, 'line', { x1: x - HALF, y1: OY - h + m * HALF, x2: x + HALF, y2: OY - h - m * HALF, stroke: COL.grey, 'stroke-width': 3.5 });
    }
    const pts = [];
    for (let i = 0; i <= 100; i++) { const x = OX + ((XEND - OX) * i) / 100; pts.push([x, OY - h0 * Math.exp(-(x - OX) / tau)]); }
    poly(dyn, pts, { stroke: COL.blue, 'stroke-width': 8, 'stroke-linecap': 'round' });
    add(dyn, 'circle', { cx: OX, cy: OY - h0, r: 11, fill: '#000' });
    txt(dyn, 68, OY - h0 - 25, [{ t: 'y' }, { t: '0', sub: true }], { size: 54 });
  };
  let r0 = 1, rt = 1;
  const i0 = slider(el, { label: 'Départ y₀ (× livre)', min: 0.4, max: 1.1, step: 0.1, value: 1, format: (v) => '×' + fr(v, 1), onInput: (v) => { r0 = v; draw(r0, rt); } });
  const it = slider(el, { label: 'Temps τ (× livre)', min: 0.5, max: 2, step: 0.25, value: 1, format: (v) => '×' + fr(v, 2), onInput: (v) => { rt = v; draw(r0, rt); } });
  resetButton(el, () => { for (const i of [i0, it]) { i.value = 1; i.dispatchEvent(new Event('input')); } });
}
