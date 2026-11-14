// Fig. 5.2 : thickness 2^n after n folds. The slider moves the red "x2" arrow: bar n is twice bar n-1.
import { svg, add, clear, slider, resetButton } from '../lib.js';
import { COL, txt, arrow, readout } from '../kit.js';

const N0 = 7; // book: arrow from n = 6 (64) to n = 7 (128)
const CX = (n) => 94 + 78.43 * n, H = (n) => 3.83 * 2 ** n, BASE = 545; // px measured on the book figure
const SUP = '⁰¹²³⁴⁵⁶⁷⁸⁹';
const TOP = (n) => BASE - H(n);

export function mount(el) {
  const root = svg(el, 760, 730, 'Figure 5.2. Diagramme en barres : l’épaisseur 2 puissance n après n pliages, de 1 pour n = 0 à 128 pour n = 7. Une flèche rouge « fois 2 » relie la barre n − 1 à la barre n.');
  const fix = add(root, 'g');
  add(fix, 'line', { x1: 36, y1: BASE, x2: 698, y2: BASE, stroke: '#000', 'stroke-width': 4 });
  for (let n = 0; n <= 7; n++) {
    add(fix, 'rect', { x: CX(n) - 27.5, y: TOP(n), width: 55, height: H(n), fill: COL.blue });
    add(fix, 'line', { x1: CX(n), y1: BASE, x2: CX(n), y2: BASE + 10, stroke: '#000', 'stroke-width': 3 });
    txt(fix, CX(n), BASE + 58, String(n), { size: 40, anchor: 'middle', it: false });
    txt(fix, CX(n), TOP(n) - 9, String(2 ** n), { size: n < 4 ? 34 : 36, anchor: 'middle', it: false });
  }
  txt(fix, 368, 650, [{ t: 'n' }, { t: ' (nombre de pliages)', it: false }], { size: 40, anchor: 'middle' });
  const t = txt(fix, 110, 85, [{ t: 'épaisseurs = 2', it: false }], { size: 46, fill: COL.blue });
  add(t, 'tspan', { dy: -17, 'font-size': 29, 'font-style': 'italic' }, 'n');
  const dyn = add(root, 'g');
  const draw = (n) => {
    clear(dyn);
    const s = [CX(n - 1) + 35, TOP(n - 1) - 10], e = [CX(n) - 11, TOP(n) + Math.min(60, H(n) / 2)];
    arrow(dyn, s, e, { c: COL.red, w: 6, h: 24 });
    txt(dyn, (s[0] + e[0]) / 2 - 61, (s[1] + e[1]) / 2 - 37, '×2', { size: 46, fill: COL.red, anchor: 'middle', it: false });
    readout(dyn, [`2${SUP[n]} = 2 × 2${SUP[n - 1]} = 2 × ${2 ** (n - 1)} = ${2 ** n}`], 700, 26);
  };
  const inp = slider(el, { label: 'Pliage n', min: 3, max: 7, step: 1, value: N0, onInput: draw });
  resetButton(el, () => { inp.value = N0; inp.dispatchEvent(new Event('input')); });
}
