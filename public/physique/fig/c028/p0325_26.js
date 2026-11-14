// Fig. 28.2 : solid turning about O, centre of mass G at L from O. Lever arm of the weight d = L sin θ. The slider changes θ.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const OX = 282, OY = 110, LP = 413, RP = 551, TH0 = 30, L = 0.5; // O, OG and rod length in px (measured); θ = 30° and L = 0.5 m (text example)
const rad = (d) => (d * Math.PI) / 180;

function vec(p, x, y, ch, size, c) { // letter with a drawn arrow above it
  txt(p, x, y, ch, { size, fill: c });
  arrow(p, [x + size * 0.04, y - size * 0.8], [x + size * 0.52, y - size * 0.8], { c, w: 3, h: 12 });
}

export function mount(el) {
  const root = svg(el, 760, 740, 'Figure 28.2. Un solide tourne autour de l’axe fixe O. Son centre de masse G est à la distance L de O. Le poids mg s’applique en G ; son bras de levier est d = L sin θ, la distance de O à la verticale du poids.');
  const fix = add(root, 'g');
  add(fix, 'line', { x1: 183, y1: 88, x2: 381, y2: 88, stroke: '#000', 'stroke-width': 10 });
  const dyn = add(root, 'g');
  const draw = (deg) => {
    clear(dyn);
    const t = rad(deg), s = Math.sin(t), c = Math.cos(t), ux = s, uy = c, nx = c, ny = -s;
    const at = (a, w) => [OX + a * ux + w * nx, OY + a * uy + w * ny];
    const pts = [at(-20, -30), at(RP, -30), at(RP, 30), at(-20, 30)].map((p) => p.join(',')).join(' ');
    add(dyn, 'polygon', { points: pts, fill: '#d0d8e4' });
    const gx = OX + LP * s, gy = OY + LP * c;
    add(dyn, 'line', { x1: OX, y1: OY, x2: OX, y2: 598, stroke: COL.grey, 'stroke-width': 4, 'stroke-dasharray': '2 8', 'stroke-linecap': 'round' });
    add(dyn, 'line', { x1: gx, y1: 55, x2: gx, y2: 690, stroke: COL.red, 'stroke-width': 1.5, 'stroke-dasharray': '6 5', opacity: 0.6 });
    add(dyn, 'line', { x1: OX, y1: OY, x2: gx, y2: OY, stroke: COL.green, 'stroke-width': 7 });
    const r = 165;
    add(dyn, 'path', { d: `M${OX},${OY + r} A${r},${r} 0 0 0 ${OX + r * s},${OY + r * c}`, fill: 'none', stroke: COL.grey, 'stroke-width': 5 });
    arrow(dyn, [gx, gy], [gx, gy + 170], { c: COL.red, w: 9, h: 28 });
    add(dyn, 'circle', { cx: gx, cy: gy, r: 17, fill: COL.blue });
    add(dyn, 'circle', { cx: OX, cy: OY, r: 17, fill: '#000' });
    txt(dyn, 198, 128, 'O', { size: 62 });
    txt(dyn, OX + (gx - OX) * 0.45 - 12, OY - 42, 'd', { size: 56, fill: COL.green });
    const [lx, ly] = at(LP / 2, 100);
    txt(dyn, lx - 12, ly + 14, 'L', { size: 56, fill: COL.grey });
    txt(dyn, OX + 190 * Math.sin(t / 2) - 20, OY + 190 * Math.cos(t / 2) + 14, 'θ', { size: 56, fill: COL.grey });
    const [bx, by] = at(LP, 70);
    txt(dyn, bx - 8, by - 6, 'G', { size: 60, fill: COL.blue });
    txt(dyn, gx - 124, gy + 125, 'm', { size: 60, fill: COL.red });
    vec(dyn, gx - 66, gy + 125, 'g', 60, COL.red);
    const d = L * s;
    readout(dyn, [`L = ${fr(L)} m   θ = ${fr(deg, 0)}°   sin θ = ${fr(s)}`, `d = L sin θ = ${fr(d)} m   moment du poids = −m g L sin θ`], 690, 24);
  };
  const inp = slider(el, { label: 'Angle θ', min: 10, max: 55, step: 1, value: TH0, unit: '°', onInput: draw });
  resetButton(el, () => { inp.value = TH0; inp.dispatchEvent(new Event('input')); });
}
