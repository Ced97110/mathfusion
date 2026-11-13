// Fig. 1.2 : rectangle of R rows and C columns. R x C squares; the same rectangle gives N / C = R.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout } from '../kit.js';

const R0 = 3, C0 = 4; // book: 3 rows, 4 columns, 12 squares

export function mount(el) {
  const root = svg(el, 760, 620, 'Figure 1.2. Un rectangle de carreaux : R lignes de haut, C colonnes de large. Il contient R × C carreaux. En rangeant ces carreaux sur C colonnes, on retrouve R lignes : N ÷ C = R.');
  const dyn = add(root, 'g');
  let r = R0, c = C0;
  const draw = () => {
    clear(dyn);
    const s = Math.min(90, 360 / c, 270 / r), w = s * c, h = s * r, x0 = 150, y0 = 85, n = r * c;
    add(dyn, 'rect', { x: x0, y: y0, width: w, height: h, fill: '#dce6f5' });
    for (let i = 1; i < c; i++) add(dyn, 'line', { x1: x0 + i * s, y1: y0, x2: x0 + i * s, y2: y0 + h, stroke: COL.blue, 'stroke-width': 5 });
    for (let j = 1; j < r; j++) add(dyn, 'line', { x1: x0, y1: y0 + j * s, x2: x0 + w, y2: y0 + j * s, stroke: COL.blue, 'stroke-width': 5 });
    add(dyn, 'rect', { x: x0, y: y0, width: w, height: h, fill: 'none', stroke: COL.blue, 'stroke-width': 5 });
    txt(dyn, 330, 50, `${r} × ${c} = ${n} carreaux`, { size: 46, fill: COL.blue, anchor: 'middle', it: false });
    arrow(dyn, [119, y0 + h - 8], [119, y0 + 10], { w: 5, h: 20, both: true });
    txt(dyn, 86, y0 + h / 2 + 16, String(r), { size: 46, anchor: 'middle', it: false });
    arrow(dyn, [x0 + 7, y0 + h + 32], [x0 + w - 5, y0 + h + 32], { w: 5, h: 20, both: true });
    txt(dyn, x0 + w / 2, y0 + h + 95, `${c} (largeur)`, { size: 44, anchor: 'middle', it: false });
    arrow(dyn, [565, y0 + h - 5], [565, y0 + 10], { c: COL.red, w: 7, h: 26 });
    txt(dyn, 580, 205, `${n} ÷ ${c}`, { size: 40, fill: COL.red, it: false });
    txt(dyn, 590, 255, `= ${r}`, { size: 40, fill: COL.red, it: false });
    readout(dyn, [`${r} × ${c} = ${n}   et   ${n} ÷ ${c} = ${n / c}`], 520, 30);
  };
  const ir = slider(el, { label: 'Lignes (hauteur)', min: 1, max: 6, step: 1, value: R0, onInput: (v) => { r = v; draw(); } });
  const ic = slider(el, { label: 'Colonnes (largeur)', min: 1, max: 6, step: 1, value: C0, onInput: (v) => { c = v; draw(); } });
  resetButton(el, () => { for (const [i, v] of [[ir, R0], [ic, C0]]) { i.value = v; i.dispatchEvent(new Event('input')); } });
}
