// Fig. 8.1 : point M on the unit circle, OH = cos θ, HM = sin θ. The slider changes θ.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const OX = 164, OY = 502, R = 415, TH0 = 50; // centre and radius in px (measured); θ = 50° measured on the book figure
const rad = (d) => (d * Math.PI) / 180;

export function mount(el) {
  const root = svg(el, 760, 740, 'Figure 8.1. Point M sur un cercle de centre O et de rayon 1. Angle θ entre l’axe horizontal et OM. H est le pied de la verticale issue de M : OH vaut cos θ, HM vaut sin θ.');
  const fix = add(root, 'g');
  arrow(fix, [38, OY], [700, OY], { w: 5, h: 30 });
  arrow(fix, [OX, 640], [OX, 12], { w: 5, h: 30 });
  const a0 = rad(105), a1 = rad(-15);
  add(fix, 'path', { d: `M${OX + R * Math.cos(a0)},${OY - R * Math.sin(a0)} A${R},${R} 0 0 1 ${OX + R * Math.cos(a1)},${OY - R * Math.sin(a1)}`, fill: 'none', stroke: COL.grey, 'stroke-width': 7 });
  txt(fix, 108, 562, 'O', { size: 56 });
  const dyn = add(root, 'g');

  const draw = (deg) => {
    clear(dyn);
    const t = rad(deg), c = Math.cos(t), s = Math.sin(t), mx = OX + R * c, my = OY - R * s;
    add(dyn, 'line', { x1: OX, y1: OY, x2: mx, y2: OY, stroke: COL.blue, 'stroke-width': 10 });
    add(dyn, 'line', { x1: mx, y1: OY, x2: mx, y2: my, stroke: COL.red, 'stroke-width': 16 });
    add(dyn, 'line', { x1: OX, y1: OY, x2: mx, y2: my, stroke: '#000', 'stroke-width': 8 });
    const r = 105;
    add(dyn, 'path', { d: `M${OX + r * c},${OY - r * s} A${r},${r} 0 0 0 ${OX + r},${OY}`, fill: 'none', stroke: COL.green, 'stroke-width': 6 });
    add(dyn, 'polyline', { points: `${mx - 25},${OY} ${mx - 25},${OY - 23} ${mx},${OY - 23}`, fill: 'none', stroke: '#000', 'stroke-width': 5 });
    for (const [x, y] of [[OX, OY], [mx, OY], [mx, my]]) add(dyn, 'circle', { cx: x, cy: y, r: 12, fill: '#000' });
    txt(dyn, mx + 20, my - 22, 'M', { size: 56 });
    txt(dyn, mx + 15, OY + 58, 'H', { size: 56 });
    const nx = -s, ny = -c;
    txt(dyn, OX + (mx - OX) / 2 + 70 * nx - 10, OY + (my - OY) / 2 + 70 * ny + 18, '1', { size: 52, it: false });
    txt(dyn, OX + 150 * Math.cos(t / 2) - 12, OY - 150 * Math.sin(t / 2) + 20, 'θ', { size: 60, fill: COL.green });
    txt(dyn, mx + 23, (my + OY) / 2 + 22, [{ t: 'sin ', it: false }, 'θ'], { size: 52, fill: COL.red });
    txt(dyn, OX + (mx - OX) / 2, 625, [{ t: 'cos ', it: false }, 'θ'], { size: 52, fill: COL.blue, anchor: 'middle' });
    readout(dyn, [`θ = ${fr(deg, 0)}°   cos θ = ${fr(c)}   sin θ = ${fr(s)}`, `OH² + HM² = ${fr(c * c + s * s, 2)} = OM²`], 690, 24);
  };
  const inp = slider(el, { label: 'Angle θ', min: 10, max: 80, step: 1, value: TH0, unit: '°', onInput: draw });
  resetButton(el, () => { inp.value = TH0; inp.dispatchEvent(new Event('input')); });
}
