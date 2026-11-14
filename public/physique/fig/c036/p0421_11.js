// Fig. 36.2 : x = cos(w0 t), its slope, the slope of the slope. The slider changes w0.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const W0 = 2; // book: omega_0 = 2 rad/s
const PX = 212 / Math.PI, X0 = 162, AMP = 72, TMAX = (630 - X0) / PX;
const ROWS = [
  { y: 87, c: COL.blue, f: (a) => Math.cos(a), name: 'x' },
  { y: 271, c: COL.green, f: (a) => -Math.sin(a), name: 'ẋ' },
  { y: 456, c: COL.red, f: (a) => -Math.cos(a), name: 'ẍ' },
];

export function mount(el) {
  const root = svg(el, 760, 710, 'Figure 36.2. Trois courbes l’une sous l’autre en fonction du temps : en haut x = cos(ω₀ t), au milieu sa pente ẋ, en bas la pente de la pente ẍ, qui est la courbe du haut retournée. Trois repères verticaux pointillés relient les courbes.');
  const fix = add(root, 'g');
  ROWS.forEach((r) => {
    add(fix, 'line', { x1: X0, y1: r.y, x2: 650, y2: r.y, stroke: '#000', 'stroke-width': 2.5 });
    txt(fix, 66, r.y + 12, r.name, { size: 58, fill: r.c });
  });
  arrow(fix, [168, 548], [642, 548], { w: 5, h: 26 });
  txt(fix, 502, 586, [{ t: 't' }, { t: ' (temps)', it: false }], { size: 42 });
  const dyn = add(root, 'g');

  const draw = (w) => {
    clear(dyn);
    const T = (2 * Math.PI) / w;
    for (const t of [0, T / 4, T / 2]) {
      add(dyn, 'line', { x1: X0 + PX * t, y1: 8, x2: X0 + PX * t, y2: 536, stroke: COL.grey, 'stroke-width': 3.5, 'stroke-dasharray': '3 6' });
    }
    for (const r of ROWS) {
      const pts = [];
      for (let i = 0; i <= 400; i++) { const t = (TMAX * i) / 400; pts.push([X0 + PX * t, r.y - AMP * r.f(w * t)]); }
      poly(dyn, pts, { stroke: r.c, 'stroke-width': 8, 'stroke-linecap': 'round' });
    }
    readout(dyn, [`ω₀ = ${fr(w, 1)} rad/s   T = 2π/ω₀ = ${fr(T)} s`, 'Chaque courbe est dessinée à la même hauteur ; amplitudes :', `x : 1    ẋ : ω₀ = ${fr(w, 1)}    ẍ : ω₀² = ${fr(w * w, 2)}`], 625);
  };
  const inp = slider(el, { label: 'Pulsation ω₀', min: 1, max: 4, step: 0.1, value: W0, unit: 'rad/s', onInput: draw });
  resetButton(el, () => { inp.value = W0; inp.dispatchEvent(new Event('input')); });
}
