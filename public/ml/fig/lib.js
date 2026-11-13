// Helpers for the interactive figures of « Avant l'apprentissage automatique ».
// A figure is an ES module public/ml/fig/cNNN/<band>.js exporting mount(el), listed in index.json.
// Its first state shows exactly the numbers of the book figure (tools/ml/test_figures.mjs checks it).
// Generic DOM helpers come from the physics book; this file adds the book's colours, a graded
// plane, and the « prédis, puis vérifie » question that unlocks the sliders.
import { add, svg, clear, slider, resetButton } from '/physique/fig/lib.js';

export { add, svg, clear, slider, resetButton };

/** Colours measured in the book's figures (role names as in the captions). */
export const COL = {
  ink: '#1e1e1e', blue: '#2d5f8b', orange: '#d98e04', red: '#b5462e', green: '#4a7c3a',
  purple: '#6b4c9a', grey: '#7a7a7a', grid: '#e4dccf', paper: '#fffdf7',
};

/** Decimal comma, at most d decimals, no trailing zeros; true minus sign. */
export const fr = (v, d = 2) => String(+(+v).toFixed(d)).replace('.', ',').replace('-', '−');

/** Plain SVG text. */
export function txt(p, x, y, s, { fill = COL.ink, size = 15, anchor = 'start', weight = 400, it = false } = {}) {
  return add(p, 'text', {
    x, y, fill, 'font-size': size, 'text-anchor': anchor, 'font-weight': weight,
    'font-style': it ? 'italic' : 'normal', 'font-family': '"DejaVu Sans", Inter, system-ui, sans-serif',
  }, s);
}

/**
 * Graded plane like the book's: paper background, grid, axes x and y, integer ticks.
 * Returns X(v), Y(v) (units -> px) and the drawing groups.
 */
export function plane(root, { x0, y0, u, xmin, xmax, ymin, ymax, ticks = true }) {
  const X = (v) => x0 + u * v;
  const Y = (v) => y0 - u * v;
  const g = add(root, 'g');
  add(g, 'rect', { x: X(xmin) - 6, y: Y(ymax) - 6, width: u * (xmax - xmin) + 12, height: u * (ymax - ymin) + 12, fill: COL.paper });
  for (let v = Math.ceil(xmin); v <= xmax; v++) add(g, 'line', { x1: X(v), y1: Y(ymin), x2: X(v), y2: Y(ymax), stroke: COL.grid, 'stroke-width': 1 });
  for (let v = Math.ceil(ymin); v <= ymax; v++) add(g, 'line', { x1: X(xmin), y1: Y(v), x2: X(xmax), y2: Y(v), stroke: COL.grid, 'stroke-width': 1 });
  add(g, 'line', { x1: X(xmin), y1: Y(0), x2: X(xmax) + 8, y2: Y(0), stroke: COL.ink, 'stroke-width': 1.3 });
  add(g, 'line', { x1: X(0), y1: Y(ymin), x2: X(0), y2: Y(ymax) - 8, stroke: COL.ink, 'stroke-width': 1.3 });
  add(g, 'polygon', { points: `${X(xmax) + 14},${Y(0)} ${X(xmax) + 4},${Y(0) - 4} ${X(xmax) + 4},${Y(0) + 4}`, fill: COL.ink });
  add(g, 'polygon', { points: `${X(0)},${Y(ymax) - 14} ${X(0) - 4},${Y(ymax) - 4} ${X(0) + 4},${Y(ymax) - 4}`, fill: COL.ink });
  txt(g, X(xmax) + 6, Y(0) - 10, 'x', { size: 14 });
  txt(g, X(0) + 8, Y(ymax) - 6, 'y', { size: 14 });
  if (ticks) {
    for (let v = Math.ceil(xmin); v <= xmax; v++) if (v) txt(g, X(v), Y(0) + 17, fr(v), { size: 12, anchor: 'middle' });
    for (let v = Math.ceil(ymin); v <= ymax; v++) if (v) txt(g, X(0) - 7, Y(v) + 4, fr(v), { size: 12, anchor: 'end' });
  }
  return { X, Y, g };
}

/** Segment of the line y = m x + b inside [xmin, xmax] x [ymin, ymax], or null. */
export function lineIn(m, b, { xmin, xmax, ymin, ymax }) {
  const pts = [];
  const push = (x, y) => { if (x >= xmin - 1e-9 && x <= xmax + 1e-9 && y >= ymin - 1e-9 && y <= ymax + 1e-9) pts.push([x, y]); };
  push(xmin, m * xmin + b);
  push(xmax, m * xmax + b);
  if (m !== 0) { push((ymin - b) / m, ymin); push((ymax - b) / m, ymax); }
  pts.sort((p, q) => p[0] - q[0]);
  return pts.length >= 2 ? [pts[0], pts[pts.length - 1]] : null;
}

/**
 * « Prédis, puis vérifie » : a question with choices, asked before the sliders work.
 * Any answer (or « Je ne sais pas ») shows whether it was right, the explanation,
 * calls onReveal() to set the figure to the case asked, and enables the controls.
 * Returns lock(inputs): call it with the sliders created after the question.
 */
export function predict(el, { question, choices, answer, why, onReveal }) {
  const box = document.createElement('div');
  box.className = 'fi-q';
  const q = document.createElement('p');
  q.className = 'fi-qt';
  q.textContent = `Prédis, puis vérifie : ${question}`;
  const row = document.createElement('div');
  row.className = 'fi-qc';
  const res = document.createElement('p');
  res.className = 'fi-qr';
  res.setAttribute('aria-live', 'polite');
  box.append(q, row, res);
  el.appendChild(box);
  let inputs = [];
  const buttons = [];
  const reveal = (picked) => {
    for (const b of buttons) b.disabled = true;
    const ok = picked === answer;
    if (picked !== null) buttons.find((b) => b.dataset.v === String(picked)).classList.add(ok ? 'ok' : 'ko');
    buttons.find((b) => b.dataset.v === String(answer))?.classList.add('ok');
    res.textContent = `${picked === null ? 'Réponse' : ok ? 'Juste' : 'Non'} : ${why} Les curseurs sont libres : essaie d’autres valeurs.`;
    for (const i of inputs) i.disabled = false;
    onReveal?.();
  };
  for (const c of choices) {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'fi-qb';
    b.dataset.v = String(c.value);
    b.textContent = c.label;
    b.addEventListener('click', () => reveal(c.value));
    buttons.push(b);
    row.appendChild(b);
  }
  const skip = document.createElement('button');
  skip.type = 'button';
  skip.className = 'fi-qb fi-qs';
  skip.textContent = 'Je ne sais pas';
  skip.addEventListener('click', () => { skip.disabled = true; reveal(null); });
  buttons.push(skip);
  row.appendChild(skip);
  return (list) => {
    inputs = list;
    for (const i of inputs) i.disabled = true;
  };
}

/** Move a slider to v as if the reader did it (fires its onInput). */
export function setSlider(input, v) {
  input.value = v;
  input.dispatchEvent(new Event('input'));
}
