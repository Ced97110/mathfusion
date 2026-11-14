// Fig. 15.2 : gas in a cylinder closed by a piston. Pressure p = F / S. Sliders change the force F and the side of the square piston.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const F0 = 50, C0 = 10; // book: F = 50 N, square piston of side 10 cm (S = 0.01 m2)
const CX = 328, W0 = 390, PXN = 135 / 50; // px measured on the book figure: centre, width at 10 cm, arrow px per newton
// molecules: [x, y, arrow dx, arrow dy] in book pixels (measured)
const MOL = [[211, 313, 26, -47], [348, 285, 9, -31], [445, 332, -47, 25], [289, 408, -31, -47], [192, 523, 40, -31], [270, 494, -38, 23], [426, 504, 17, -46]];

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 15.2. Un cylindre fermé par un piston contient des molécules de gaz qui bougent dans toutes les directions. Une force F vers le bas tient le piston, d’aire S. La pression est p = F/S.');
  const dyn = add(root, 'g');
  const draw = (f, c) => {
    clear(dyn);
    const w = (W0 * c) / C0, xl = CX - w / 2, xr = CX + w / 2, k = w / W0;
    add(dyn, 'rect', { x: xl, y: 178, width: w, height: 60, fill: COL.grey });
    for (const [x, y, dx, dy] of MOL) arrow(dyn, [CX + (x - CX) * k, y], [CX + (x - CX) * k + dx, y + dy], { c: COL.blue, w: 5, h: 18 });
    for (const [x, y] of MOL) add(dyn, 'circle', { cx: CX + (x - CX) * k, cy: y, r: 15, fill: COL.blue });
    add(dyn, 'line', { x1: xl, y1: 118, x2: xl, y2: 580, stroke: '#000', 'stroke-width': 11 });
    add(dyn, 'line', { x1: xr, y1: 118, x2: xr, y2: 580, stroke: '#000', 'stroke-width': 11 });
    add(dyn, 'line', { x1: xl - 5, y1: 580, x2: xr + 5, y2: 580, stroke: '#000', 'stroke-width': 11 });
    add(dyn, 'line', { x1: CX, y1: 12, x2: CX, y2: 182, stroke: '#000', 'stroke-width': 10 });
    arrow(dyn, [CX, 155 - PXN * f], [CX, 155], { c: COL.red, w: 7, h: 26 });
    txt(dyn, CX + 25, 100, 'F', { size: 58, fill: COL.red });
    txt(dyn, xr + 20, 225, 'P', { size: 58 });
    add(dyn, 'line', { x1: xr, y1: 262, x2: xr + 55, y2: 337, stroke: COL.grey, 'stroke-width': 4 });
    txt(dyn, xr + 20, 370, 'S', { size: 58 });
    txt(dyn, 46 + xl - (CX - W0 / 2), 545, 'gaz', { size: 50, fill: COL.blue, it: false }); // keeps the book gap to the left wall
    const m = c / 100, s = m * m;
    readout(dyn, [`S = ${fr(m, 2)} × ${fr(m, 2)} = ${fr(s, 4)} m²`, `p = F ÷ S = ${f} ÷ ${fr(s, 4)} = ${Math.round(f / s)} N/m²`], 612, 26);
  };
  let f = F0, c = C0;
  const i1 = slider(el, { label: 'Force F', min: 25, max: 55, step: 5, value: F0, unit: 'N', onInput: (v) => { f = v; draw(f, c); } });
  const i2 = slider(el, { label: 'Côté du piston', min: 6, max: 14, step: 1, value: C0, unit: 'cm', onInput: (v) => { c = v; draw(f, c); } });
  resetButton(el, () => { for (const [i, v] of [[i1, F0], [i2, C0]]) { i.value = v; i.dispatchEvent(new Event('input')); } });
}
