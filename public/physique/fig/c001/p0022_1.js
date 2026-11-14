// Fig. 1.1 : number line. Blue arrow = start at 0 and move by a; red arrow = then move by b. Result a + b.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout } from '../kit.js';

const A0 = 3, B0 = -5; // book: 0 + 3 = 3, then 3 - 5 = -2
const X0 = 368, U = 48.9; // px of 0 ; px per unit (measured on the book figure)
const X = (v) => X0 + U * v;
const sg = (v) => (v < 0 ? '−' : '') + Math.abs(v);

export function mount(el) {
  const root = svg(el, 760, 620, 'Figure 1.1. La droite des nombres, de −6 à 6, avec le zéro O au milieu. Une flèche bleue part de 0 et avance de a ; une flèche rouge part de là et recule de b. Le point rouge est le résultat a + b.');
  const fix = add(root, 'g');
  arrow(fix, [47, 237], [683, 237], { w: 6, h: 24 });
  for (let v = -6; v <= 6; v++) add(fix, 'line', { x1: X(v), y1: 224, x2: X(v), y2: 250, stroke: '#000', 'stroke-width': 5 });
  txt(fix, 47, 45, 'négatifs', { size: 40, fill: COL.grey, it: false });
  txt(fix, 682, 45, 'positifs', { size: 40, fill: COL.grey, it: false, anchor: 'end' });
  txt(fix, 333, 195, 'O', { size: 50 });
  add(fix, 'circle', { cx: X0, cy: 237, r: 12, fill: '#000' });
  const dyn = add(root, 'g');
  let a = A0, b = B0;
  const draw = () => {
    clear(dyn);
    const r = a + b;
    const labels = new Set([-6, -4, -2, 0, 2, 4, 6, a, r]);
    for (const v of labels) txt(dyn, X(v), 318, String(v).replace('-', '-'), { size: 42, anchor: 'middle', it: false });
    arrow(dyn, [X0 + 4, 150], [X(a) - 11, 150], { c: COL.blue, w: 7, h: 24 });
    txt(dyn, (X0 + X(a)) / 2 + 2, 100, '+' + a, { size: 46, fill: COL.blue, anchor: 'middle', it: false });
    add(dyn, 'circle', { cx: X(a), cy: 237, r: 12, fill: COL.blue });
    arrow(dyn, [X(a) - 4, 360], [X(r) + 12, 360], { c: COL.red, w: 7, h: 24 });
    txt(dyn, (X(a) + X(r)) / 2, 408, sg(b), { size: 46, fill: COL.red, anchor: 'middle', it: false });
    add(dyn, 'circle', { cx: X(r), cy: 237, r: 12, fill: COL.red });
    readout(dyn, [`0 + ${a} = ${a}`, `${a} ${b < 0 ? '−' : '+'} ${Math.abs(b)} = ${sg(r)}`], 500, 30);
  };
  const ia = slider(el, { label: 'Avancer de a', min: 1, max: 6, step: 1, value: A0, onInput: (v) => { a = v; draw(); } });
  const ib = slider(el, { label: 'Puis ajouter b', min: -6, max: -1, step: 1, value: B0, format: (v) => sg(v), onInput: (v) => { b = v; draw(); } });
  resetButton(el, () => { for (const [i, v] of [[ia, A0], [ib, B0]]) { i.value = v; i.dispatchEvent(new Event('input')); } });
}
