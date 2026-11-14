// Fig. 2.3 : four lines through A = (2 ; 3), slopes 0,75 / 2 / 5 / -1; only m = 2 also goes through B = (-1 ; -3).
// Interactive: the slope of the blue line turns it around A. Question: which slope reaches B = (0 ; 1)?
import { add, svg, clear, slider, resetButton, COL, fr, txt, plane, lineIn, predict, setSlider } from '../lib.js';

const A = [2, 3];
const BOOK = { m: 2, B: [-1, -3] };
const BOX = { xmin: -3.6, xmax: 3.8, ymin: -4.6, ymax: 4.5 };
const FIXED = [
  { m: 0.75, c: COL.orange, dash: '8 5', label: 'm = 0,75', at: [-3.4, 0.5] },
  { m: 5, c: COL.red, dash: '2 4', label: 'm = 5', at: [1, -3.6] },
  { m: -1, c: COL.purple, dash: '10 4 2 4', label: 'm = −1', at: [1.8, 0.4] },
];

export function mount(el) {
  const lock = predict(el, {
    question: 'on déplace B en (0 ; 1). Quelle pente doit avoir la droite bleue, qui tourne autour de A, pour passer par B ?',
    choices: [{ label: '0,75', value: 0.75 }, { label: '1', value: 1 }, { label: '2', value: 2 }, { label: '3', value: 3 }],
    answer: 1,
    why: 'de B à A on monte de 3 − 1 = 2 pour une course de 2 − 0 = 2, donc m = 2/2 = 1.',
    onReveal: () => { B = [0, 1]; setSlider(im, 1); },
  });
  const root = svg(el, 520, 500, 'Figure 2.3. Quatre droites passent par le point A = (2 ; 3) avec les pentes 0,75, 2, 5 et −1. Seule la droite bleue, de pente 2, passe aussi par B = (−1 ; −3). Le curseur fait tourner la droite bleue autour de A.');
  const { X, Y } = plane(root, { x0: 210, y0: 262, u: 48, ...BOX });
  const seg = (m, attrs, p) => {
    const s = lineIn(m, A[1] - m * A[0], BOX);
    if (s) add(p, 'line', { x1: X(s[0][0]), y1: Y(s[0][1]), x2: X(s[1][0]), y2: Y(s[1][1]), 'stroke-width': 2.4, ...attrs });
  };
  const fix = add(root, 'g');
  for (const f of FIXED) {
    seg(f.m, { stroke: f.c, 'stroke-dasharray': f.dash }, fix);
    txt(fix, X(f.at[0]), Y(f.at[1]), f.label, { fill: f.c, size: 14 });
  }
  txt(fix, 16, 20, 'quatre droites par A :', { size: 14 });
  txt(fix, 16, 38, 'une seule passe aussi par B', { size: 14 });
  const dyn = add(root, 'g');
  let m = BOOK.m;
  let B = [...BOOK.B];
  const draw = () => {
    clear(dyn);
    seg(m, { stroke: COL.blue }, dyn);
    const hits = Math.abs(A[1] + m * (B[0] - A[0]) - B[1]) < 1e-9;
    add(dyn, 'circle', { cx: X(B[0]), cy: Y(B[1]), r: 6, fill: COL.red });
    txt(dyn, X(B[0]) - 10, Y(B[1]) + 5, 'B', { fill: COL.red, size: 17, anchor: 'end' });
    add(dyn, 'circle', { cx: X(A[0]), cy: Y(A[1]), r: 6, fill: COL.ink });
    txt(dyn, X(A[0]) + 10, Y(A[1]) - 6, 'A', { size: 17 });
    txt(dyn, X(-1.2), Y(-4.3), `m = ${fr(m)}`, { fill: COL.blue, size: 14 });
    const yAtB = A[1] + m * (B[0] - A[0]);
    txt(dyn, 16, 494, hits
      ? `m = ${fr(m)} : la droite bleue passe par B = (${fr(B[0])} ; ${fr(B[1])}).`
      : `m = ${fr(m)} : en x = ${fr(B[0])}, la droite bleue donne y = ${fr(yAtB)}, pas ${fr(B[1])}. Elle manque B.`,
    { fill: hits ? COL.green : COL.red, size: 14 });
    root.dataset.state = JSON.stringify({ m, B, hits });
  };
  const im = slider(el, { label: 'Pente m de la droite bleue', min: -3, max: 6, step: 0.25, value: BOOK.m, format: (v) => fr(v), onInput: (v) => { m = v; draw(); } });
  lock([im]);
  resetButton(el, () => { B = [...BOOK.B]; setSlider(im, BOOK.m); });
}
