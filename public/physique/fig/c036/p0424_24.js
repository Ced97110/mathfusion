// Fig. 36.3 : potential-energy bowl Ep = k x^2 / 2, level E, turning points A and B.
// The slider changes the amplitude C (throw harder): E = k C^2 / 2 rises, A and B move apart, T stays.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const K = 8, M = 2, C0 = 0.1; // book: k = 8 N/m, m = 2 kg, C = 0.1 m (E = 0.04 J)
const SX = 2110, SE = 242 / 0.04, OX = 351, OY = 521; // px per m ; px per J
const X = (x) => OX + SX * x, Y = (e) => OY - SE * e;

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 36.3. Courbe en cuvette de l’énergie potentielle Ep en fonction de l’écart x, avec O au fond. Un trait horizontal rouge, l’énergie totale E, coupe la courbe aux points A à gauche et B à droite. Une flèche verte « va-et-vient » relie les deux côtés de la cuvette.');
  const fix = add(root, 'g');
  arrow(fix, [OX, 606], [OX, 48], { w: 5, h: 30 });
  arrow(fix, [35, OY], [706, OY], { w: 5, h: 30 });
  txt(fix, 335, 46, [{ t: 'E' }, { t: 'p', sub: true }], { size: 42 });
  txt(fix, 668, 538, 'x', { size: 42 });
  const pts = [];
  for (let i = 0; i <= 200; i++) { const x = -0.13 + (0.26 * i) / 200; pts.push([X(x), Y(0.5 * K * x * x)]); }
  poly(fix, pts, { stroke: COL.blue, 'stroke-width': 8, 'stroke-linecap': 'round' });
  add(fix, 'circle', { cx: OX, cy: OY, r: 12, fill: '#000' });
  txt(fix, 366, 584, 'O', { size: 54 });
  const dyn = add(root, 'g');

  const draw = (c) => {
    clear(dyn);
    const e = 0.5 * K * c * c, ye = Y(e), r = c * SX;
    add(dyn, 'line', { x1: 65, y1: ye, x2: 637, y2: ye, stroke: COL.red, 'stroke-width': 7 });
    const h = r / Math.SQRT2 + 16;
    arrow(dyn, [OX, Y(e / 2)], [OX - h, Y(e / 2)], { c: COL.green, w: 7, h: 26 });
    arrow(dyn, [OX, Y(e / 2)], [OX + h, Y(e / 2)], { c: COL.green, w: 7, h: 26 });
    txt(dyn, OX + 8, Y(e / 2) - 26, 'va-et-vient', { size: 38, fill: COL.green, anchor: 'middle', it: false });
    for (const s of [-1, 1]) add(dyn, 'circle', { cx: OX + s * r, cy: ye, r: 12, fill: '#000' });
    txt(dyn, OX - r - 28, ye - 36, 'A', { size: 54, anchor: 'middle' });
    txt(dyn, OX + r + 37, ye - 36, 'B', { size: 54, anchor: 'middle' });
    txt(dyn, OX + r + 5, ye - 26, 'E', { size: 42, fill: COL.red, anchor: 'middle' });
    readout(dyn, [`k = ${K} N/m   C = ${fr(c, 3)} m   E = ½ k C² = ${fr(e, 4)} J`, `T = 2π√(m/k) = ${fr(2 * Math.PI * Math.sqrt(M / K))} s  (m = ${M} kg) : ne change pas`], 632);
  };
  const inp = slider(el, { label: 'Lancer (amplitude C)', min: 0.05, max: 0.125, step: 0.005, value: C0, unit: 'm', format: (v) => fr(v, 3), onInput: draw });
  resetButton(el, () => { inp.value = C0; inp.dispatchEvent(new Event('input')); });
}
