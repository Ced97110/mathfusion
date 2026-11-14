// Fig. 21.1 : the same point P seen in axes (x, y) and in axes (x', y') turned by theta. The slider turns the primed axes.
import { svg, add, clear, slider, resetButton, } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const TH0 = (Math.acos(0.96) * 180) / Math.PI; // text: cos theta = 0.96, sin theta = 0.28 (about 16.3 degrees)
const O = [268, 443], L = 362, UNIT = 61.2; // px: origin and axis length measured on the book figure; px per unit chosen so |OP| matches the book drawing
const PX = 4 * UNIT, PY = 3 * UNIT, P = [O[0] + PX, O[1] - PY], S5 = 1 / UNIT; // the text gives P = (4 ; 3), |OP| = 5

export function mount(el) {
  const root = svg(el, 760, 720, 'Figure 21.1. Un point P vu dans deux repères de même origine O. Les axes x′, y′ sont tournés de l’angle θ par rapport aux axes x, y. Les coordonnées de P changent, mais la flèche r de O à P reste la même.');
  const fix = add(root, 'g');
  arrow(fix, [O[0], 445], [638, 445], { w: 6, h: 26 });
  arrow(fix, [O[0], 445], [O[0], 82], { w: 6, h: 26 });
  add(fix, 'line', { x1: O[0], y1: P[1], x2: P[0], y2: P[1], stroke: '#000', 'stroke-width': 5, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' });
  add(fix, 'line', { x1: P[0], y1: P[1], x2: P[0], y2: 445, stroke: '#000', 'stroke-width': 5, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' });
  arrow(fix, O, [P[0] - 8, P[1] + 8], { c: COL.blue, w: 10, h: 30 });
  add(fix, 'circle', { cx: P[0], cy: P[1], r: 11, fill: '#000' });
  txt(fix, 246, 22 + 20, 'y', { size: 52 });
  txt(fix, 655, 462, 'x', { size: 52 });
  txt(fix, 235, 492, 'O', { size: 52 });
  txt(fix, 510, 230, 'P', { size: 52 });
  txt(fix, 220, 252, 'y', { size: 46 });
  txt(fix, 481, 495, 'x', { size: 46 });
  txt(fix, 354, 322, 'r', { size: 52, fill: COL.blue });
  arrow(fix, [354, 273], [382, 273], { c: COL.blue, w: 4, h: 12 });
  const dyn = add(root, 'g');
  const draw = (deg) => {
    clear(dyn);
    const th = (deg * Math.PI) / 180, c = Math.cos(th), s = Math.sin(th);
    const u = [c, -s], v = [-s, -c], at = (d, k) => [O[0] + k * d[0], O[1] + k * d[1]];
    const xp = PX * c + PY * s, yp = PY * c - PX * s;
    const tx = at(u, L), ty = at(v, L), foot = at(u, xp);
    arrow(dyn, O, tx, { c: COL.red, w: 6, h: 26 });
    arrow(dyn, O, ty, { c: COL.red, w: 6, h: 26 });
    add(dyn, 'line', { x1: P[0], y1: P[1], x2: foot[0], y2: foot[1], stroke: COL.red, 'stroke-width': 5, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' });
    const arc = []; for (let i = 0; i <= 30; i++) { const a = (th * i) / 30; arc.push([O[0] + 95 * Math.cos(a), O[1] - 95 * Math.sin(a)]); }
    poly(dyn, arc, { stroke: COL.green, 'stroke-width': 6 });
    txt(dyn, O[0] + 125 * Math.cos(th / 2) - 6, O[1] - 125 * Math.sin(th / 2) + 14, 'θ', { size: 48, fill: COL.green });
    txt(dyn, tx[0] + 23, tx[1] - 5, [{ t: 'x' }, { t: '′', it: false }], { size: 52, fill: COL.red });
    txt(dyn, Math.max(10, ty[0] - 62), ty[1] - (ty[0] - 62 < 10 ? 28 : 5), [{ t: 'y' }, { t: '′', it: false }], { size: 52, fill: COL.red });
    txt(dyn, foot[0] + 27, foot[1] + 25, [{ t: 'x' }, { t: '′', it: false }], { size: 40, fill: COL.red });
    readout(dyn, [`θ = ${fr(deg, 1)}°   cos θ = ${fr(c)}   sin θ = ${fr(s)}`, `x = ${fr(PX * S5)}   y = ${fr(PY * S5)}   (|OP| = 5)`, `x′ = x cos θ + y sin θ = ${fr(xp * S5)}`, `y′ = y cos θ − x sin θ = ${fr(yp * S5)}`, `x′² + y′² = ${fr((xp * xp + yp * yp) * S5 * S5, 1)}  (inchangé)`], 540, 26);
  };
  const inp = slider(el, { label: 'Angle θ', min: 0, max: 30, step: 0.1, value: TH0, unit: '°', onInput: draw });
  resetButton(el, () => { inp.value = TH0; inp.dispatchEvent(new Event('input')); });
}
