// Fig. 10.2 : y = 20 t − 5 t². Tangents at P, S (top, t = 2 s) and Q; slope = 20 − 10 t. Two sliders move P and Q.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const X0 = 101, Y0 = 413, SX = 137, SY = 15.9; // px per second, px per metre (measured on the book figure)
const TP0 = 0.7, TQ0 = 3.3, TS = 2; // P and Q read on the book figure: symmetric around the top
const y = (t) => 20 * t - 5 * t * t, slope = (t) => 20 - 10 * t;
const px = (t) => X0 + SX * t, py = (v) => Y0 - SY * v;
const sign = (m) => (Math.abs(m) < 1e-9 ? '= 0' : m > 0 ? '> 0' : '< 0');

export function mount(el) {
  const root = svg(el, 760, 610, 'Figure 10.2. Hauteur y = 20t − 5t² d’une balle lancée vers le haut. En P la tangente monte (pente positive), en S, au sommet à t = 2 s, elle est horizontale (pente nulle), en Q elle descend (pente négative).');
  const fix = add(root, 'g');
  add(fix, 'line', { x1: 101, y1: 0, x2: 101, y2: 445, stroke: '#000', 'stroke-width': 5 });
  arrow(fix, [100, Y0], [705, Y0], { w: 5, h: 28 });
  txt(fix, 622, 436, ['t', { t: ' (s)', it: false }], { size: 38 });
  const pts = [];
  for (let i = 0; i <= 120; i++) { const t = (4 * i) / 120; pts.push([px(t), py(y(t))]); }
  poly(fix, pts, { stroke: COL.blue, 'stroke-width': 8, 'stroke-linecap': 'round' });
  const dyn = add(root, 'g');

  let tp = TP0, tq = TQ0;
  const draw = () => {
    clear(dyn);
    const one = (t, name, ox, oy, lx, ly) => {
      const m = slope(t), x = px(t), yy = py(y(t)), k = (m * SY) / SX;
      add(dyn, 'line', { x1: x - 78, y1: yy + k * 78, x2: x + 78, y2: yy - k * 78, stroke: COL.red, 'stroke-width': 7 });
      add(dyn, 'circle', { cx: x, cy: yy, r: 11, fill: '#000' });
      txt(dyn, x + ox, yy + oy, name, { size: 56 });
      txt(dyn, x + lx, yy + ly, `pente ${sign(m)}`, { size: 38, fill: COL.red, it: false });
    };
    one(tp, 'P', -62, -20, -89, 151);
    one(TS, 'S', -15, -25, -95, -68);
    one(tq, 'Q', 16, -20, -46, -134);
    readout(dyn, [tp, TS, tq].map((t, i) => `${'PSQ'[i]} : t = ${fr(t, 1)} s   pente = 20 − 10 × ${fr(t, 1)} = ${fr(slope(t), 1)} m/s`), 490, 24);
  };
  const a = slider(el, { label: 'Instant de P, avant le sommet', min: 0.1, max: 1.9, step: 0.1, value: TP0, unit: 's', onInput: (v) => { tp = v; draw(); } });
  const b = slider(el, { label: 'Instant de Q, après le sommet', min: 2.1, max: 3.9, step: 0.1, value: TQ0, unit: 's', onInput: (v) => { tq = v; draw(); } });
  resetButton(el, () => { a.value = TP0; b.value = TQ0; a.dispatchEvent(new Event('input')); b.dispatchEvent(new Event('input')); });
}
