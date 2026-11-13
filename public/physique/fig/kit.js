// Shared drawing helpers for the interactive figures (colors of the book, text, arrows, readout).
import { add } from './lib.js';

export const COL = { blue: '#1f5fa8', green: '#2e8b57', grey: '#666666', red: '#c0392b', black: '#000' };
const FONT = '"DejaVu Sans", Inter, system-ui, sans-serif';

/** Number with a French decimal comma, d decimals, trailing zeros removed. */
export const fr = (v, d = 2) => String(+v.toFixed(d)).replace('.', ',');

/** SVG text. parts: a string or a list of strings / {t, sub, it}. Italic by default (math letters). */
export function txt(p, x, y, parts, { fill = COL.black, size = 40, anchor = 'start', it = true } = {}) {
  const t = add(p, 'text', { x, y, fill, 'font-size': size, 'text-anchor': anchor, 'font-family': FONT, 'font-style': it ? 'italic' : 'normal' });
  let off = 0;
  for (const part of [].concat(parts)) {
    const o = typeof part === 'string' ? { t: part } : part;
    const want = o.sub ? size * 0.22 : 0;
    const a = { dy: want - off };
    if (o.sub) a['font-size'] = size * 0.62;
    if (o.sub || o.it === false) a['font-style'] = 'normal';
    off = want;
    add(t, 'tspan', a, o.t);
  }
  return t;
}

/** Arrow from a to b (tip at b); both = heads at both ends. */
export function arrow(p, [x1, y1], [x2, y2], { c = COL.black, w = 6, h = 22, both = false } = {}) {
  const a = Math.atan2(y2 - y1, x2 - x1), ca = Math.cos(a), sa = Math.sin(a);
  const head = (x, y, s) => {
    const bx = x - s * h * ca, by = y - s * h * sa;
    add(p, 'polygon', { points: `${x},${y} ${bx - s * 0.4 * h * sa},${by + s * 0.4 * h * ca} ${bx + s * 0.4 * h * sa},${by - s * 0.4 * h * ca}`, fill: c });
    return [bx + s * 0.2 * h * ca, by + s * 0.2 * h * sa];
  };
  const [ex, ey] = head(x2, y2, 1);
  const [sx, sy] = both ? head(x1, y1, -1) : [x1, y1];
  add(p, 'line', { x1: sx, y1: sy, x2: ex, y2: ey, stroke: c, 'stroke-width': w });
}

/** Numbers recomputed from the formulas, one text line each. */
export function readout(p, lines, y0, size = 26) {
  lines.forEach((s, i) => txt(p, 30, y0 + i * (size + 8), s.replace(/ {2,}/g, ' '), { size, fill: '#222', it: false }));
}

/** Polyline path from points. */
export const poly = (p, pts, attrs) => add(p, 'path', { d: pts.map(([x, y], i) => `${i ? 'L' : 'M'}${x.toFixed(1)},${y.toFixed(1)}`).join(''), fill: 'none', ...attrs });
