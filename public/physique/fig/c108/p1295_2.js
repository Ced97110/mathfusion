// Fig. 108.1 : circle drawn on a sphere of radius R = 1 m, in 3D. Opens on the book orientation.
// The slider changes r_mes (arc from O along the surface). C = 2 pi R sin(r_mes/R), r_pr = C / 2 pi.
import { svg, add, clear, slider, resetButton, view3d } from '../lib.js';
import { COL, txt, readout, fr, poly } from '../kit.js';

const R0 = 1, MES0 = 0.87, S = 241; // book: sphere of radius 1 m ; MES0 read on the book figure (circle at 50 degrees from O)

export function mount(el) {
  const root = svg(el, 760, 700, 'Figure 108.1. Une sphère avec un cercle rouge C tracé autour du point O, en haut. Le rayon mesuré r_mes est l’arc vert le long de la surface, de O au cercle. Le rayon prédit r_pr = C/2π est le segment bleu, du centre du cercle à son bord, plus court.');
  const g = add(root, 'g');
  let mes = MES0, view;
  const draw = (P) => {
    clear(g);
    const a = mes / R0, z0 = Math.cos(a), rho = Math.sin(a), c0 = P([0, 0, 0]);
    add(g, 'circle', { cx: c0[0], cy: c0[1], r: S, fill: COL.blue, 'fill-opacity': 0.07, stroke: COL.grey, 'stroke-width': 5 });
    const ring = [], mer = [];
    for (let i = 0; i <= 120; i++) { const q = (2 * Math.PI * i) / 120; ring.push(P([rho * Math.cos(q), rho * Math.sin(q), z0])); }
    for (let i = 0; i <= 40; i++) { const b = (a * i) / 40; mer.push(P([-Math.sin(b), 0, Math.cos(b)])); }
    poly(g, ring.map((p) => p.slice(0, 2)), { stroke: COL.red, 'stroke-width': 8, 'stroke-linejoin': 'round' });
    poly(g, mer.map((p) => p.slice(0, 2)), { stroke: COL.green, 'stroke-width': 9, 'stroke-linecap': 'round' });
    const c = P([0, 0, z0]), e = P([-rho, 0, z0]), m = P([-rho / 2, 0, z0]), pole = P([0, 0, 1]), r = P([rho, 0, z0]);
    add(g, 'line', { x1: c[0], y1: c[1], x2: e[0], y2: e[1], stroke: COL.blue, 'stroke-width': 8 });
    add(g, 'circle', { cx: c[0], cy: c[1], r: 9, fill: COL.blue });
    add(g, 'line', { x1: m[0], y1: m[1] + 12, x2: m[0], y2: m[1] + 66, stroke: COL.blue, 'stroke-width': 3 });
    txt(g, m[0], m[1] + 124, ['r', { t: 'pr', sub: true }], { size: 54, fill: COL.blue, anchor: 'middle' });
    add(g, 'circle', { cx: pole[0], cy: pole[1], r: 12, fill: '#000' });
    txt(g, pole[0] + 18, pole[1] - 20, 'O', { size: 54 });
    txt(g, r[0] + 22, r[1] + 20, 'C', { size: 58, fill: COL.red });
    const gm = mer[20];
    txt(g, gm[0] - 66, gm[1] - 30, ['r', { t: 'mes', sub: true }], { size: 54, fill: COL.green, anchor: 'middle' });
    const circ = 2 * Math.PI * R0 * rho, rpr = circ / (2 * Math.PI);
    readout(g, [`r_mes = ${fr(mes)} m   C = ${fr(circ)} m`, `r_pr = C/2π = ${fr(rpr)} m   excès = r_mes − r_pr = ${fr(mes - rpr)} m`], 612);
  };
  view = view3d(root, { cx: 387, cy: 317, scale: S, draw, start: { yaw: 0, pitch: 0.25 }, label: 'Sphère de rayon 1 m avec un cercle tracé autour du point O, en trois dimensions' });
  const inp = slider(el, { label: 'Rayon mesuré r_mes', min: 0.3, max: 1.57, step: 0.01, value: MES0, unit: 'm', onInput: (v) => { mes = v; if (view) view.redraw(); } });
  resetButton(el, () => { inp.value = MES0; mes = MES0; view.reset(); });
}
