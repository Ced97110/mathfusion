// Test of the interactive figures of « Avant l'apprentissage automatique » in a real browser.
// For each figure: (1) the first state shows the numbers of the book caption (values copied from
// the captions, not from the modules); (2) sliders are locked until the reader predicts;
// (3) everything works with the keyboard alone: answer, move a slider, go back to the book state;
// (4) no console error.
//
// Usage: build the site (out/), serve it, then
//   PW=<path to playwright-core/index.mjs> node tools/ml/test_figures.mjs http://localhost:8000
// playwright-core drives the installed Google Chrome (no browser download):
//   npm i --no-save --prefix <dir> playwright-core
const pw = await import(process.env.PW || 'playwright-core');
const BASE = process.argv[2] || 'http://localhost:8000';

const FIGS = {
  'c002/p0090_3': {
    page: '002', state: { m: 2, B: [-1, -3], hits: true },
    texts: ['m = 0,75', 'm = 5', 'm = −1', 'm = 2', 'A', 'B'],
  },
  'c002/p0092_4': {
    page: '002', state: { base: 1.5, height: 3, ratio: 2 },
    texts: ['petit triangle : 3 / 1,5 = 2', 'grand triangle : 6 / 3 = 2', 'base BC = 3', 'CA = 6', 'base 1,5', 'hauteur 3'],
  },
  'c002/p0100_8': {
    page: '002', state: { B: [-1, -3], rise: -6, run: -3, m: 2, b: -1 },
    texts: ['m = (−6)/(−3) = 2', 'b = −1', 'θ = 63,4°', 'b₂ − a₂ = −3 − 3 = −6', 'course b₁ − a₁ = −1 − 2 = −3', 'A = (2 ; 3)', 'B = (−1 ; −3)'],
  },
  'c002/p0116_27': {
    page: '002', state: { b: 1, mg: -2 },
    texts: ['y = 2x + 1', 'y = 2x', 'y = 2x − 1', 'b = 1', 'b = 0', 'b = −1', 'f(x) = 2x − 1 : monte', 'g(x) = −2x − 1 : descend', '(1 ; 1)', '(1 ; −3)', 'pentes 2 et −2'],
  },
};

const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
let failures = 0;
const check = (ok, msg) => { console.log(`${ok ? 'OK  ' : 'ÉCHEC'} ${msg}`); if (!ok) failures++; };

const browser = await pw.chromium.launch({ channel: 'chrome', headless: true });
const page = await browser.newPage({ viewport: { width: 760, height: 1000 } });
const errors = [];
page.on('console', (m) => m.type() === 'error' && !m.text().startsWith('Failed to load resource') && errors.push(m.text()));
page.on('response', (r) => r.status() >= 400 && errors.push(`${r.status()} ${r.url()}`));
page.on('pageerror', (e) => errors.push(String(e)));

for (const [id, exp] of Object.entries(FIGS)) {
  await page.goto(`${BASE}/apprentissage/${exp.page}/`);
  const img = page.locator(`img[src="/ml/img/${id}.svg"]`);
  await img.scrollIntoViewIfNeeded();
  const box = page.locator(`img[src="/ml/img/${id}.svg"] + .fi`);
  await box.locator('svg[data-state]').waitFor({ timeout: 10000 });
  const svg = box.locator('svg');
  const state = JSON.parse(await svg.getAttribute('data-state'));
  check(same(state, exp.state), `${id} état de départ ${JSON.stringify(state)}`);
  const texts = await svg.locator('text').allTextContents();
  const missing = exp.texts.filter((t) => !texts.includes(t));
  check(!missing.length, `${id} nombres de la légende${missing.length ? ' ; manquants : ' + missing.join(' | ') : ''}`);
  check(await img.evaluate((n) => n.classList.contains('fi-done')), `${id} image du livre remplacée`);
  const sliders = box.locator('input[type=range]');
  const n = await sliders.count();
  const locked = await sliders.evaluateAll((l) => l.every((i) => i.disabled));
  check(n > 0 && locked, `${id} ${n} curseur(s) bloqué(s) avant la prédiction`);
  // keyboard only: focus the first choice, answer with Enter
  await box.locator('.fi-qb').first().focus();
  await page.keyboard.press('Enter');
  check(await sliders.evaluateAll((l) => l.every((i) => !i.disabled)), `${id} curseurs libres après la réponse`);
  check((await box.locator('.fi-qr').textContent()).length > 20, `${id} explication affichée`);
  // move the first slider with the arrow keys
  await sliders.first().focus();
  const before = await svg.getAttribute('data-state');
  await page.keyboard.press('ArrowLeft');
  await page.keyboard.press('ArrowLeft');
  check(before !== (await svg.getAttribute('data-state')), `${id} flèches du clavier : la figure change`);
  // back to the book with the keyboard
  await box.locator('.fi-r').focus();
  await page.keyboard.press('Enter');
  check(same(JSON.parse(await svg.getAttribute('data-state')), exp.state), `${id} retour à la figure du livre`);
}
check(!errors.length, `aucune erreur dans la console${errors.length ? ' : ' + errors.join(' | ') : ''}`);
await browser.close();
console.log(failures ? `${failures} échec(s)` : 'Tous les tests passent.');
process.exit(failures ? 1 : 0);
