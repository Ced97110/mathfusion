// Fig. 9.1 : a (3 km, east) then b (4 km); the red arrow is a + b. The slider changes the angle between a and b.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

// letter with a drawn arrow above it (vector); returns the x after the letter
function vec(p, x, y, ch, size, c) {
  txt(p, x, y, ch, { size, fill: c });
  const yy = y - size * 0.8;
  arrow(p, [x + size * 0.02, yy], [x + size * 0.5, yy], { c, w: 3, h: 12 });
  return x + size * 0.62;
}
const txt2 = (p, x, y, t, c, size) => { txt(p, x, y, t, { size, fill: c, it: false }); return x + size * 0.85; };
const OX = 98, OY = 422, U = 103; // origin and px per km (measured on the book figure)
const A = 3, B = 4, PHI0 = 90; // book: a = 3 km east, b = 4 km north (angle 90°)
const rad = (d) => (d * Math.PI) / 180;

export function mount(el) {
  const root = svg(el, 760, 620, 'Figure 9.1. Trajet à pied : la flèche a va vers l’est sur 3 km, la flèche b part du bout de a et monte vers le nord sur 4 km. La flèche rouge a + b, de O au bout de b, mesure 5 km.');
  root.setAttribute('viewBox', '-170 0 930 620'); // extra room on the left for the labels of a + b
  const fix = add(root, 'g');
  arrow(fix, [575, 415], [575, 308], { c: COL.grey, w: 6, h: 22 });
  arrow(fix, [581, 422], [667, 422], { c: COL.grey, w: 6, h: 22 });
  txt(fix, 562, 288, 'nord', { size: 36, fill: COL.grey, it: false });
  txt(fix, 630, 470, 'est', { size: 36, fill: COL.grey, it: false });
  arrow(fix, [OX, OY], [OX + A * U, OY], { c: COL.blue, w: 10, h: 34 });
  txt(fix, vec(fix, 225, 488, 'a', 58, COL.blue) + 18, 488, '(3 km)', { size: 58, fill: COL.blue, it: false });
  add(fix, 'circle', { cx: OX, cy: OY, r: 12, fill: '#000' });
  txt(fix, 50, 472, 'O', { size: 56 });
  const dyn = add(root, 'g');

  const draw = (deg) => {
    clear(dyn);
    const p = rad(deg), bx = B * Math.cos(p), by = B * Math.sin(p);
    const tx = OX + A * U, ty = OY, ex = tx + bx * U, ey = ty - by * U;
    const sx = A + bx, sy = by, sl = Math.hypot(sx, sy);
    arrow(dyn, [tx, ty], [ex, ey], { c: COL.green, w: 10, h: 34 });
    arrow(dyn, [OX, OY], [ex, ey], { c: COL.red, w: 12, h: 34 });
    if (Math.abs(deg - 90) < 0.5) {
      add(dyn, 'polyline', { points: `${tx - 25},${ty} ${tx - 25},${ty - 26} ${tx},${ty - 26}`, fill: 'none', stroke: '#000', 'stroke-width': 5 });
    } else {
      const r = 45, a1 = -p;
      add(dyn, 'path', { d: `M${tx + r},${ty} A${r},${r} 0 0 ${deg < 90 ? 0 : 0} ${tx + r * Math.cos(a1)},${ty + r * Math.sin(a1)}`, fill: 'none', stroke: '#000', 'stroke-width': 4 });
    }
    // labels of a + b (left of the red arrow) and of b (right of the green arrow)
    const mx = (OX + ex) / 2, my = (OY + ey) / 2, ux = (ex - OX) / (sl * U), uy = (ey - OY) / (sl * U);
    const r = Math.min(1.8, Math.abs(ux / uy)), off = 40 + 30 * r, rx = mx + off * uy, ry = my - off * ux;
    const w = 62 * 2.09, dx2 = Math.min(0, 55 * (ux / uy));
    vec(dyn, txt2(dyn, vec(dyn, rx - w, ry, 'a', 62, COL.red), ry, '+', COL.red, 62), ry, 'b', 62, COL.red);
    txt(dyn, rx + dx2, ry + 55, `(${fr(sl)} km)`, { size: 44, fill: COL.red, it: false, anchor: 'end' });
    const gx = (tx + ex) / 2, gy = (ty + ey) / 2;
    const dx = Math.cos(p), dy = -Math.sin(p), nx = -dy, ny = dx, xs = (80 * Math.max(0, -dx)) / Math.sin(p);
    vec(dyn, gx + 20 * nx + 20, gy + 20 * ny + 15, 'b', 62, COL.green);
    txt(dyn, gx + 20 * nx + 20 + xs, gy + 20 * ny + 95, '(4 km)', { size: 42, fill: COL.green, it: false });
    readout(dyn, [`angle entre a et b : ${fr(deg, 0)}°`, `|a + b|² = 3² + 4² + 2·3·4·cos ${fr(deg, 0)}° = ${fr(sl * sl, 1)}   donc   |a + b| = ${fr(sl)} km`], 540, 26);
  };
  const inp = slider(el, { label: 'Angle entre a et b', min: 60, max: 150, step: 1, value: PHI0, unit: '°', onInput: draw });
  resetButton(el, () => { inp.value = PHI0; inp.dispatchEvent(new Event('input')); });
}
