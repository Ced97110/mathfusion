// Fig. 24.2 : charge q1 at P makes a field E; charge q2 at R feels F = q2 E. Sliders change the distance PR and the charge q2.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr } from '../kit.js';

const R0 = 1, Q0 = 1; // book: PR = 1 m, q2 = 1 microcoulomb (q1 = 1 microcoulomb, E = 9000 V/m, F = 0.009 N)
const P = [340, 285], PXM = 241, DIR = [227 / 241, -82 / 241], FPX = 82; // px measured: P, PR = 1 m, direction PR, F arrow at r = 1 m and q2 = 1
const K = 9e9, Q1 = 1e-6;
const si = (v) => (v >= 0.001 ? fr(v, 4) : v.toExponential(1).replace('e-', ' × 10⁻').replace('.', ','));

export function mount(el) {
  const root = svg(el, 760, 640, 'Figure 24.2. La charge q1 en P crée un champ E, des flèches grises dirigées le long du rayon et de plus en plus courtes quand on s’éloigne. Au point R, la charge q2 subit la force F = q2 E, flèche rouge dans la même direction.');
  const fix = add(root, 'g');
  const ring = (t0, t1) => { for (let k = 0; k < 12; k++) { const a = (k * Math.PI) / 6, d = [Math.cos(a), -Math.sin(a)]; arrow(fix, [P[0] + t0 * d[0], P[1] + t0 * d[1]], [P[0] + t1 * d[0], P[1] + t1 * d[1]], { c: COL.grey, w: 4, h: t1 - t0 > 40 ? 17 : 13 }); } };
  ring(73.5, 129.2); ring(180.3, 202.6);
  add(fix, 'circle', { cx: P[0], cy: P[1], r: 20, fill: COL.blue });
  txt(fix, 240, 300, [{ t: 'q' }, { t: '1', sub: true }], { size: 56, fill: COL.blue });
  txt(fix, 362, 275, 'P', { size: 56 });
  txt(fix, 50, 85, 'E', { size: 56, fill: COL.grey });
  arrow(fix, [52, 42], [84, 42], { c: COL.grey, w: 4, h: 12 });
  const dyn = add(root, 'g');
  const draw = (r, q) => {
    clear(dyn);
    const Rp = [P[0] + r * PXM * DIR[0], P[1] + r * PXM * DIR[1]], len = (FPX * q) / (r * r), tip = [Rp[0] + len * DIR[0], Rp[1] + len * DIR[1]];
    arrow(dyn, Rp, tip, { c: COL.red, w: 8, h: 28 });
    add(dyn, 'circle', { cx: Rp[0], cy: Rp[1], r: 17, fill: COL.green });
    txt(dyn, Rp[0] - 17, Rp[1] - 31, [{ t: 'q' }, { t: '2', sub: true }], { size: 56, fill: COL.green });
    txt(dyn, Rp[0] - 5, Rp[1] + 60, 'R', { size: 56 });
    const fx = len < 70 ? tip[0] + 8 : tip[0] - 24;
    txt(dyn, fx, tip[1] - 22, 'F', { size: 56, fill: COL.red });
    arrow(dyn, [fx + 2, tip[1] - 70], [fx + 30, tip[1] - 70], { c: COL.red, w: 4, h: 12 });
    const E = (K * Q1) / (r * r), F = q * 1e-6 * E;
    readout(dyn, [`E = 9 × 10⁹ × 10⁻⁶ ÷ ${fr(r, 1)}² = ${Math.round(E)} V/m`, `F = q₂ E = ${fr(q, 2)} × 10⁻⁶ × ${Math.round(E)} = ${si(F)} N`], 560, 26);
  };
  let r = R0, q = Q0;
  const i1 = slider(el, { label: 'Distance PR', min: 0.9, max: 1.5, step: 0.1, value: R0, unit: 'm', onInput: (x) => { r = x; draw(r, q); } });
  const i2 = slider(el, { label: 'Charge q₂', min: 0.5, max: 1.5, step: 0.25, value: Q0, unit: 'µC', onInput: (x) => { q = x; draw(r, q); } });
  resetButton(el, () => { for (const [i, v] of [[i1, R0], [i2, Q0]]) { i.value = v; i.dispatchEvent(new Event('input')); } });
}
