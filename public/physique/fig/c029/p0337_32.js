// Fig. 29.2 : a point moves along a radius of a turning plate; seen from the ground it follows a curve. Fc = 2 m ω v. The slider scales ω.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const OX = 355, OY = 242, RP = 226, STEP = 72, PHI = 18.2; // centre, plate radius, radial step per instant (px) and rotation per instant (deg) measured on the book figure
const FC0 = 65, VK = 0.835; // length of Fc and scale of v in the book figure (px), measured
const rad = (d) => (d * Math.PI) / 180, PUR = '#6c3483';
const M = 1, OM0 = 2, VR = 0.5; // text: m = 1 kg, ω = 2 rad/s, v = 0,5 m/s, Fc = 2 N
const P = (u, w) => [OX + STEP * u * Math.cos(rad(PHI * w * u)), OY - STEP * u * Math.sin(rad(PHI * w * u))];

export function mount(el) {
  const root = svg(el, 760, 620, 'Figure 29.2. Vue depuis le sol : un point se déplace le long d’un rayon d’un plateau qui tourne à la vitesse angulaire ω. Positions 1, 2, 3 à trois instants : le point suit une courbe. La force de Coriolis Fc, perpendiculaire à la vitesse, vaut 2mωv.');
  root.setAttribute('viewBox', '0 -70 760 690');
  const fix = add(root, 'g');
  add(fix, 'circle', { cx: OX, cy: OY, r: RP, fill: '#e6e6e6', stroke: COL.grey, 'stroke-width': 6 });
  add(fix, 'path', { d: 'M100,333 Q128,450 262,497', fill: 'none', stroke: COL.grey, 'stroke-width': 7 });
  add(fix, 'polygon', { points: '274,500 248,488 252,512', fill: COL.grey });
  txt(fix, 50, 445, 'ω', { size: 60, fill: COL.grey });
  const dyn = add(root, 'g');

  const draw = (w) => {
    clear(dyn);
    for (let k = 1; k <= 3; k++) { const a = rad(PHI * w * k); add(dyn, 'line', { x1: OX, y1: OY, x2: OX + RP * Math.cos(a), y2: OY - RP * Math.sin(a), stroke: COL.blue, 'stroke-width': 5, 'stroke-dasharray': '14 8' }); }
    const pts = []; for (let i = 0; i <= 60; i++) pts.push(P((3 * i) / 60, w));
    poly(dyn, pts, { stroke: COL.red, 'stroke-width': 8, 'stroke-linecap': 'round' });
    add(dyn, 'circle', { cx: OX, cy: OY, r: 11, fill: '#000' });
    for (let k = 1; k <= 3; k++) {
      const [x, y] = P(k, w);
      add(dyn, 'circle', { cx: x, cy: y, r: 15, fill: COL.red });
      txt(dyn, x + 28, y + 40, String(k), { size: 56, fill: COL.red, it: false });
    }
    // ground velocity at point 2 : radial STEP and tangential r ω per instant
    const [x2, y2] = P(2, w), a2 = rad(PHI * w * 2), vr = STEP, vt = 2 * STEP * rad(PHI * w);
    const vx = vr * Math.cos(a2) - vt * Math.sin(a2), vy = -(vr * Math.sin(a2) + vt * Math.cos(a2)), vl = Math.hypot(vx, vy), dx = vx / vl, dy = vy / vl;
    arrow(dyn, [x2, y2], [x2 + VK * vx, y2 + VK * vy], { c: COL.green, w: 8, h: 24 });
    const tx = x2 + VK * vx, ty = y2 + VK * vy;
    txt(dyn, tx + 62 * dx + 8, ty + 62 * dy + 18, 'v', { size: 54, fill: COL.green });
    arrow(dyn, [tx + 62 * dx + 10, ty + 62 * dy - 22], [tx + 62 * dx + 40, ty + 62 * dy - 22], { c: COL.green, w: 3, h: 11 });
    // Fc : perpendicular to v (turned to the left), length proportional to ω
    const fl = FC0 * w, fx = dy, fy = -dx, ex = x2 + fl * fx, ey = y2 + fl * fy;
    arrow(dyn, [x2, y2], [ex, ey], { c: PUR, w: 8, h: 24 });
    const gx = ex + 70 * fx - 28, gy = ey + 70 * fy + 22;
    txt(dyn, gx, gy, ['F', { t: 'c', sub: true }], { size: 54, fill: PUR });
    arrow(dyn, [gx + 2, gy - 44], [gx + 34, gy - 44], { c: PUR, w: 3, h: 11 });
    readout(dyn, [`m = ${M} kg   ω = ${fr(w * OM0, 1)} rad/s   v = ${fr(VR)} m/s`, `Fc = 2 m ω v = 2 × ${M} × ${fr(w * OM0, 1)} × ${fr(VR)} = ${fr(2 * M * w * OM0 * VR, 2)} N`], 570, 24);
  };
  const inp = slider(el, { label: 'Vitesse angulaire ω du plateau', min: 0.8, max: 3.2, step: 0.1, value: OM0, unit: 'rad/s', onInput: (v) => draw(v / OM0) });
  resetButton(el, () => { inp.value = OM0; inp.dispatchEvent(new Event('input')); });
}
