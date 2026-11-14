// Shared helpers for the interactive figures of the physics book.
// A figure is an ES module in public/physique/fig/cNNN/<name>.js that exports
//   mount(el)  : draws the figure inside the empty <div> el.
// Its first state must show exactly what the PDF figure shows (same values, same labels).
// No dependency: plain SVG + DOM. The static SVG stays in the page as fallback and for print.

const NS = 'http://www.w3.org/2000/svg';

/** Create an SVG element with attributes, optionally appended to parent. */
export function add(parent, tag, attrs = {}, text) {
  const node = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, String(v));
  if (text !== undefined) node.textContent = text;
  if (parent) parent.appendChild(node);
  return node;
}

/** Responsive SVG root of logical size w x h (user units), appended to el. */
export function svg(el, w, h, label) {
  const root = add(null, 'svg', { viewBox: `0 0 ${w} ${h}`, width: '100%', role: 'img', 'aria-label': label || '' });
  root.style.display = 'block';
  root.style.font = '13px Inter, system-ui, sans-serif';
  el.appendChild(root);
  return root;
}

/** Remove every child of a node (used to redraw on each input). */
export function clear(node) {
  while (node.firstChild) node.removeChild(node.firstChild);
}

/**
 * Labelled range input. Native <input type=range> gives keyboard and screen-reader support.
 * onInput(value) is called at once with the initial value, then on every change.
 */
export function slider(el, { label, min, max, step, value, unit = '', format, onInput }) {
  const row = document.createElement('label');
  row.className = 'fi-s';
  const name = document.createElement('span');
  name.textContent = label;
  const input = document.createElement('input');
  Object.assign(input, { type: 'range', min, max, step, value });
  const out = document.createElement('output');
  const show = (v) => (format ? format(v) : String(v).replace('.', ',')) + (unit ? ` ${unit}` : '');
  const update = () => {
    const v = Number(input.value);
    out.textContent = show(v);
    input.setAttribute('aria-valuetext', `${label} ${show(v)}`);
    onInput(v);
  };
  input.addEventListener('input', update);
  row.append(name, input, out);
  el.appendChild(row);
  update();
  return input;
}

/** Button that puts the figure back in the state of the book. */
export function resetButton(el, onReset) {
  const b = document.createElement('button');
  b.type = 'button';
  b.className = 'fi-r';
  b.textContent = 'Revenir à la figure du livre';
  b.addEventListener('click', onReset);
  el.appendChild(b);
  return b;
}

export const reducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/**
 * Orthographic 3D view drawn in SVG, rotated by drag or arrow keys.
 * start = { yaw, pitch } in radians: the orientation of the book figure (yaw 0, pitch 0 = front view:
 * x right, z up, larger y = nearer the reader). Default: the exact isometric view (yaw 45 deg, pitch atan(1/sqrt 2) = 35.264 deg).
 * Escape (or reset()) goes back to start.
 * draw(P) is called on every change; P([x, y, z]) returns [sx, sy, depth] (z up, larger depth = nearer).
 * Draw far things first (sort by depth) for correct overlap.
 */
export function view3d(root, { cx, cy, scale, draw, label, start }) {
  const ISO = start || { yaw: Math.PI / 4, pitch: Math.atan(1 / Math.SQRT2) };
  let { yaw, pitch } = ISO;
  const P = ([x, y, z]) => {
    const cyw = Math.cos(yaw), syw = Math.sin(yaw), cp = Math.cos(pitch), sp = Math.sin(pitch);
    const x1 = x * cyw - y * syw;
    const y1 = x * syw + y * cyw;
    return [cx + scale * x1, cy - scale * (z * cp - y1 * sp), y1 * cp + z * sp];
  };
  const redraw = () => draw(P);
  root.setAttribute('tabindex', '0');
  root.setAttribute('aria-label', `${label || 'Vue en trois dimensions'}. Flèches pour tourner, Échap pour revenir.`);
  root.style.touchAction = 'none';
  root.style.cursor = 'grab';
  let drag = null;
  root.addEventListener('pointerdown', (e) => {
    drag = { x: e.clientX, y: e.clientY, yaw, pitch };
    root.setPointerCapture(e.pointerId);
    root.style.cursor = 'grabbing';
  });
  root.addEventListener('pointermove', (e) => {
    if (!drag) return;
    yaw = drag.yaw + (e.clientX - drag.x) * 0.01;
    pitch = Math.max(-1.5, Math.min(1.5, drag.pitch + (e.clientY - drag.y) * 0.01));
    redraw();
  });
  const end = () => { drag = null; root.style.cursor = 'grab'; };
  root.addEventListener('pointerup', end);
  root.addEventListener('pointercancel', end);
  root.addEventListener('keydown', (e) => {
    const k = { ArrowLeft: [-0.1, 0], ArrowRight: [0.1, 0], ArrowUp: [0, 0.1], ArrowDown: [0, -0.1] }[e.key];
    if (k) { yaw += k[0]; pitch = Math.max(-1.5, Math.min(1.5, pitch + k[1])); redraw(); e.preventDefault(); }
    if (e.key === 'Escape') { ({ yaw, pitch } = ISO); redraw(); }
  });
  redraw();
  return { redraw, reset: () => { ({ yaw, pitch } = ISO); redraw(); } };
}
