// Fig. 104.2 : pure shear of a cube, in 3D. Opens on the front view of the book. The slider changes theta = delta/l.
import { svg, add, clear, slider, resetButton, view3d } from '../lib.js';
import { COL, txt, arrow, readout, fr, poly } from '../kit.js';

const TH0 = 0.27; // read on the book figure: delta / l = 91 / 332
const L = 333;

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 104.2. Cisaillement pur d’un cube vu de face : la face du haut glisse de δ vers la droite sous la force G, la face du bas est retenue par la force opposée G. L’angle de cisaillement est θ = δ/l. La diagonale rouge D s’allonge, la verte D′ raccourcit. Le cube peut être tourné.');
  const g = add(root, 'g');
  let th = TH0, view;
  const draw = (P) => {
    clear(g);
    const V = (u, v, w) => P([u + th * w - 0.5, v - 0.5, w - 0.5]);
    const U = (u, v, w) => P([u - 0.5, v - 0.5, w - 0.5]); // not sheared
    const S = (a) => a.slice(0, 2);
    const verts = [];
    for (let i = 0; i < 8; i++) verts.push(V(i & 1, (i >> 1) & 1, (i >> 2) & 1));
    const mean = verts.reduce((s, p) => s + p[2], 0) / 8;
    const faces = [[0, 1, 3, 2], [4, 5, 7, 6], [0, 1, 5, 4], [2, 3, 7, 6], [0, 2, 6, 4], [1, 3, 7, 5]]
      .map((f) => ({ f, d: f.reduce((s, i) => s + verts[i][2], 0) })).sort((a, b) => a.d - b.d);
    for (const { f } of faces) add(g, 'polygon', { points: f.map((i) => S(verts[i]).join(',')).join(' '), fill: COL.blue, 'fill-opacity': 0.07 });
    poly(g, [U(0, 1, 0), U(0, 1, 1), U(1, 1, 1), U(1, 1, 0)].map(S), { stroke: COL.grey, 'stroke-width': 6, 'stroke-dasharray': '16 9' });
    const edges = [];
    for (let i = 0; i < 8; i++) for (const b of [1, 2, 4]) if (!(i & b)) edges.push([i, i | b]);
    edges.map((e) => ({ e, d: verts[e[0]][2] + verts[e[1]][2] - 2 * mean })).sort((a, b) => a.d - b.d).forEach(({ e, d }) => {
      add(g, 'line', { x1: verts[e[0]][0], y1: verts[e[0]][1], x2: verts[e[1]][0], y2: verts[e[1]][1], stroke: COL.blue, 'stroke-linecap': 'round', ...(d < -0.05 ? { 'stroke-width': 4, 'stroke-dasharray': '10 9', opacity: 0.6 } : { 'stroke-width': 7 }) }); // hidden edges dashed
    });
    const dg = (a, b, c) => add(g, 'line', { x1: a[0], y1: a[1], x2: b[0], y2: b[1], stroke: c, 'stroke-width': 7 });
    dg(V(0, 1, 0), V(1, 1, 1), COL.red);
    dg(V(0, 1, 1), V(1, 1, 0), COL.green);
    const shift = th - TH0, T1 = U(0.55 + shift, 1, 1.11), T2 = U(0.985 + shift, 1, 1.11), B1 = U(0.724, 1, -0.115), B2 = U(0.294, 1, -0.115);
    arrow(g, S(T1), S(T2), { c: COL.red, w: 7, h: 26 });
    arrow(g, S(B1), S(B2), { c: COL.red, w: 7, h: 26 });
    txt(g, (T1[0] + T2[0]) / 2 - 4, T1[1] - 22, 'G', { size: 56, fill: COL.red, anchor: 'middle' });
    txt(g, (B1[0] + B2[0]) / 2 - 11, B1[1] + 60, 'G', { size: 56, fill: COL.red, anchor: 'middle' });
    const TR = V(1, 1, 1), BR = V(1, 1, 0);
    txt(g, TR[0] + 14, TR[1] + 14, 'D', { size: 54, fill: COL.red });
    txt(g, BR[0] + 14, BR[1] - 6, ['D', '′'], { size: 54, fill: COL.green });
    if (th > 0.06) {
      const d1 = U(0.02, 1, 1.03), d2 = U(th - 0.02, 1, 1.03);
      arrow(g, S(d1), S(d2), { w: 4, h: 16, both: true });
      txt(g, d1[0] - 42, d1[1] - 12, 'δ', { size: 52, anchor: 'middle' });
      const a = Math.atan(th), arc = [];
      for (let i = 0; i <= 10; i++) { const q = (a * i) / 10; arc.push(S(U(0.33 * Math.sin(q), 1, 0.33 * Math.cos(q)))); }
      poly(g, arc, { stroke: '#000', 'stroke-width': 4 });
      const m = U(0.5 * Math.sin(a / 2), 1, 0.5 * Math.cos(a / 2));
      txt(g, m[0], m[1] + 18, 'θ', { size: 52, anchor: 'middle' });
    }
    readout(g, [`θ = δ/l = ${fr(th, 2)} rad`, `D = ${fr(Math.hypot(1 + th, 1))} l   D′ = ${fr(Math.hypot(1 - th, 1))} l`], 612);
  };
  view = view3d(root, { cx: 313.5, cy: 283, scale: L, draw, start: { yaw: 0, pitch: 0 }, label: 'Cube cisaillé en trois dimensions, vu de face comme dans le livre' });
  const inp = slider(el, { label: 'Glissement θ = δ/l', min: 0, max: 0.4, step: 0.01, value: TH0, unit: 'rad', onInput: (v) => { th = v; if (view) view.redraw(); } });
  resetButton(el, () => { inp.value = TH0; th = TH0; view.reset(); });
}
