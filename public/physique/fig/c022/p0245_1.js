// Fig. 22.1 : spring x'' = -x computed step by step (points) against the exact cos t (curve). The slider changes the step epsilon.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const E0 = 0.1, TEND = 2; // book: epsilon = 0.1 s, points up to t = 2 s
const OX = 181, OY = 345, PX = 238.5; // px per second and per unit of x, measured on the book figure
const X = (t) => OX + PX * t, Y = (x) => OY - PX * x;

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 22.1. Position x d’une masse au bout d’un ressort selon le temps t. La courbe bleue est la solution exacte cos t. Les points rouges sont calculés pas à pas : à chaque pas, la force −x change la vitesse, la vitesse change la position. Partie de x = 1 au repos, la masse passe par O vers t = 1,5 s.');
  const fix = add(root, 'g');
  arrow(fix, [OX, 488], [OX, 40], { w: 5, h: 24 });
  arrow(fix, [168, OY], [706, OY], { w: 5, h: 24 });
  txt(fix, 30, 36, [{ t: 'x' }, { t: ' (position)', it: false }], { size: 34 });
  txt(fix, 554, 128, [{ t: 't' }, { t: ' (temps)', it: false }], { size: 34 });
  txt(fix, 130, 118, '1', { size: 38, it: false });
  const pts = []; for (let i = 0; i <= 200; i++) { const t = (TEND * i) / 200; pts.push([X(t), Y(Math.cos(t))]); }
  poly(fix, pts, { stroke: COL.blue, 'stroke-width': 7 });
  txt(fix, 422, 165, [{ t: 'cos ', it: false }, { t: 't' }], { size: 42, fill: COL.blue });
  add(fix, 'circle', { cx: X(Math.PI / 2), cy: OY, r: 9, fill: '#000' });
  txt(fix, 546, 320, 'O', { size: 40 });
  txt(fix, 530, 403, '1,5', { size: 38, it: false });
  const dyn = add(root, 'g');
  const draw = (eps) => {
    clear(dyn);
    const n = Math.floor(TEND / eps + 1e-9);
    let x = 1, v = 0, err = 0;
    const xs = [x];
    v += -x * eps / 2; // half step, as in the book
    for (let i = 1; i <= n; i++) { x += v * eps; xs.push(x); v += -x * eps; }
    xs.forEach((xi, i) => { add(dyn, 'circle', { cx: X(i * eps), cy: Y(xi), r: 7, fill: COL.red }); err = Math.max(err, Math.abs(xi - Math.cos(i * eps))); });
    readout(dyn, [`Pas ε = ${fr(eps, 2)} s : ${n} pas jusqu’à t = ${fr(n * eps, 1)} s`, `départ : v = −x ε/2 (un demi-pas)`, `à chaque pas : x ← x + v ε, puis v ← v − x ε (nouveau x)`, `écart maximal avec cos t = ${fr(err, 3)}`], 580, 26);
  };
  const inp = slider(el, { label: 'Pas ε', min: 0.05, max: 0.3, step: 0.05, value: E0, unit: 's', onInput: draw });
  resetButton(el, () => { inp.value = E0; inp.dispatchEvent(new Event('input')); });
}
