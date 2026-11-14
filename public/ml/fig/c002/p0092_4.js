// Fig. 2.4 : two right triangles on the line y = 2x - 1. Small (green): base 1,5, height 3.
// Large (B, C, A): base BC = 3, height CA = 6. Same angle theta, same ratio height / base = 2.
// Interactive: the base of the small triangle (apex at A) changes; the ratio stays 2.
import { add, svg, clear, slider, resetButton, COL, fr, txt, plane, lineIn, predict, setSlider } from '../lib.js';

const A = [2, 3], B = [-1, -3], C = [2, -3];
const BOOK = 1.5;
const BOX = { xmin: -2.6, xmax: 3.6, ymin: -3.8, ymax: 3.4 };

export function mount(el) {
  const lock = predict(el, {
    question: 'le petit triangle a maintenant une base de 2,5. Quelle est sa hauteur ?',
    choices: [{ label: '2,5', value: 2.5 }, { label: '4', value: 4 }, { label: '5', value: 5 }, { label: '6', value: 6 }],
    answer: 5,
    why: 'sur cette droite, la hauteur vaut toujours 2 fois la base : 2 × 2,5 = 5. Le rapport 5 / 2,5 = 2 ne dépend pas de la taille.',
    onReveal: () => setSlider(it, 2.5),
  });
  const root = svg(el, 520, 470, 'Figure 2.4. Deux triangles rectangles collés à la droite y = 2x − 1. Le petit, vert, a une base de 1,5 et une hauteur de 3. Le grand, de sommets B, C et A, a une base de 3 et une hauteur de 6. Le rapport hauteur sur base vaut 2 pour les deux. Le curseur change la base du petit triangle.');
  const { X, Y } = plane(root, { x0: 210, y0: 220, u: 56, ...BOX });
  const P = (p) => `${X(p[0])},${Y(p[1])}`;
  const fix = add(root, 'g');
  add(fix, 'polygon', { points: [B, C, A].map(P).join(' '), fill: COL.orange, 'fill-opacity': 0.13 });
  add(fix, 'line', { x1: X(C[0]), y1: Y(C[1]), x2: X(A[0]), y2: Y(A[1]), stroke: COL.orange, 'stroke-width': 2.4, 'stroke-dasharray': '7 5' });
  add(fix, 'line', { x1: X(B[0]), y1: Y(B[1]), x2: X(C[0]), y2: Y(C[1]), stroke: COL.ink, 'stroke-width': 2.4 });
  const s = lineIn(2, -1, BOX);
  add(fix, 'line', { x1: X(s[0][0]), y1: Y(s[0][1]), x2: X(s[1][0]), y2: Y(s[1][1]), stroke: COL.blue, 'stroke-width': 2.4 });
  txt(fix, X(2.15), Y(-1.05), 'hauteur', { fill: COL.orange, size: 14 });
  txt(fix, X(2.15), Y(-1.4), 'CA = 6', { fill: COL.orange, size: 14 });
  txt(fix, X(-0.4), Y(-3.3), 'base BC = 3', { size: 14 });
  for (const [p, name, c, dx] of [[B, 'B', COL.red, -12], [C, 'C', COL.ink, 10], [A, 'A', COL.orange, -12]]) {
    add(fix, 'circle', { cx: X(p[0]), cy: Y(p[1]), r: 5.5, fill: c });
    txt(fix, X(p[0]) + dx, Y(p[1]) + (name === 'C' ? 18 : -6), name, { fill: c, size: 17, anchor: dx < 0 ? 'end' : 'start' });
  }
  const dyn = add(root, 'g');
  let t = BOOK;
  const draw = () => {
    clear(dyn);
    const h = 2 * t;
    const foot = [2 - t, 3 - h], corner = [2, 3 - h];
    add(dyn, 'polygon', { points: [foot, corner, A].map(P).join(' '), fill: COL.green, 'fill-opacity': 0.28, stroke: COL.green, 'stroke-width': 1.5 });
    add(dyn, 'line', { x1: X(foot[0]), y1: Y(foot[1]), x2: X(corner[0]), y2: Y(corner[1]), stroke: COL.green, 'stroke-width': 3 });
    txt(dyn, X(2 - t / 2), Y(corner[1]) - 6, `base ${fr(t)}`, { fill: COL.green, size: 14, anchor: 'middle' });
    txt(dyn, X(2) - 8, Y(3 - h / 2), `hauteur ${fr(h)}`, { fill: COL.green, size: 14, anchor: 'end' });
    txt(dyn, 16, 24, `petit triangle : ${fr(h)} / ${fr(t)} = ${fr(h / t)}`, { size: 15 });
    txt(dyn, 16, 44, 'grand triangle : 6 / 3 = 2', { size: 15 });
    txt(dyn, 16, 462, `Même angle θ : hauteur / base = ${fr(h / t)}, quelle que soit la taille.`, { fill: COL.green, size: 14 });
    root.dataset.state = JSON.stringify({ base: t, height: h, ratio: h / t });
  };
  const it = slider(el, { label: 'Base du petit triangle', min: 0.5, max: 3, step: 0.25, value: BOOK, format: (v) => fr(v), onInput: (v) => { t = v; draw(); } });
  lock([it]);
  resetButton(el, () => setSlider(it, BOOK));
}
