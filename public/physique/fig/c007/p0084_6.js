// Fig. 7.2 : two cars. Red: x = 30 t. Blue: x = 20 + v t (book: v = 15). The slider changes the blue speed: R moves.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const X0 = 107, Y0 = 552, SX = 158.6, SY = 5; // px per second, px per metre (measured on the book figure)
const V0 = 15, VR = 30, D0 = 20;
const px = (t) => X0 + SX * t, py = (x) => Y0 - SY * x;
const TMAX = 3;

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 7.2. Position x de deux voitures en fonction du temps t. La bleue part de 20 m, la rouge part de O et va deux fois plus vite. Au point R, la rouge rattrape la bleue.');
  const fix = add(root, 'g');
  arrow(fix, [107, 575], [107, 40], { w: 5, h: 28 });
  arrow(fix, [87, Y0], [705, Y0], { w: 5, h: 28 });
  txt(fix, 38, 40, [{ t: 'x (m)', it: false }], { size: 34 });
  txt(fix, 592, 596, ['t', { t: ' (s)', it: false }], { size: 38 });
  txt(fix, 36, 462, '20', { size: 38, fill: COL.blue, it: false });
  add(fix, 'line', { x1: px(0), y1: py(0), x2: px(TMAX), y2: py(VR * TMAX), stroke: COL.red, 'stroke-width': 8, 'stroke-linecap': 'round' });
  txt(fix, 425, 160, `pente ${VR}`, { size: 40, fill: COL.red, it: false });
  add(fix, 'circle', { cx: px(0), cy: py(0), r: 12, fill: '#000' });
  txt(fix, 120, 592, 'O', { size: 52 });
  const dyn = add(root, 'g');

  const draw = (v) => {
    clear(dyn);
    const tr = D0 / (VR - v), xr = VR * tr;
    add(dyn, 'line', { x1: px(0), y1: py(D0), x2: px(TMAX), y2: py(D0 + v * TMAX), stroke: COL.blue, 'stroke-width': 8, 'stroke-linecap': 'round' });
    add(dyn, 'line', { x1: px(tr), y1: py(xr), x2: px(tr), y2: Y0, stroke: COL.grey, 'stroke-width': 4, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' });
    add(dyn, 'circle', { cx: px(tr), cy: py(xr), r: 12, fill: '#000' });
    txt(dyn, px(tr) - 54, py(xr) - 22, 'R', { size: 52 });
    txt(dyn, px(tr) - 38, 596, fr(tr, 2), { size: 34, it: false });
    txt(dyn, 410, py(D0 + v * 2.48) + 94, `pente ${fr(v, 1)}`, { size: 40, fill: COL.blue, it: false });
    readout(dyn, [`rouge : x = 30 t   bleue : x = 20 + ${fr(v, 1)} t`, `R : 20 + ${fr(v, 1)} t = 30 t, t = 20/${fr(VR - v, 1)} = ${fr(tr, 2)} s, x = ${fr(xr, 1)} m`], 635, 24);
  };
  const inp = slider(el, { label: 'Vitesse de la voiture bleue', min: 5, max: 20, step: 1, value: V0, unit: 'm/s', onInput: draw });
  resetButton(el, () => { inp.value = V0; inp.dispatchEvent(new Event('input')); });
}
