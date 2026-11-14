// Fig. 25.3 : pendulum released at height H: W H = 1/2 m V^2 at the bottom. The slider changes H (relative to the book figure); V follows V = sqrt(2 g H).
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const PV = [391, 20], L = 396, H0 = 106, V0PX = 127; // px measured on the book figure: pivot, rod length, H, length of the V arrow
const sub = (s) => s;

export function mount(el) {
  const root = svg(el, 760, 600, 'Figure 25.3. Un pendule lâché à la hauteur H : en haut la vitesse est nulle, en bas la hauteur est nulle et la vitesse est V. L’énergie de hauteur W H devient l’énergie de mouvement un demi m V au carré.');
  const fix = add(root, 'g');
  add(fix, 'line', { x1: 335, y1: 20, x2: 446, y2: 20, stroke: '#000', 'stroke-width': 8 });
  add(fix, 'line', { x1: PV[0], y1: PV[1], x2: PV[0], y2: PV[1] + L, stroke: COL.grey, 'stroke-width': 5 });
  add(fix, 'circle', { cx: PV[0], cy: PV[1], r: 12, fill: '#000' });
  add(fix, 'circle', { cx: PV[0], cy: PV[1] + L, r: 20, fill: COL.red });
  txt(fix, 512, 232, [{ t: 'W' }, { t: 'H' }], { size: 56, fill: COL.blue });
  const t2 = txt(fix, 522, 300, [{ t: '= ½', it: false }, { t: 'mV' }], { size: 56, fill: COL.red });
  add(t2, 'tspan', { dy: -22, 'font-size': 35, 'font-style': 'normal' }, '2');
  const dyn = add(root, 'g');
  const draw = (r) => {
    clear(dyn);
    const h = H0 * r, phi = Math.acos(1 - h / L), bx = PV[0] - L * Math.sin(phi), by = PV[1] + L * Math.cos(phi);
    add(dyn, 'line', { x1: PV[0], y1: PV[1], x2: bx, y2: by, stroke: COL.grey, 'stroke-width': 5 });
    const arc = []; for (let i = 0; i <= 60; i++) { const a = -phi + 0.09 + ((2 * phi - 0.09) * i) / 60; arc.push(`${i ? 'L' : 'M'}${(PV[0] + L * Math.sin(a)).toFixed(1)},${(PV[1] + L * Math.cos(a) + 5).toFixed(1)}`); }
    add(dyn, 'path', { d: arc.join(''), fill: 'none', stroke: COL.grey, 'stroke-width': 5, 'stroke-dasharray': '1 11', 'stroke-linecap': 'round' });
    add(dyn, 'line', { x1: bx - 27, y1: by, x2: bx + 230, y2: by, stroke: COL.blue, 'stroke-width': 4, 'stroke-dasharray': '16 9' });
    add(dyn, 'circle', { cx: bx, cy: by, r: 20, fill: COL.blue });
    const hx = bx - 7, bot = PV[1] + L;
    for (const y of [by, bot]) add(dyn, 'line', { x1: hx - 22, y1: y, x2: hx + 20, y2: y, stroke: COL.blue, 'stroke-width': 6 });
    add(dyn, 'line', { x1: hx, y1: by, x2: hx, y2: bot, stroke: COL.blue, 'stroke-width': 6 });
    txt(dyn, hx - 66, (by + bot) / 2 + 25, 'H', { size: 58, fill: COL.blue });
    txt(dyn, bx - 47, by - 48, [{ t: 'V', it: true }, { t: ' = 0', it: false }], { size: 52, fill: COL.blue });
    const len = V0PX * Math.sqrt(r);
    arrow(dyn, [423, bot], [423 + len, bot], { c: COL.red, w: 7, h: 26 });
    txt(dyn, 450, bot - 26, 'V', { size: 58, fill: COL.red });
    readout(dyn, [`H = ${fr(r, 2)} × (H du livre)`, `W H = ½ m V² donc V = √(2 g H) : V = ${fr(Math.sqrt(r), 2)} × (V du livre)`], 520, 26);
  };
  const inp = slider(el, { label: 'Hauteur H (× livre)', min: 0.4, max: 1.5, step: 0.1, value: 1, format: (v) => '×' + fr(v, 1), onInput: draw });
  resetButton(el, () => { inp.value = 1; inp.dispatchEvent(new Event('input')); });
}
