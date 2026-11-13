// Fig. 2.9 : top, y = 2x + 1, y = 2x, y = 2x - 1 (same slope 2, b = 1, 0, -1: parallel).
// Bottom, f(x) = 2x - 1 rises and g(x) = -2x - 1 falls (same b = -1, slopes 2 and -2).
// Interactive: b of the orange line (top) and the slope of g (bottom).
import { add, svg, clear, slider, resetButton, COL, fr, txt, plane, lineIn, predict, setSlider } from '../lib.js';

const BOOK = { b: 1, mg: -2 };
const BOX = { xmin: -3.2, xmax: 3.3, ymin: -3.4, ymax: 3.4 };
const U = 36;
const COLX = 330; // legend column, right of the planes
const eq = (m, b, name = 'y') => {
  const mx = m === 0 ? '' : m === 1 ? 'x' : m === -1 ? '−x' : `${fr(m)}x`;
  if (!mx) return `${name} = ${fr(b)}`;
  return `${name} = ${mx}${b === 0 ? '' : `${b < 0 ? ' − ' : ' + '}${fr(Math.abs(b))}`}`;
};

export function mount(el) {
  const lock = predict(el, {
    question: 'la droite orange devient y = 2x + 3. Où coupe-t-elle l’axe vertical, et reste-t-elle parallèle aux deux autres ?',
    choices: [{ label: 'en 3, parallèle', value: 'a' }, { label: 'en 2, parallèle', value: 'b' }, { label: 'en 3, pas parallèle', value: 'c' }, { label: 'en −3, parallèle', value: 'd' }],
    answer: 'a',
    why: 'pour x = 0, y = 2 × 0 + 3 = 3. La pente reste 2 : changer b déplace la droite sans la tourner.',
    onReveal: () => setSlider(ib, 3),
  });
  const root = svg(el, 520, 540, 'Figure 2.9. En haut : y = 2x + 1, y = 2x et y = 2x − 1 ont la même pente 2, elles sont parallèles et coupent l’axe vertical en 1, 0 et −1. En bas : f(x) = 2x − 1 monte et g(x) = −2x − 1 descend ; elles ont le même b = −1. Un curseur change b pour la droite orange, l’autre change la pente de g.');
  const top = plane(root, { x0: 140, y0: 135, u: U, ...BOX });
  const bot = plane(root, { x0: 140, y0: 400, u: U, ...BOX });
  const draw1 = (pl, m, b, c, p) => {
    const s = lineIn(m, b, BOX);
    if (s) add(p, 'line', { x1: pl.X(s[0][0]), y1: pl.Y(s[0][1]), x2: pl.X(s[1][0]), y2: pl.Y(s[1][1]), stroke: c, 'stroke-width': 2.4 });
  };
  const legend = (p, y, c, a, b) => {
    txt(p, COLX, y, a, { fill: c, size: 14 });
    if (b) txt(p, COLX + 120, y, b, { fill: c, size: 14 });
  };
  const fix = add(root, 'g');
  draw1(top, 2, 0, COL.red, fix);
  draw1(top, 2, -1, COL.blue, fix);
  for (const [b, c] of [[0, COL.red], [-1, COL.blue]]) add(fix, 'circle', { cx: top.X(0), cy: top.Y(b), r: 4.5, fill: c });
  legend(fix, 64, COL.red, 'y = 2x', 'b = 0');
  legend(fix, 86, COL.blue, 'y = 2x − 1', 'b = −1');
  draw1(bot, 2, -1, COL.blue, fix);
  add(fix, 'circle', { cx: bot.X(1), cy: bot.Y(1), r: 4.5, fill: COL.blue });
  txt(fix, bot.X(1) + 8, bot.Y(1) + 4, '(1 ; 1)', { fill: COL.blue, size: 12 });
  legend(fix, 300, COL.blue, 'f(x) = 2x − 1 : monte');
  add(fix, 'circle', { cx: bot.X(0), cy: bot.Y(-1), r: 4.5, fill: COL.ink });
  const dyn = add(root, 'g');
  let b = BOOK.b, mg = BOOK.mg;
  const draw = () => {
    clear(dyn);
    draw1(top, 2, b, COL.orange, dyn);
    add(dyn, 'circle', { cx: top.X(0), cy: top.Y(b), r: 4.5, fill: COL.orange });
    legend(dyn, 42, COL.orange, eq(2, b), `b = ${fr(b)}`);
    const same = b === 0 ? 'confondue avec la rouge' : b === -1 ? 'confondue avec la bleue' : 'b différent : parallèles';
    txt(dyn, COLX, 130, 'même pente m = 2,', { size: 14 });
    txt(dyn, COLX, 150, same, { size: 14 });
    draw1(bot, mg, -1, COL.orange, dyn);
    const y1 = mg - 1;
    if (y1 >= BOX.ymin && y1 <= BOX.ymax) {
      add(dyn, 'circle', { cx: bot.X(1), cy: bot.Y(y1), r: 4.5, fill: COL.orange });
      txt(dyn, bot.X(1) + 8, bot.Y(y1) + 4, `(1 ; ${fr(y1)})`, { fill: COL.orange, size: 12 });
    }
    const way = mg > 0 ? 'monte' : mg < 0 ? 'descend' : 'reste à plat';
    legend(dyn, 322, COL.orange, `${eq(mg, -1, 'g(x)')} : ${way}`);
    txt(dyn, COLX, 395, 'même b = −1,', { size: 14 });
    txt(dyn, COLX, 415, `pentes 2 et ${fr(mg)}`, { size: 14 });
    root.dataset.state = JSON.stringify({ b, mg });
  };
  const ib = slider(el, { label: 'b de la droite orange (en haut)', min: -3, max: 3, step: 0.5, value: BOOK.b, format: (v) => fr(v), onInput: (v) => { b = v; draw(); } });
  const im = slider(el, { label: 'Pente de g (en bas)', min: -3, max: 3, step: 0.5, value: BOOK.mg, format: (v) => fr(v), onInput: (v) => { mg = v; draw(); } });
  lock([ib, im]);
  resetButton(el, () => { setSlider(ib, BOOK.b); setSlider(im, BOOK.mg); });
}
