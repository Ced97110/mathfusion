import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 44, 51, 'diviseurs de a = 6', 'encre', 'l')
vals = ['−6', '−3', '−2', '−1', '1', '2', '3', '6']
w, g = 9.0, 1.7
x0 = (88 - (8 * w + 7 * g)) / 2
for i, v in enumerate(vals):
    role = 'fixe' if v in ('6', '−6') else 'sujet'
    box(ax, x0 + i * (w + g), 28, w, 11, role, label=v, size='m')
xa = x0 + 1 * (w + g)
xb = x0 + 6 * (w + g) + w
brace(ax, xa, xb, 26, 'sujet', label='diviseurs propres de 6')
text(ax, x0 + w / 2, 18, 'associé', 'fixe', 's')
text(ax, x0 + 7 * (w + g) + w / 2, 18, 'associé', 'fixe', 's')
text(ax, 44, 4, 'exclus : 6 ∣ 6 et 6 divise aussi −6', 'fixe', 's')
save(fig, '56-041')
