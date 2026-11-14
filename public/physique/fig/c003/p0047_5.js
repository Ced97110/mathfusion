// Fig. 3.2 : price 3 + 2d (blue) against the price paid (red). The slider changes the price paid; S moves, d = (paid - 3) / 2.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout } from '../kit.js';

const P0 = 25; // book: 25 euros paid, d = 11 km
const OX = 130, OY = 500.5, PXK = 354 / 11, PXE = 11.32; // px measured on the book figure: origin, px per km, px per euro
const X = (d) => OX + PXK * d, Y = (p) => OY - PXE * p;
const fr0 = (v) => String(+v.toFixed(1)).replace('.', ',');

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 3.2. Graphique du prix en euros selon la distance d en km. La ligne bleue est le prix 3 + 2d, qui part de 3. La ligne rouge est le prix payé, horizontale. Elles se croisent au point S ; sous S, l’axe des distances donne d.');
  const fix = add(root, 'g');
  arrow(fix, [OX, 535], [OX, 36], { w: 6, h: 26 });
  arrow(fix, [113, 500], [706, 500], { w: 6, h: 26 });
  txt(fix, 33, 42, 'prix (€)', { size: 34, it: false });
  txt(fix, 565, 548, [{ t: 'd' }, { t: ' (km)', it: false }], { size: 38 });
  txt(fix, 70, 467 + 14, '3', { size: 42, it: false, anchor: 'middle' });
  add(fix, 'line', { x1: OX, y1: Y(3), x2: X(16.1), y2: Y(3 + 2 * 16.1), stroke: COL.blue, 'stroke-width': 8 });
  txt(fix, 535, 365, [{ t: '3 + 2', it: false }, { t: 'd' }], { size: 42, fill: COL.blue });
  const dyn = add(root, 'g');
  const draw = (p) => {
    clear(dyn);
    const d = (p - 3) / 2, sx = X(d), sy = Y(p);
    add(dyn, 'line', { x1: OX, y1: sy, x2: 663, y2: sy, stroke: COL.red, 'stroke-width': 7 });
    txt(dyn, 163, sy - 38, `${fr0(p)} (payé)`, { size: 40, fill: COL.red, it: false });
    add(dyn, 'line', { x1: sx, y1: sy + 12, x2: sx, y2: 500, stroke: '#000', 'stroke-width': 5, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' });
    add(dyn, 'circle', { cx: sx, cy: sy, r: 11, fill: '#000' });
    txt(dyn, sx + 22, sy - 28, 'S', { size: 50 });
    txt(dyn, sx, 548, fr0(d), { size: 42, it: false, anchor: 'middle' });
    readout(dyn, [`3 + 2d = ${fr0(p)}  →  2d = ${fr0(p)} − 3 = ${fr0(p - 3)}`, `d = ${fr0(p - 3)} ÷ 2 = ${fr0(d)} km`], 630, 30);
  };
  const inp = slider(el, { label: 'Prix payé', min: 13, max: 28, step: 1, value: P0, unit: '€', onInput: draw });
  resetButton(el, () => { inp.value = P0; inp.dispatchEvent(new Event('input')); });
}
