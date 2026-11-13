// Fig. 13.2 : step-by-step (Euler) method for y' = -0.2 y, start 60, against the exact 60 exp(-t/5). The slider changes the step.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, readout, fr, poly } from '../kit.js';

const DT0 = 1, K = 0.2, Y0 = 60, TEND = 6; // book: step 1 min, y' = -0.2 y, start 60
const OX = 140, OY = 482, PXT = 89.8, PXY = 6.75; // px measured on the book figure: origin, px per min, px per degree
const X = (t) => OX + PXT * t, Y = (y) => OY - PXY * y;
const exact = (t) => Y0 * Math.exp(-K * t);

export function mount(el) {
  const root = svg(el, 760, 740, 'Figure 13.2. Écart de température y en degrés selon le temps t en minutes. La courbe bleue est la solution exacte 60 e puissance −t/5. La ligne brisée rouge est la méthode pas à pas : à chaque pas, on garde la pente du début du pas. Elle descend plus vite que la courbe ; des pas plus courts la rapprochent.');
  const fix = add(root, 'g');
  add(fix, 'line', { x1: OX, y1: 10, x2: OX, y2: OY, stroke: '#000', 'stroke-width': 4 });
  add(fix, 'line', { x1: OX - 2, y1: OY, x2: 705, y2: OY, stroke: '#000', 'stroke-width': 4 });
  for (const y of [0, 20, 40, 60]) {
    add(fix, 'line', { x1: OX - 10, y1: Y(y), x2: OX, y2: Y(y), stroke: '#000', 'stroke-width': 3 });
    txt(fix, OX - 20, Y(y) + 12, String(y), { size: 34, anchor: 'end', it: false });
  }
  for (let t = 0; t <= 6; t++) {
    add(fix, 'line', { x1: X(t), y1: OY, x2: X(t), y2: OY + 10, stroke: '#000', 'stroke-width': 3 });
    txt(fix, X(t), OY + 44, String(t), { size: 34, anchor: 'middle', it: false });
  }
  txt(fix, 423, 570, [{ t: 't' }, { t: ' (minutes)', it: false }], { size: 34, anchor: 'middle' });
  const yl = txt(fix, 50, 245, [{ t: 'y' }, { t: ' (écart, °C)', it: false }], { size: 34, anchor: 'middle' });
  yl.setAttribute('transform', 'rotate(-90 50 245)');
  const pts = [];
  for (let i = 0; i <= 120; i++) { const t = (TEND * i) / 120; pts.push([X(t), Y(exact(t))]); }
  poly(fix, pts, { stroke: COL.blue, 'stroke-width': 7 });
  txt(fix, 428, 178, 'exacte', { size: 36, fill: COL.blue, it: false });
  txt(fix, 500, 415, 'pas à pas', { size: 36, fill: COL.red, it: false });
  txt(fix, 155, 57, '60', { size: 34, it: false });
  const dyn = add(root, 'g');
  const draw = (dt) => {
    clear(dyn);
    const n = Math.round(TEND / dt), ys = [Y0];
    for (let i = 0; i < n; i++) ys.push(ys[i] - K * ys[i] * dt);
    poly(dyn, ys.map((y, i) => [X(i * dt), Y(y)]), { stroke: COL.red, 'stroke-width': 6, 'stroke-linejoin': 'round' });
    ys.forEach((y, i) => {
      add(dyn, 'circle', { cx: X(i * dt), cy: Y(y), r: 9, fill: COL.red });
      const t = i * dt;
      if (i > 0 && dt >= 1 && t <= 3) txt(dyn, X(t) - 40, Y(y) + 46, fr(y, 1), { size: 32, fill: COL.red, anchor: 'middle', it: false });
    });
    const yn = ys[n], ye = exact(TEND);
    readout(dyn, [`Pas Δt = ${fr(dt)} min : y suivant = y − ${fr(K)} × y × Δt`, `à t = ${TEND} min : pas à pas ${fr(yn, 1)} °C, exacte ${fr(ye, 1)} °C`, `écart = ${fr(yn - ye, 1)} °C`], 622, 26);
  };
  const inp = slider(el, { label: 'Pas Δt', min: 0.5, max: 2, step: 0.5, value: DT0, unit: 'min', onInput: draw });
  resetButton(el, () => { inp.value = DT0; inp.dispatchEvent(new Event('input')); });
}
