// Fig. 20.1 : s = 16 t² (feet, seconds), A at t0 = 5 s. The slider moves B (Δt): the secant tends to the tangent T (slope 160 ft/s).
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const X0 = 186, Y0 = 461, SX = 42, SY = 0.2575; // px per second, px per foot (measured on the book figure)
const T0 = 5, DT0 = 3.74, K = 16; // text: s = 16 t², t0 = 5 s; Δt of the book figure measured on the drawing
const px = (t) => X0 + SX * t, py = (s) => Y0 - SY * s, s = (t) => K * t * t;
const dot = { stroke: COL.grey, 'stroke-width': 4, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' };

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 20.1. Distance s parcourue par une bille qui tombe en fonction du temps t, s = 16 t². Le point A est à l’instant t0 = 5 s. La sécante AB en rouge a pour pente la vitesse moyenne Δs/Δt ; quand Δt diminue, B glisse vers A et la sécante tourne jusqu’à la tangente T en vert pointillé.');
  const fix = add(root, 'g');
  arrow(fix, [186, 520], [186, 40], { w: 5, h: 28 });
  arrow(fix, [168, Y0], [705, Y0], { w: 5, h: 28 });
  txt(fix, 30, 36, ['s', { t: ' (distance)', it: false }], { size: 34 });
  txt(fix, 522, 418, ['t', { t: ' (temps)', it: false }], { size: 34 });
  const pts = [];
  for (let i = 0; i <= 120; i++) { const t = (10.05 * i) / 120; pts.push([px(t), py(s(t))]); }
  poly(fix, pts, { stroke: COL.blue, 'stroke-width': 8, 'stroke-linecap': 'round' });
  const xa = px(T0), ya = py(s(T0)), m = ((2 * K * T0) * SY) / SX;
  add(fix, 'line', { x1: 273, y1: ya + m * (xa - 273), x2: 648, y2: ya - m * (648 - xa), stroke: COL.green, 'stroke-width': 6, 'stroke-dasharray': '16 9' });
  txt(fix, 660, 135, 'T', { size: 46, fill: COL.green });
  add(fix, 'line', { x1: xa, y1: ya, x2: xa, y2: Y0, ...dot });
  add(fix, 'circle', { cx: xa, cy: ya, r: 12, fill: '#000' });
  txt(fix, xa - 44, ya - 38, 'A', { size: 50 });
  txt(fix, xa - 14, 512, ['t', { t: '0', sub: true }], { size: 44 });
  const dyn = add(root, 'g');

  const draw = (dt) => {
    clear(dyn);
    const tb = T0 + dt, ds = s(tb) - s(T0), sl = ds / dt, xb = px(tb), yb = py(s(tb)), k = (sl * SY) / SX;
    const x1 = xa - 88, x2 = Math.min(xb + 54, 640);
    add(dyn, 'line', { x1, y1: ya + k * (xa - x1), x2, y2: ya - k * (x2 - xa), stroke: COL.red, 'stroke-width': 6 });
    add(dyn, 'polyline', { points: `${xa},${ya} ${xb},${ya} ${xb},${yb}`, fill: 'none', ...dot });
    add(dyn, 'circle', { cx: xb, cy: yb, r: 12, fill: '#000' });
    const near = dt < 2;
    txt(dyn, xb - 52, near ? yb - 62 : yb - 22, 'B', { size: 50 });
    txt(dyn, xb + 18, (ya + yb) / 2 + 15, [{ t: 'Δ', it: false }, 's'], { size: 44 });
    txt(dyn, xa + Math.max(14, (xb - xa) / 2 - 20), ya + 46, [{ t: 'Δ', it: false }, 't'], { size: 44 });
    readout(dyn, [`s = 16 t²   t0 = ${T0} s   s(t0) = ${fr(s(T0), 0)} pieds`, `Δt = ${fr(dt, 2)} s   Δs = ${fr(ds, 1)} pieds   Δs/Δt = ${fr(sl, 1)} pieds/s`, `tangente T : ${fr(2 * K * T0, 0)} pieds/s`], 570, 24);
  };
  const inp = slider(el, { label: 'Δt, écart de B à A', min: 0.5, max: 5, step: 0.01, value: DT0, unit: 's', onInput: draw });
  resetButton(el, () => { inp.value = DT0; inp.dispatchEvent(new Event('input')); });
}
