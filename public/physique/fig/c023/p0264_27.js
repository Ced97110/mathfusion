// Fig. 23.2 : axis of velocities. Two equal masses at v1 and v2 stick: v = (v1 + v2) / 2. Seen from the vehicle at v: -u and +u.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const V10 = 4, V20 = 2; // book: v1 = 4 m/s, v2 = 2 m/s
const XM = 326, PXV = 162.5; // x of v = 3 and px per m/s, measured on the book figure
const X = (v) => XM + PXV * (v - 3);
const sub = (a, b) => [{ t: a }, { t: b, sub: true }];

export function mount(el) {
  const root = svg(el, 760, 600, 'Figure 23.2. L’axe des vitesses, vu du sol puis vu du véhicule. Les vitesses v2 et v1 avant le choc de deux masses égales sont de part et d’autre de la vitesse v après le choc, qui est leur milieu. Vue du véhicule, elles deviennent −u et +u, et v devient 0.');
  const fix = add(root, 'g');
  arrow(fix, [55, 90], [612, 90], { w: 5, h: 18 });
  arrow(fix, [55, 332], [612, 332], { w: 5, h: 18 });
  txt(fix, 42, 45, 'au sol', { size: 38, fill: COL.grey, it: false });
  txt(fix, 572, 70, 'vitesse', { size: 36, it: false });
  txt(fix, 42, 285, 'vu du véhicule', { size: 38, fill: COL.grey, it: false });
  const dyn = add(root, 'g');
  const draw = (v1, v2) => {
    clear(dyn);
    const v = (v1 + v2) / 2, u = (v1 - v2) / 2, x1 = X(v1), x2 = X(v2), xv = X(v);
    arrow(dyn, [x2 + 9, 35], [xv - 8, 35], { c: COL.grey, w: 4, h: 14, both: true });
    arrow(dyn, [xv + 9, 35], [x1 - 9, 35], { c: COL.grey, w: 4, h: 14, both: true });
    for (const [x, c] of [[x2, COL.blue], [x1, COL.blue], [xv, COL.red]]) add(dyn, 'circle', { cx: x, cy: 90, r: 12, fill: c });
    txt(dyn, x2 + 6, 158, sub('v', '2'), { size: 52, fill: COL.blue, anchor: 'middle' });
    txt(dyn, xv - 4, 158, 'v', { size: 52, fill: COL.red, anchor: 'middle' });
    txt(dyn, x1 + 8, 158, sub('v', '1'), { size: 52, fill: COL.blue, anchor: 'middle' });
    add(dyn, 'line', { x1: xv, y1: 188, x2: xv, y2: 308, stroke: COL.red, 'stroke-width': 4, 'stroke-dasharray': '2 7', 'stroke-linecap': 'round' });
    const bl = xv - PXV * u, br = xv + PXV * u;
    for (const [x, c] of [[bl, COL.blue], [xv, COL.red], [br, COL.blue]]) add(dyn, 'circle', { cx: x, cy: 332, r: 12, fill: c });
    txt(dyn, bl - 4, 412, [{ t: '−', it: false }, { t: 'u' }], { size: 54, fill: COL.blue, anchor: 'middle' });
    txt(dyn, xv + 3, 412, '0', { size: 54, fill: COL.red, anchor: 'middle', it: false });
    txt(dyn, br + 13, 412, [{ t: '+', it: false }, { t: 'u' }], { size: 54, fill: COL.blue, anchor: 'middle' });
    readout(dyn, [`v = (v₁ + v₂) ÷ 2 = (${fr(v1)} + ${fr(v2)}) ÷ 2 = ${fr(v)} m/s`, `u = (v₁ − v₂) ÷ 2 = ${fr(u)} m/s`, `avant : m × ${fr(v1)} + m × ${fr(v2)} = ${fr(v1 + v2)} m`, `après : 2m × ${fr(v)} = ${fr(2 * v)} m`], 480, 26);
  };
  let a = V10, b = V20;
  const i1 = slider(el, { label: 'Vitesse v₁', min: 3.5, max: 4.5, step: 0.25, value: V10, unit: 'm/s', onInput: (x) => { a = x; draw(a, b); } });
  const i2 = slider(el, { label: 'Vitesse v₂', min: 1.5, max: 2.5, step: 0.25, value: V20, unit: 'm/s', onInput: (x) => { b = x; draw(a, b); } });
  resetButton(el, () => { for (const [i, v] of [[i1, V10], [i2, V20]]) { i.value = v; i.dispatchEvent(new Event('input')); } });
}
