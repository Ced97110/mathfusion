// Fig. 30.2 : wheel mounted askew. ω1 = 3 rad/s, ω2 = 4 rad/s (text), I2 = 1, I1 = 2 I2 for a disc. L = I1 ω1 + I2 ω2. The slider changes I1/I2.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const W1 = 3, W2 = 4, I2 = 1, K0 = 2; // text: ω1 = 3, ω2 = 4 rad/s, I2 = 1, I1 = 2 I2
const OX = 230, OY = 191, U = 43; // origin and px per rad/s (layout choice)
const WN = Math.hypot(W1, W2), c = W1 / WN, s = W2 / WN; // ω = 5 rad/s ; ω1 = ω cos α, ω2 = ω sin α
const u1 = [c, s], u2 = [s, -c]; // screen directions (y down): ω1 down-right, perpendicular to the wheel ; ω2 up-right, in the wheel plane

function vec(p, x, y, ch, sub, size, col) { // letter, subscript and a drawn arrow above
  txt(p, x, y, [ch, ...(sub ? [{ t: sub, sub: true }] : [])], { size, fill: col });
  arrow(p, [x + size * 0.04, y - size * 0.8], [x + size * 0.52, y - size * 0.8], { c: col, w: 3, h: 12 });
}

export function mount(el) {
  const root = svg(el, 760, 650, 'Figure 30.2. Une roue montée de travers sur son axe. La vitesse angulaire ω se décompose en ω1 = 3 rad/s, perpendiculaire au plan de la roue, et ω2 = 4 rad/s, dans ce plan. Les moments d’inertie I1 et I2 sont différents : L = I1 ω1 + I2 ω2 n’est pas dans la direction de ω.');
  const fix = add(root, 'g');
  add(fix, 'line', { x1: 20, y1: OY, x2: 700, y2: OY, stroke: '#000', 'stroke-width': 8 });
  const ang = -Math.atan2(u2[1], u2[0]) * 180 / Math.PI; // wheel plane = direction of ω2
  add(fix, 'ellipse', { cx: OX, cy: OY, rx: 186, ry: 37, transform: `rotate(${-ang} ${OX} ${OY})`, fill: '#d0d8e4', stroke: COL.grey, 'stroke-width': 4 });
  const t1 = [OX + U * W1 * u1[0], OY + U * W1 * u1[1]], t2 = [OX + U * W2 * u2[0], OY + U * W2 * u2[1]], ex = OX + U * WN;
  add(fix, 'polyline', { points: `${t2},${ex},${OY} ${t1}`, fill: 'none', stroke: COL.grey, 'stroke-width': 4, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' });
  for (const t of [t1, t2]) add(fix, 'line', { x1: OX, y1: OY, x2: t[0] - (t[0] - OX) * 0.05, y2: t[1] - (t[1] - OY) * 0.05, stroke: COL.green, 'stroke-width': 6, 'stroke-dasharray': '16 9' });
  arrow(fix, [OX, OY], [ex, OY], { c: COL.green, w: 9, h: 30 });
  vec(fix, ex - 10, OY - 40, 'ω', '', 56, COL.green);
  vec(fix, t2[0] + 14, t2[1] - 16, 'ω', '2', 52, COL.green);
  vec(fix, t1[0] - 6, t1[1] + 72, 'ω', '1', 52, COL.green);
  const dyn = add(root, 'g');

  const draw = (k) => {
    clear(dyn);
    const l1 = k * I2 * W1, l2 = I2 * W2; // L1 = I1 ω1, L2 = I2 ω2
    const lx = U * (l1 * u1[0] + l2 * u2[0]), ly = U * (l1 * u1[1] + l2 * u2[1]), l = Math.hypot(lx, ly);
    arrow(dyn, [OX, OY], [OX + lx, OY + ly], { c: COL.red, w: 10, h: 30 });
    vec(dyn, OX + lx + 40 * lx / l - 4, OY + ly + 40 * ly / l + 22, 'L', '', 56, COL.red);
    const a = (Math.atan2(ly, lx) * 180) / Math.PI;
    readout(dyn, [`ω1 = ${W1} rad/s   ω2 = ${W2} rad/s   I2 = ${I2}   I1 = ${fr(k * I2, 1)}`, `L1 = I1 ω1 = ${fr(l1, 1)}   L2 = I2 ω2 = ${fr(l2, 1)}`, `angle entre L et ω : ${fr(a - 0, 1)}°   (0° si I1 = I2)`], 570, 24);
  };
  const inp = slider(el, { label: 'Rapport I1/I2 (disque : 2)', min: 1, max: 4, step: 0.1, value: K0, onInput: draw });
  resetButton(el, () => { inp.value = K0; inp.dispatchEvent(new Event('input')); });
}
