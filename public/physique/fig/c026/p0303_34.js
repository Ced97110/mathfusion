// Fig. 26.3 : potential-energy profile Ep(x) and total energy E. The slider raises E: A and B move, then the mass passes the hump.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, poly } from '../kit.js';

// curve of the book figure, sampled from the drawing (px)
const C = [[97,60],[100,88],[103,116],[106,144],[109,172],[112,200],[116,228],[120,256],[124,284],[130,312],[134,340],[142,368],[150,396],[155,410],[161,424],[168,438],[177,449],[190,457],[205,456],[220,448],[234,436],[248,422],[262,404],[276,385],[290,367],[304,350],[318,330],[332,314],[346,298],[360,286],[374,273],[388,262],[402,254],[416,246],[430,241],[444,236],[458,233],[472,232],[487,231],[500,232],[514,233],[528,235],[542,238],[556,242],[570,246],[584,251],[598,256],[612,262],[626,268],[640,274],[654,280],[662,284]];
const YMIN = 458, YPEAK = 231, E0 = (YMIN - 340) / (YMIN - YPEAK); // E of the book: line at y = 340
const ye = (e) => YMIN - e * (YMIN - YPEAK);
const cross = (y) => { const r = []; for (let i = 0; i < C.length - 1; i++) { const [x0, y0] = C[i], [x1, y1] = C[i + 1]; if ((y0 - y) * (y1 - y) <= 0 && y0 !== y1) r.push(x0 + ((y - y0) / (y1 - y0)) * (x1 - x0)); } return r; };

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 26.3. Énergie potentielle Ep en fonction de la position x. Le creux en x1 est un équilibre stable, la bosse en x2 un équilibre instable. Le trait rouge est l’énergie totale E : la masse oscille entre A et B ; avec plus d’énergie elle franchit la bosse.');
  const fix = add(root, 'g');
  arrow(fix, [53, 605], [53, 45], { w: 5, h: 30 });
  arrow(fix, [38, 500], [705, 500], { w: 5, h: 30 });
  txt(fix, 35, 48, ['E', { t: 'p', sub: true }], { size: 40 });
  txt(fix, 478, 524, ['x', { t: ' (position)', it: false }], { size: 42 });
  poly(fix, C, { stroke: COL.blue, 'stroke-width': 9, 'stroke-linejoin': 'round' });
  add(fix, 'circle', { cx: 197, cy: 458, r: 12, fill: COL.green });
  add(fix, 'circle', { cx: 487, cy: 231, r: 12, fill: '#d35400' });
  txt(fix, 178, 575, ['x', { t: '1', sub: true }], { size: 50, fill: COL.green });
  const dyn = add(root, 'g');

  const draw = (e) => {
    clear(dyn);
    const y = ye(e), xs = cross(y), a = xs[0], b = e < 1 ? xs[1] : null, bound = e < 1;
    add(dyn, 'line', { x1: a, y1: y, x2: bound ? b : 660, y2: y, stroke: COL.red, 'stroke-width': 8 });
    if (bound) add(dyn, 'line', { x1: b, y1: y, x2: 660, y2: y, stroke: COL.red, 'stroke-width': 6, 'stroke-dasharray': '2 14', 'stroke-linecap': 'round' });
    add(dyn, 'circle', { cx: a, cy: y, r: 12, fill: '#000' });
    txt(dyn, a - 44, y - 20, 'A', { size: 56 });
    if (bound) {
      add(dyn, 'circle', { cx: b, cy: y, r: 12, fill: '#000' });
      txt(dyn, b + 12, y - 28, 'B', { size: 56 });
      const ya = YMIN - 0.356 * (YMIN - y), xa = cross(ya);
      arrow(dyn, [xa[0] + 4, ya], [xa[1] - 4, ya], { c: COL.red, w: 5, h: 18, both: true });
    }
    const ly = [200, 300, 125].find((b) => Math.abs(y - (b - 18)) > 45);
    txt(dyn, 465, ly, ['x', { t: '2', sub: true }], { size: 50, fill: '#d35400' });
    txt(dyn, y >= 330 ? 575 : 672, y >= 330 ? y - 25 : y + 14, 'E', { size: 50, fill: COL.red });
  };
  const inp = slider(el, { label: 'Énergie totale E', min: 0.05, max: 1.4, step: 0.01, value: E0, format: (v) => (v < 1 ? 'état lié : oscille entre A et B' : 'franchit la bosse et part'), onInput: draw });
  resetButton(el, () => { inp.value = E0; inp.dispatchEvent(new Event('input')); });
}
