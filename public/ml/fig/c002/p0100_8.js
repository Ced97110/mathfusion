// Fig. 2.5 : the slope formula. A = (2 ; 3), B = (-1 ; -3), C = (2 ; -3).
// Rise b2 - a2 = -3 - 3 = -6 (blue), run b1 - a1 = -1 - 2 = -3 (red), m = (-6)/(-3) = 2 (green line),
// intercept b = -1 (purple), angle theta = 63,4 deg (orange). Interactive: the coordinates of B.
import { add, svg, clear, slider, resetButton, COL, fr, txt, plane, lineIn, predict, setSlider } from '../lib.js';

const A = [2, 3];
const BOOK = [-1, -3];
const BOX = { xmin: -2.6, xmax: 3.6, ymin: -3.6, ymax: 3.6 };
const sub = (k) => ['₁', '₂'][k - 1];
const par = (v) => (v < 0 ? `(${fr(v)})` : fr(v));

export function mount(el) {
  const lock = predict(el, {
    question: 'on déplace B en (0 ; −3). Que vaut la pente m de la droite AB ?',
    choices: [{ label: '1,5', value: 1.5 }, { label: '2', value: 2 }, { label: '3', value: 3 }, { label: '−3', value: -3 }],
    answer: 3,
    why: 'montée b₂ − a₂ = −3 − 3 = −6, course b₁ − a₁ = 0 − 2 = −2, donc m = (−6)/(−2) = 3.',
    onReveal: () => { setSlider(i1, 0); setSlider(i2, -3); },
  });
  const root = svg(el, 520, 480, 'Figure 2.5. La formule de la pente. A = (2 ; 3) et B = (−1 ; −3). Le trait bleu est la montée, −3 − 3 = −6. Le trait rouge est la course, −1 − 2 = −3. La droite verte a pour pente le quotient, 2, et coupe l’axe vertical en b = −1. Les curseurs déplacent B.');
  const { X, Y } = plane(root, { x0: 190, y0: 225, u: 56, ...BOX });
  const dyn = add(root, 'g');
  let B = [...BOOK];
  const draw = () => {
    clear(dyn);
    const C = [A[0], B[1]];
    const rise = B[1] - A[1], run = B[0] - A[0];
    const vertical = run === 0;
    const m = vertical ? null : rise / run;
    if (!vertical && rise !== 0) {
      const b = A[1] - m * A[0];
      const s = lineIn(m, b, BOX);
      if (s) add(dyn, 'line', { x1: X(s[0][0]), y1: Y(s[0][1]), x2: X(s[1][0]), y2: Y(s[1][1]), stroke: COL.green, 'stroke-width': 2.4 });
      if (b >= BOX.ymin && b <= BOX.ymax) {
        add(dyn, 'circle', { cx: X(0), cy: Y(b), r: 5.5, fill: COL.purple });
        txt(dyn, X(0) + 10, Y(b) - 8, `b = ${fr(b)}`, { fill: COL.purple, size: 16 });
      }
      // angle theta between the horizontal through B (towards C) and the line (towards A)
      const deg = (Math.atan(m) * 180) / Math.PI;
      const r = 26, a0 = run < 0 ? 0 : Math.PI, a1 = Math.atan2(-rise, -run);
      const pt = (a) => `${X(B[0]) + r * Math.cos(a)},${Y(B[1]) - r * Math.sin(a)}`;
      const sweep = Math.sin(a1 - a0) > 0 ? 0 : 1;
      add(dyn, 'path', { d: `M${pt(a0)} A${r},${r} 0 0 ${sweep} ${pt(a1)}`, fill: 'none', stroke: COL.orange, 'stroke-width': 1.8 });
      txt(dyn, 16, 46, `θ = ${fr(deg, 1)}°`, { fill: COL.orange, size: 15 });
    } else if (vertical) {
      add(dyn, 'line', { x1: X(A[0]), y1: Y(BOX.ymin), x2: X(A[0]), y2: Y(BOX.ymax), stroke: COL.green, 'stroke-width': 2.4, 'stroke-dasharray': '6 5' });
    }
    add(dyn, 'line', { x1: X(A[0]), y1: Y(A[1]), x2: X(C[0]), y2: Y(C[1]), stroke: COL.blue, 'stroke-width': 3.2 });
    add(dyn, 'line', { x1: X(B[0]), y1: Y(B[1]), x2: X(C[0]), y2: Y(C[1]), stroke: COL.red, 'stroke-width': 3.2 });
    for (const [p, name, dx, dy] of [[A, `A = (${fr(A[0])} ; ${fr(A[1])})`, -8, -10], [B, `B = (${fr(B[0])} ; ${fr(B[1])})`, -10, -10], [C, 'C', 8, 18]]) {
      add(dyn, 'circle', { cx: X(p[0]), cy: Y(p[1]), r: 5.5, fill: name.startsWith('B') ? COL.red : COL.ink });
      txt(dyn, X(p[0]) + dx, Y(p[1]) + dy, name, { size: 16, anchor: dx < 0 ? 'end' : 'start' });
    }
    txt(dyn, X(2.15), Y(-1.2), 'montée', { fill: COL.blue, size: 13 });
    txt(dyn, X(2.15), Y(-1.55), `b₂ − a₂ = ${fr(B[1])} − ${fr(A[1])} = ${fr(rise)}`, { fill: COL.blue, size: 13 });
    txt(dyn, 16, 440, `course b${sub(1)} − a${sub(1)} = ${fr(B[0])} − ${fr(A[0])} = ${fr(run)}`, { fill: COL.red, size: 14 });
    txt(dyn, 16, 24, vertical
      ? `course = 0 : m = ${fr(rise)}/0 n’existe pas, la droite est verticale.`
      : `m = ${par(rise)}/${par(run)} = ${fr(m)}`, { fill: COL.green, size: 16, weight: 700 });
    txt(dyn, 16, 468, vertical ? 'Deux points l’un au-dessus de l’autre : pas de pente (figure 2.10).'
      : rise === 0 ? 'Montée nulle : la droite est horizontale, m = 0.'
        : `La pente est la montée divisée par la course : ${par(rise)} / ${par(run)} = ${fr(m)}.`, { size: 14 });
    root.dataset.state = JSON.stringify({ B, rise, run, m, b: vertical ? null : A[1] - m * A[0] });
  };
  const i1 = slider(el, { label: 'b₁, abscisse de B', min: -2, max: 3, step: 1, value: BOOK[0], format: (v) => fr(v), onInput: (v) => { B = [v, B[1]]; draw(); } });
  const i2 = slider(el, { label: 'b₂, ordonnée de B', min: -3, max: 3, step: 1, value: BOOK[1], format: (v) => fr(v), onInput: (v) => { B = [B[0], v]; draw(); } });
  lock([i1, i2]);
  resetButton(el, () => { setSlider(i1, BOOK[0]); setSlider(i2, BOOK[1]); });
}
