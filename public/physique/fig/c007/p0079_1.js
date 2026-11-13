// Fig. 7.1 : line y = 2x + 3, points P (1, 5) and Q (3, 9). The slider moves Q along the line: the slope stays 2.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const X0 = 139, Y0 = 605, UX = 114, UY = 44; // origin and px per unit (measured on the book figure)
const XP = 1, XQ0 = 3, M = 2, B = 3; // book: P at x = 1, Q at x = 3, y = 2x + 3
const px = (x) => X0 + UX * x, py = (y) => Y0 - UY * y;
const f = (x) => M * x + B;
const dot = { stroke: COL.grey, 'stroke-width': 4, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' };

export function mount(el) {
  const root = svg(el, 760, 740, 'Figure 7.1. Une droite y = 2x + 3 avec deux points P et Q. Du point P au point Q on avance de Δx puis on monte de Δy ; la pente Δy/Δx vaut 2. La droite coupe l’axe vertical en B, à la hauteur 3.');
  const fix = add(root, 'g');
  arrow(fix, [X0, 640], [X0, 40], { w: 5, h: 28 });
  arrow(fix, [35, Y0], [700, Y0], { w: 5, h: 28 });
  txt(fix, 148, 52, 'y', { size: 40 });
  txt(fix, 636, 668, 'x', { size: 50 });
  txt(fix, 80, 486, '3', { size: 38, it: false });
  add(fix, 'line', { x1: px(-0.62), y1: py(f(-0.62)), x2: px(4.02), y2: py(f(4.02)), stroke: COL.blue, 'stroke-width': 8, 'stroke-linecap': 'round' });
  add(fix, 'circle', { cx: X0, cy: py(B), r: 12, fill: '#000' });
  txt(fix, 158, 530, 'B', { size: 52 });
  add(fix, 'line', { x1: px(XP), y1: py(f(XP)), x2: px(XP), y2: Y0, ...dot });
  add(fix, 'circle', { cx: px(XP), cy: py(f(XP)), r: 12, fill: '#000' });
  txt(fix, 200, 372, 'P', { size: 52 });
  txt(fix, 243, 652, '1', { size: 38, it: false });
  const dyn = add(root, 'g');

  const draw = (xq) => {
    clear(dyn);
    const dx = xq - XP, dy = f(xq) - f(XP), qx = px(xq), qy = py(f(xq)), py0 = py(f(XP));
    add(dyn, 'line', { x1: qx, y1: qy, x2: qx, y2: Y0, ...dot });
    add(dyn, 'polyline', { points: `${px(XP)},${py0} ${qx},${py0} ${qx},${qy}`, fill: 'none', stroke: COL.red, 'stroke-width': 7 });
    add(dyn, 'circle', { cx: qx, cy: qy, r: 12, fill: '#000' });
    const hi = qy - 26 < 140;
    txt(dyn, hi ? qx + 18 : qx - 54, hi ? qy - 14 : qy - 26, 'Q', { size: 52 });
    txt(dyn, qx - 10, 652, fr(xq, 2), { size: 38, it: false });
    txt(dyn, qx + 20, (qy + py0) / 2 + 14, [{ t: 'Δ', it: false }, 'y', { t: ` = ${fr(dy)}`, it: false }], { size: 42, fill: COL.red });
    txt(dyn, (px(XP) + qx) / 2 - 60, py0 + 75, [{ t: 'Δ', it: false }, 'x', { t: ` = ${fr(dx)}`, it: false }], { size: 42, fill: COL.red });
    txt(dyn, 175, 114, `pente = ${fr(dy)}/${fr(dx)} = ${fr(dy / dx)}`, { size: 44, fill: COL.blue, it: false });
    readout(dyn, [`P (1 ; ${fr(f(XP))})   Q (${fr(xq)} ; ${fr(f(xq))})`], 700);
  };
  const inp = slider(el, { label: 'Abscisse de Q', min: 1.5, max: 4, step: 0.1, value: XQ0, onInput: draw });
  resetButton(el, () => { inp.value = XQ0; inp.dispatchEvent(new Event('input')); });
}
