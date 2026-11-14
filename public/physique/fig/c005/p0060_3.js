// Fig. 5.1 : square of side n has area n^2 ("au carré"); the square root goes back. The slider changes the side n.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout } from '../kit.js';

const N0 = 3; // book: side 3, area 9
const SIZE = 223; // px of the square in the book figure (measured); it stays this size, the grid gets finer

/** Text with an optional superscript (sup) part. */
function sup(p, x, y, before, e, after, opt) {
  const t = txt(p, x, y, before, opt);
  add(t, 'tspan', { dy: -opt.size * 0.38, 'font-size': opt.size * 0.62, 'font-style': 'normal' }, e);
  add(t, 'tspan', { dy: opt.size * 0.38, 'font-size': opt.size, 'font-style': 'normal' }, after);
}

export function mount(el) {
  const root = svg(el, 760, 620, 'Figure 5.1. Un carré de côté n est rempli de carreaux : son aire est n au carré. La flèche bleue va du côté à l’aire (au carré), la flèche rouge revient de l’aire au côté (racine).');
  const dyn = add(root, 'g');
  const draw = (n) => {
    clear(dyn);
    const s = SIZE / n, x0 = 133, y0 = 94, a = n * n;
    add(dyn, 'rect', { x: x0, y: y0, width: SIZE, height: SIZE, fill: '#dce6f5' });
    for (let i = 1; i < n; i++) {
      add(dyn, 'line', { x1: x0 + i * s, y1: y0, x2: x0 + i * s, y2: y0 + SIZE, stroke: COL.blue, 'stroke-width': 5 });
      add(dyn, 'line', { x1: x0, y1: y0 + i * s, x2: x0 + SIZE, y2: y0 + i * s, stroke: COL.blue, 'stroke-width': 5 });
    }
    add(dyn, 'rect', { x: x0, y: y0, width: SIZE, height: SIZE, fill: 'none', stroke: COL.blue, 'stroke-width': 5 });
    sup(dyn, 88, 60, 'aire = ' + n, '2', ` = ${a}`, { size: 46, fill: COL.blue, it: false });
    arrow(dyn, [103, y0 + SIZE - 10], [103, y0 + 10], { w: 5, h: 20, both: true });
    txt(dyn, 73, 217, String(n), { size: 46, anchor: 'middle', it: false });
    arrow(dyn, [143, 348], [350, 348], { w: 5, h: 20, both: true });
    txt(dyn, 245, 395, `côté ${n}`, { size: 44, anchor: 'middle', it: false });
    txt(dyn, 548, 82, 'au carré', { size: 38, fill: COL.blue, anchor: 'middle', it: false });
    arrow(dyn, [430, 117], [660, 117], { c: COL.blue, w: 7, h: 26 });
    txt(dyn, 548, 172, `${n} → ${a}`, { size: 42, fill: COL.blue, anchor: 'middle', it: false });
    txt(dyn, 548, 262, 'racine', { size: 38, fill: COL.red, anchor: 'middle', it: false });
    arrow(dyn, [662, 295], [432, 295], { c: COL.red, w: 7, h: 26 });
    const w = String(a).length * 27, tx = 548 - (w + 100) / 2;
    txt(dyn, tx, 362, '√', { size: 46, fill: COL.red, it: false });
    txt(dyn, tx + 30, 362, `${a} = ${n}`, { size: 46, fill: COL.red, it: false });
    add(dyn, 'line', { x1: tx + 29, y1: 322, x2: tx + 30 + w, y2: 322, stroke: COL.red, 'stroke-width': 3 });
    readout(dyn, [`${n} × ${n} = ${a}   et   √${a} = ${n}`], 480, 30);
  };
  const inp = slider(el, { label: 'Côté n', min: 1, max: 6, step: 1, value: N0, onInput: draw });
  resetButton(el, () => { inp.value = N0; inp.dispatchEvent(new Event('input')); });
}
