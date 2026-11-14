// Fig. 27.2 : effective potential Ep,e(r) and four energies. The slider moves E2 (negative, bound): rmin and rmax move; at the bottom it is the circle E1.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, poly } from '../kit.js';

// curve of the book figure, sampled from the drawing (px)
const C = [[118,132],[118,160],[120,188],[120,216],[121,230],[122,258],[124,286],[126,314],[128,342],[130,370],[132,398],[134,412],[137,426],[139,440],[142,454],[145,468],[150,482],[160,496],[174,502],[193,496],[207,488],[221,480],[235,474],[249,466],[263,458],[277,451],[291,444],[305,438],[319,433],[333,428],[347,423],[361,418],[375,414],[389,412],[403,408],[417,404],[431,400],[445,398],[459,395],[473,392],[487,390],[501,388],[515,386],[529,384],[543,382],[557,380],[571,378],[585,376],[599,374],[613,373],[627,372],[641,370],[655,368]];
const YMIN = 502, Y0 = 310, E0 = (YMIN - 406) / (YMIN - Y0); // E2 of the book: line at y = 406
const cross = (y) => { const r = []; for (let i = 0; i < C.length - 1; i++) { const [x0, y0] = C[i], [x1, y1] = C[i + 1]; if ((y0 - y) * (y1 - y) <= 0 && y0 !== y1) r.push(x0 + ((y - y0) / (y1 - y0)) * (x1 - x0)); } return r; };
const dot = { stroke: COL.grey, 'stroke-width': 4, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' };

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 27.2. Énergie potentielle effective en fonction de la distance r. Quatre énergies : E1 au fond du creux (cercle), E2 négative (ellipse, r oscille entre rmin et rmax), E3 nulle (parabole), E4 positive (hyperbole).');
  const fix = add(root, 'g');
  arrow(fix, [77, 618], [77, 45], { w: 5, h: 30 });
  arrow(fix, [66, Y0], [705, Y0], { w: 5, h: 30 });
  txt(fix, 35, 48, ['E', { t: 'p, e', sub: true }], { size: 40 });
  poly(fix, C, { stroke: COL.blue, 'stroke-width': 9, 'stroke-linejoin': 'round' });
  add(fix, 'line', { x1: 120, y1: 223, x2: 674, y2: 223, stroke: '#6c3483', 'stroke-width': 8 });
  txt(fix, 613, 205, ['E', { t: '4', sub: true }], { size: 50, fill: '#6c3483' });
  add(fix, 'line', { x1: 125, y1: Y0, x2: 674, y2: Y0, stroke: '#d35400', 'stroke-width': 4 });
  txt(fix, 613, 296, ['E', { t: '3', sub: true }], { size: 50, fill: '#d35400' });
  add(fix, 'line', { x1: 174, y1: 502, x2: 174, y2: 557, ...dot });
  add(fix, 'circle', { cx: 174, cy: 502, r: 12, fill: COL.red });
  txt(fix, 205, 512, ['E', { t: '1', sub: true }], { size: 50, fill: COL.red });
  txt(fix, 200, 600, ['r', { t: '1', sub: true }], { size: 50 });
  const dyn = add(root, 'g');

  const draw = (e) => {
    clear(dyn);
    const y = YMIN - e * (YMIN - Y0), [rmin, rmax] = cross(y);
    add(dyn, 'line', { x1: rmin, y1: y, x2: rmax, y2: y, stroke: COL.red, 'stroke-width': 8 });
    add(dyn, 'line', { x1: rmin, y1: y, x2: rmin, y2: 555, ...dot });
    add(dyn, 'line', { x1: rmax, y1: y, x2: rmax, y2: 555, ...dot });
    txt(dyn, rmax + 12, y + 40, ['E', { t: '2', sub: true }], { size: 50, fill: COL.red });
    txt(dyn, rmin - 42, 600, ['r', { t: 'min', sub: true }], { size: 46 });
    txt(dyn, rmax - 40, rmax - 174 < 130 ? 650 : 600, ['r', { t: 'max', sub: true }], { size: 46 });
  };
  const inp = slider(el, { label: 'Énergie E2 (négative)', min: 0.05, max: 0.68, step: 0.01, value: E0, format: (v) => (v < 0.1 ? 'ellipse presque circulaire' : 'ellipse : r entre rmin et rmax'), onInput: draw });
  resetButton(el, () => { inp.value = E0; inp.dispatchEvent(new Event('input')); });
}
