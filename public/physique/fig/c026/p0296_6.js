// Fig. 26.2 : small triangle of the staircase. Hypotenuse s = 2 m, angle θ with the force; x = s cos θ. The slider changes θ.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const TX = 251, TY = 58, SP = 405, S = 2, TH0 = 60; // top vertex, hypotenuse in px (measured); s = 2 m and θ = 60° (text example)
const rad = (d) => (d * Math.PI) / 180;

export function mount(el) {
  const root = svg(el, 760, 640, 'Figure 26.2. Un petit triangle rectangle de l’escalier : le corps avance de s le long de l’hypoténuse, la force F est dirigée vers le bas. Le côté vertical vaut x = s cos θ, le côté horizontal s sin θ.');
  const dyn = add(root, 'g');
  const draw = (deg) => {
    clear(dyn);
    const t = rad(deg), c = Math.cos(t), s = Math.sin(t), vx = SP * c, hx = SP * s, by = TY + vx, ex = TX + hx;
    add(dyn, 'line', { x1: TX, y1: TY - 4, x2: TX, y2: by + 4, stroke: COL.blue, 'stroke-width': 9 });
    add(dyn, 'line', { x1: TX - 4, y1: by, x2: ex + 2, y2: by, stroke: COL.green, 'stroke-width': 9 });
    arrow(dyn, [TX, TY], [ex, by], { w: 9, h: 30 });
    add(dyn, 'polyline', { points: `${TX},${by - 24} ${TX + 24},${by - 24} ${TX + 24},${by}`, fill: 'none', stroke: COL.grey, 'stroke-width': 4 });
    const r = 70;
    add(dyn, 'path', { d: `M${TX},${TY + r} A${r},${r} 0 0 0 ${TX + r * s},${TY + r * c}`, fill: 'none', stroke: COL.grey, 'stroke-width': 5 });
    txt(dyn, TX + 105 * Math.sin(t / 2) - 18, TY + 105 * Math.cos(t / 2) + 18, 'θ', { size: 52, fill: COL.grey });
    // F stays above the hypotenuse; when the hypotenuse would cross it, F moves to the right of the tip
    const side = deg <= 44, fx = side ? 490 : ex + 35, fb = side ? 275 : by - 10;
    arrow(dyn, [fx, fb - 120], [fx, fb], { c: COL.red, w: 8, h: 26 });
    const lx = side ? fx + 22 : fx - 62;
    txt(dyn, lx, fb - 62, 'F', { size: 52, fill: COL.red });
    arrow(dyn, [lx + 8, fb - 100], [lx + 40, fb - 100], { c: COL.red, w: 3, h: 10 });
    const mx = TX + hx / 2, my = TY + vx / 2;
    txt(dyn, mx + 60 * c - 14, my - 60 * s + 16, 's', { size: 52 });
    txt(dyn, TX - 68, my + 16, 'x', { size: 52, fill: COL.blue });
    txt(dyn, TX + hx / 2, by + 75, ['s sin ', 'θ'], { size: 46, fill: COL.green, anchor: 'middle' });
    txt(dyn, 408, 56, ['x = s cos ', 'θ'], { size: 46, fill: COL.blue });
    readout(dyn, [`s = ${S} m   θ = ${fr(deg, 0)}°   cos θ = ${fr(c)}`, `x = s cos θ = ${fr(S * c)} m   s sin θ = ${fr(S * s)} m`], by + 130, 24);
  };
  const inp = slider(el, { label: 'Angle θ entre la force et le déplacement', min: 10, max: 80, step: 1, value: TH0, unit: '°', onInput: draw });
  resetButton(el, () => { inp.value = TH0; inp.dispatchEvent(new Event('input')); });
}
