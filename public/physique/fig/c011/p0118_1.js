// Fig. 11.1 : v = 10 t, area under the line cut in vertical bands of width dt. The slider changes dt.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const DT0 = 0.5; // book: bands of 0.5 s
const A = 10, TEND = 3; // v = 10 t ; distance from 0 to 3 s
const OX = 140, OY = 498, PXT = 166, PXV = 14.3; // px measured on the book figure: origin, px per s, px per m/s
const X = (t) => OX + PXT * t, Y = (v) => OY - PXV * v;

export function mount(el) {
  const root = svg(el, 760, 740, 'Figure 11.1. Vitesse v = 10 t en fonction du temps t, de 0 à 3 s. L’aire sous la droite est la distance. Elle est découpée en bandes verticales de largeur Δt ; chaque bande est un rectangle de hauteur v et de largeur Δt. Les petits triangles gris au-dessus des rectangles manquent à la somme.');
  const fix = add(root, 'g');
  add(fix, 'polygon', { points: `${X(0)},${Y(0)} ${X(TEND)},${Y(0)} ${X(TEND)},${Y(A * TEND)}`, fill: '#e3e3e3' });
  const dyn = add(root, 'g');
  const top = add(root, 'g');
  add(top, 'line', { x1: OX, y1: 12, x2: OX, y2: OY, stroke: '#000', 'stroke-width': 4 });
  add(top, 'line', { x1: OX - 2, y1: OY, x2: 703, y2: OY, stroke: '#000', 'stroke-width': 4 });
  for (const v of [0, 10, 20, 30]) {
    add(top, 'line', { x1: OX - 10, y1: Y(v), x2: OX, y2: Y(v), stroke: '#000', 'stroke-width': 3 });
    txt(top, OX - 20, Y(v) + 13, String(v), { size: 38, anchor: 'end', it: false });
  }
  for (let t = 0; t <= 3; t++) {
    add(top, 'line', { x1: X(t), y1: OY, x2: X(t), y2: OY + 10, stroke: '#000', 'stroke-width': 3 });
    txt(top, X(t), OY + 40, String(t), { size: 30, anchor: 'middle', it: false });
  }
  txt(top, 423, 580, [{ t: 't' }, { t: ' (temps, s)', it: false }], { size: 34, anchor: 'middle' });
  const yl = txt(top, 50, 255, [{ t: 'v' }, { t: ' (m/s)', it: false }], { size: 34, anchor: 'middle' });
  yl.setAttribute('transform', 'rotate(-90 50 255)');
  poly(top, [[X(0), Y(0)], [X(3.3), Y(A * 3.3)]], { stroke: COL.blue, 'stroke-width': 7 });

  const draw = (dt) => {
    clear(dyn);
    const n = Math.round(TEND / dt);
    let sum = 0;
    for (let i = 0; i < n; i++) {
      const t = i * dt, h = A * t;
      sum += h * dt;
      if (h > 0) add(dyn, 'rect', { x: X(t), y: Y(h), width: PXT * dt, height: PXV * h, fill: 'rgba(31,95,168,0.4)', stroke: 'rgba(31,95,168,0.5)', 'stroke-width': 3 });
    }
    const ts = Math.floor(2 / dt + 1e-9) * dt, xa = X(ts), xb = X(ts + dt);
    arrow(dyn, [xa + 2, 106], [xb - 2, 106], { c: COL.green, w: 5, h: 18, both: true });
    txt(dyn, (xa + xb) / 2, 66, [{ t: 'Δ', it: false }, { t: 't' }], { size: 46, fill: COL.green, anchor: 'middle' });
    arrow(dyn, [xb, OY - 2], [xb, Y(A * ts) + 4], { c: COL.blue, w: 3, h: 16, both: true });
    txt(dyn, xb + 15, Y(A * ts / 2) + 14, 'v', { size: 44, fill: COL.blue });
    add(dyn, 'rect', { x: 335, y: 415, width: 276, height: 46, fill: '#fff', opacity: 0.8 });
    txt(dyn, 473, 450, 'aire = distance', { size: 36, anchor: 'middle', it: false });
    const exact = 0.5 * A * TEND * TEND;
    readout(dyn, [`Δt = ${fr(dt)} s : ${n} bandes`, `somme des rectangles = ${fr(sum)} m`, `aire sous la droite = ½ × ${A * TEND} × ${TEND} = ${fr(exact)} m`, `triangles manquants = ${fr(exact - sum)} m`], 625, 26);
  };
  const inp = slider(el, { label: 'Largeur Δt', min: 0.25, max: 1, step: 0.25, value: DT0, unit: 's', onInput: draw });
  resetButton(el, () => { inp.value = DT0; inp.dispatchEvent(new Event('input')); });
}
