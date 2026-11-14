// Fig. 9.2 : vector v of length 10 at angle θ with the x axis; vx = v cos θ, vy = v sin θ. The slider changes θ.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const OX = 94, OY = 389, U = 48.5, V = 10, TH0 = 30; // origin and px per unit (measured on the book figure)
const rad = (d) => (d * Math.PI) / 180;

export function mount(el) {
  const root = svg(el, 760, 640, 'Figure 9.2. Un vecteur v de longueur 10 fait un angle θ avec l’axe x. Sa composante selon x est v cos θ, sa composante selon y est v sin θ : ce sont les deux côtés de l’angle droit du triangle.');
  const fix = add(root, 'g');
  arrow(fix, [35, OY], [700, OY], { w: 5, h: 30 });
  arrow(fix, [OX, 487], [OX, 45], { w: 5, h: 30 });
  txt(fix, 100, 42, 'y', { size: 40 });
  txt(fix, 668, 432, 'x', { size: 40 });
  add(fix, 'circle', { cx: OX, cy: OY, r: 12, fill: '#000' });
  txt(fix, 50, 452, 'O', { size: 56 });
  const dyn = add(root, 'g');

  const draw = (deg) => {
    clear(dyn);
    const t = rad(deg), c = Math.cos(t), s = Math.sin(t), vx = V * c, vy = V * s;
    const ex = OX + vx * U, ey = OY - vy * U, px = Math.sin(t) * -1, py = -Math.cos(t);
    add(dyn, 'line', { x1: OX, y1: OY, x2: ex, y2: OY, stroke: COL.blue, 'stroke-width': 10 });
    add(dyn, 'line', { x1: ex, y1: OY, x2: ex, y2: ey, stroke: COL.green, 'stroke-width': 14 });
    arrow(dyn, [OX, OY], [ex, ey], { c: COL.red, w: 10, h: 34 });
    add(dyn, 'polyline', { points: `${ex - 25},${OY} ${ex - 25},${OY - 24} ${ex},${OY - 24}`, fill: 'none', stroke: '#000', 'stroke-width': 5 });
    const r = 107;
    add(dyn, 'path', { d: `M${OX + r * c},${OY - r * s} A${r},${r} 0 0 0 ${OX + r},${OY}`, fill: 'none', stroke: '#000', 'stroke-width': 5 });
    const at = (f, k) => [OX + f * (ex - OX) + k * px, OY + f * (ey - OY) + k * py];
    const [lx, ly] = at(0.7, 50), [wx, wy] = at(0.25, 70);
    txt(dyn, lx - 22, ly + 14, '10', { size: 52, fill: COL.red, it: false });
    txt(dyn, wx - 14, wy + 14, 'v', { size: 62, fill: COL.red });
    arrow(dyn, [wx - 12, wy - 36], [wx + 18, wy - 36], { c: COL.red, w: 3, h: 12 });
    const th = txt(dyn, 215, 365, [{ t: 'θ', it: true }, { t: ` = ${fr(deg, 0)}°`, it: false }], { size: 46 });
    th.setAttribute('style', 'paint-order:stroke;stroke:#fff;stroke-width:8px');
    txt(dyn, 195, 462, [{ t: 'v' }, { t: 'x', sub: true }, { t: ` = ${fr(vx)}`, it: false }], { size: 52, fill: COL.blue });
    txt(dyn, ex + 20, (OY + ey) / 2 + 16, [{ t: 'v' }, { t: 'y', sub: true }, { t: ` = ${fr(vy)}`, it: false }], { size: 52, fill: COL.green });
    readout(dyn, [`vx = 10 cos ${fr(deg, 0)}° = ${fr(vx)}   vy = 10 sin ${fr(deg, 0)}° = ${fr(vy)}`, `vx² + vy² = ${fr(vx * vx, 1)} + ${fr(vy * vy, 1)} = ${fr(vx * vx + vy * vy, 0)}`], 540, 26);
  };
  const inp = slider(el, { label: 'Angle θ', min: 15, max: 45, step: 1, value: TH0, unit: '°', onInput: draw });
  resetButton(el, () => { inp.value = TH0; inp.dispatchEvent(new Event('input')); });
}
