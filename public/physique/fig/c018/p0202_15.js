// Fig. 18.3 : triangulation. Base L fixed, angles θ1 and θ2 measured in A and B; h = L / (cot θ1 + cot θ2). Two sliders.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, readout, fr } from '../kit.js';

const AX = 135, AY = 470, LP = 482; // A and base length in px (measured on the book figure)
const TH1_0 = 52, TH2_0 = 65; // angles of the book figure, measured on the drawing
const rad = (d) => (d * Math.PI) / 180, cot = (d) => 1 / Math.tan(rad(d));
const L_TEXT = 1000; // text: case L = 1000 m

export function mount(el) {
  const root = svg(el, 760, 820, 'Figure 18.3. Deux observateurs en A et B, séparés par la base L, visent le même satellite S et mesurent les angles θ1 et θ2. Ces trois nombres fixent la hauteur h du triangle, tracée en rouge pointillé.');
  root.setAttribute('viewBox', '0 -120 760 820');
  const dyn = add(root, 'g');
  let t1 = TH1_0, t2 = TH2_0;
  const draw = () => {
    clear(dyn);
    const hr = 1 / (cot(t1) + cot(t2)), h = hr * LP, sx = AX + h * cot(t1), sy = AY - h, bx = AX + LP;
    add(dyn, 'line', { x1: AX, y1: AY, x2: sx, y2: sy, stroke: COL.blue, 'stroke-width': 8 });
    add(dyn, 'line', { x1: bx, y1: AY, x2: sx, y2: sy, stroke: COL.blue, 'stroke-width': 8 });
    add(dyn, 'line', { x1: AX, y1: AY, x2: bx, y2: AY, stroke: '#000', 'stroke-width': 10 });
    add(dyn, 'line', { x1: sx, y1: AY, x2: sx, y2: sy, stroke: COL.red, 'stroke-width': 6, 'stroke-dasharray': '14 10' });
    const r = 75, a = rad(t1), b = rad(t2);
    add(dyn, 'path', { d: `M${AX + r * Math.cos(a)},${AY - r * Math.sin(a)} A${r},${r} 0 0 0 ${AX + r},${AY}`, fill: 'none', stroke: COL.green, 'stroke-width': 6 });
    add(dyn, 'path', { d: `M${bx - r * Math.cos(b)},${AY - r * Math.sin(b)} A${r},${r} 0 0 1 ${bx - r},${AY}`, fill: 'none', stroke: COL.green, 'stroke-width': 6 });
    for (const [x, y] of [[AX, AY], [bx, AY], [sx, sy]]) add(dyn, 'circle', { cx: x, cy: y, r: 14, fill: '#000' });
    txt(dyn, sx + 20, sy - 25, 'S', { size: 56 });
    txt(dyn, AX - 55, AY + 45, 'A', { size: 56 });
    txt(dyn, bx + 20, AY + 45, 'B', { size: 56 });
    txt(dyn, (AX + bx) / 2 - 20, AY + 70, 'L', { size: 56 });
    txt(dyn, sx + 20, (sy + AY) / 2 + 25, 'h', { size: 56, fill: COL.red });
    txt(dyn, AX + 112 * Math.cos(a / 2) - 25, AY - 112 * Math.sin(a / 2) + 18, ['θ', { t: '1', sub: true }], { size: 50, fill: COL.green });
    txt(dyn, bx - 112 * Math.cos(b / 2) - 25, AY - 112 * Math.sin(b / 2) + 18, ['θ', { t: '2', sub: true }], { size: 50, fill: COL.green });
    readout(dyn, [`θ1 = ${t1}°   θ2 = ${t2}°   h = L / (cot θ1 + cot θ2) = ${fr(hr, 3)} L`, `avec L = ${L_TEXT} m (cas du texte) : h = ${fr(hr * L_TEXT, 0)} m`], 585, 24);
  };
  const a = slider(el, { label: 'Angle θ1 en A', min: 30, max: 65, step: 1, value: TH1_0, unit: '°', onInput: (v) => { t1 = v; draw(); } });
  const b = slider(el, { label: 'Angle θ2 en B', min: 30, max: 65, step: 1, value: TH2_0, unit: '°', onInput: (v) => { t2 = v; draw(); } });
  resetButton(el, () => { a.value = TH1_0; b.value = TH2_0; a.dispatchEvent(new Event('input')); b.dispatchEvent(new Event('input')); });
}
