// Fig. 10.1 : d = 5 t², A at t = 1 s, B at t = 2 s. The slider moves B: the secant AB tends to the tangent at A.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const X0 = 101, Y0 = 515.7, SX = 227, SY = 16.53; // px per second, px per metre (measured on the book figure)
const TA = 1, TB0 = 2, K = 5, TMAX = 2.37;
const px = (t) => X0 + SX * t, py = (d) => Y0 - SY * d, d = (t) => K * t * t;

export function mount(el) {
  const root = svg(el, 760, 690, 'Figure 10.1. Distance tombée d = 5t² en fonction du temps. Le point A est à t = 1 s, le point B à t = 2 s. La sécante AB est en gris, la tangente en A est en rouge, moins raide. Le triangle vert donne Δt et Δd.');
  const fix = add(root, 'g');
  arrow(fix, [101, 585], [101, 45], { w: 5, h: 28 });
  arrow(fix, [100, Y0], [705, Y0], { w: 5, h: 28 });
  txt(fix, 33, 40, [{ t: 'd (m)', it: false }], { size: 34 });
  txt(fix, 365, 572, ['t', { t: ' (temps, s)', it: false }], { size: 34 });
  const pts = [];
  for (let i = 0; i <= 120; i++) { const t = (TMAX * i) / 120; pts.push([px(t), py(d(t))]); }
  poly(fix, pts, { stroke: COL.blue, 'stroke-width': 8, 'stroke-linecap': 'round' });
  const m = 2 * K * TA, xa = px(TA), ya = py(d(TA)), kx = 218;
  add(fix, 'line', { x1: xa - kx, y1: ya + (m * SY / SX) * kx, x2: xa + kx * 1.15, y2: ya - (m * SY / SX) * kx * 1.15, stroke: COL.red, 'stroke-width': 7 });
  txt(fix, 135, 295, 'tangente', { size: 40, fill: COL.red, it: false });
  txt(fix, 135, 350, 'sécante', { size: 40, fill: COL.grey, it: false });
  const dyn = add(root, 'g');

  const draw = (tb) => {
    clear(dyn);
    const dt = tb - TA, dd = d(tb) - d(TA), sl = dd / dt, xb = px(tb), yb = py(d(tb));
    const sec = (t) => py(d(TA) + sl * (t - TA));
    add(dyn, 'line', { x1: px(0.604), y1: sec(0.604), x2: px(2.31), y2: sec(2.31), stroke: COL.grey, 'stroke-width': 6, 'stroke-dasharray': '16 9' });
    add(dyn, 'polyline', { points: `${xa},${ya} ${xb},${ya} ${xb},${yb}`, fill: 'none', stroke: COL.green, 'stroke-width': 5 });
    for (const [x, y] of [[xa, ya], [xb, yb]]) add(dyn, 'circle', { cx: x, cy: y, r: 11, fill: '#000' });
    txt(dyn, xa + 18, ya + 44, 'A', { size: 52 });
    txt(dyn, xb - 67, yb - 40, 'B', { size: 52 });
    txt(dyn, 398, ya + 45, [{ t: 'Δ', it: false }, 't'], { size: 44, fill: COL.green });
    txt(dyn, xb + 20, (ya + yb) / 2 + 30, [{ t: 'Δ', it: false }, 'd'], { size: 44, fill: COL.green });
    readout(dyn, [`A (1 ; ${fr(d(TA))})   B (${fr(tb)} ; ${fr(d(tb), 1)})   Δt = ${fr(dt)} s   Δd = ${fr(dd, 1)} m`, `sécante : Δd/Δt = ${fr(sl, 1)} m/s   tangente en A : ${fr(m, 1)} m/s`], 615, 24);
  };
  const inp = slider(el, { label: 'Instant de B', min: 1.1, max: 2.3, step: 0.05, value: TB0, unit: 's', onInput: draw });
  resetButton(el, () => { inp.value = TB0; inp.dispatchEvent(new Event('input')); });
}
