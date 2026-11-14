// Fig. 4.1 : F against x for a spring, F/x = k everywhere. The slider changes k; the three points stay on one straight line.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout } from '../kit.js';

const K0 = 8; // book: F/x = 8 N/m
const OX = 104, OY = 540, PXM = 1390, PXN = 143; // px measured on the book figure: origin, px per m, px per N
const X = (x) => OX + PXM * x, Y = (f) => OY - PXN * f;
const f1 = (v) => String(+v.toFixed(2));
const PTS = [['A', 0.1], ['B', 0.2], ['C', 0.3]];

export function mount(el) {
  const root = svg(el, 760, 740, 'Figure 4.1. Graphique de la force F en newtons selon l’allongement x en mètres : une droite qui part de O. Trois points A, B, C sur la droite ont tous le même rapport F sur x, égal à k.');
  const fix = add(root, 'g');
  arrow(fix, [OX, 585], [OX, 40], { w: 6, h: 26 });
  arrow(fix, [75, OY], [703, OY], { w: 6, h: 26 });
  txt(fix, 43, 42, [{ t: 'F' }, { t: ' (N)', it: false }], { size: 36 });
  txt(fix, 576, 588, [{ t: 'x' }, { t: ' (m)', it: false }], { size: 40 });
  txt(fix, 42, 520, 'O', { size: 52 });
  add(fix, 'circle', { cx: OX, cy: OY, r: 11, fill: '#000' });
  for (const [, x] of PTS) txt(fix, X(x), 603, f1(x), { size: 36, it: false, anchor: 'middle' });
  const dyn = add(root, 'g');
  const draw = (k) => {
    clear(dyn);
    const xe = Math.min(0.362, (OY - 45) / (PXN * k));
    txt(dyn, 160, 122, [{ t: 'F/x' }, { t: ' = ' + f1(k) + ' partout', it: false }], { size: 40, fill: COL.blue });
    add(dyn, 'line', { x1: OX, y1: OY, x2: X(xe), y2: Y(k * xe), stroke: COL.blue, 'stroke-width': 8, 'stroke-linecap': 'round' });
    for (const [name, x] of PTS) {
      const f = k * x;
      add(dyn, 'line', { x1: OX, y1: Y(f), x2: X(x), y2: Y(f), stroke: COL.grey, 'stroke-width': 3.5, 'stroke-dasharray': '3 6' });
      add(dyn, 'line', { x1: X(x), y1: Y(f), x2: X(x), y2: OY, stroke: COL.grey, 'stroke-width': 3.5, 'stroke-dasharray': '3 6' });
      txt(dyn, 90, Y(f) + 13, f1(f), { size: 36, it: false, anchor: 'end' });
      add(dyn, 'circle', { cx: X(x), cy: Y(f), r: 11, fill: COL.red });
      txt(dyn, X(x) + 22, Y(f) + 58, name, { size: 50, fill: COL.red });
    }
    readout(dyn, PTS.map(([n, x]) => `${n} : F/x = ${f1(k * x)} ÷ ${f1(x)} = ${f1(k)} N/m`), 640, 24);
  };
  const inp = slider(el, { label: 'Rapport k = F/x', min: 4, max: 10, step: 0.5, value: K0, unit: 'N/m', onInput: draw });
  resetButton(el, () => { inp.value = K0; inp.dispatchEvent(new Event('input')); });
}
