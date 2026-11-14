// Fig. 2.2 : rectangle a x (b + c) cut in two: ab + ac. Sliders change a, b, c.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout } from '../kit.js';

const M = (s) => s.split(/([a-z]+)/).filter(Boolean).map((t) => (/[a-z]/.test(t) ? { t } : { t, it: false }));
const V0 = { a: 3, b: 4, c: 2 }; // book: a = 3, b = 4, c = 2

export function mount(el) {
  const root = svg(el, 760, 620, 'Figure 2.2. Un rectangle de hauteur a et de largeur b + c. Un trait pointillé le coupe en deux : à gauche un rectangle d’aire ab en bleu, à droite un rectangle d’aire ac en rouge. L’aire totale est la somme.');
  const dyn = add(root, 'g');
  const v = { ...V0 };
  const draw = () => {
    clear(dyn);
    const { a, b, c } = v;
    const u = Math.min(73.5, 442 / (b + c), 330 / a), x0 = 185, y0 = 85, h = a * u, wb = b * u, wc = c * u, xm = x0 + wb, yb = y0 + h;
    txt(dyn, 407, 50, M('a(b + c) = ab + ac'), { size: 48, anchor: 'middle' });
    add(dyn, 'rect', { x: x0, y: y0, width: wb, height: h, fill: '#dce6f5', stroke: COL.blue, 'stroke-width': 6 });
    add(dyn, 'rect', { x: xm, y: y0, width: wc, height: h, fill: '#f5dcd9', stroke: COL.red, 'stroke-width': 6 });
    add(dyn, 'line', { x1: xm, y1: y0, x2: xm, y2: yb, stroke: '#000', 'stroke-width': 6, 'stroke-dasharray': '10 10' });
    const mid = y0 + h / 2;
    txt(dyn, x0 + wb / 2, mid + 14, M(`ab = ${a * b}`), { size: Math.min(46, wb / 3.4), fill: COL.blue, anchor: 'middle' });
    const sc = Math.min(44, wc / 2.6);
    txt(dyn, xm + wc / 2, mid - 4, M('ac'), { size: sc, fill: COL.red, anchor: 'middle' });
    txt(dyn, xm + wc / 2, mid - 4 + sc * 1.1, M(`= ${a * c}`), { size: sc, fill: COL.red, anchor: 'middle' });
    arrow(dyn, [155, yb - 8], [155, y0 + 10], { w: 5, h: 20, both: true });
    txt(dyn, 86, mid + 16, M(`a = ${a}`), { size: 44, anchor: 'middle' });
    arrow(dyn, [x0 + 8, yb + 30], [xm - 8, yb + 30], { w: 5, h: 20, both: true });
    arrow(dyn, [xm + 8, yb + 30], [xm + wc - 6, yb + 30], { w: 5, h: 20, both: true });
    txt(dyn, x0 + wb / 2, yb + 82, M(`b = ${b}`), { size: 44, anchor: 'middle' });
    txt(dyn, xm + wc / 2, yb + 82, M(`c = ${c}`), { size: 44, anchor: 'middle' });
    readout(dyn, [`a(b + c) = ${a} × ${b + c} = ${a * (b + c)}`, `ab + ac = ${a * b} + ${a * c} = ${a * b + a * c}`], 540, 30);
  };
  const ins = Object.keys(V0).map((k) => {
    const [min, max] = { a: [1, 5], b: [2, 6], c: [1, 4] }[k];
    return slider(el, { label: `${k} =`, min, max, step: 1, value: V0[k], onInput: (x) => { v[k] = x; draw(); } });
  });
  resetButton(el, () => ins.forEach((i, n) => { i.value = Object.values(V0)[n]; i.dispatchEvent(new Event('input')); }));
}
