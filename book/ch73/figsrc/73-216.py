import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(42)
cw, ch = 7, 6; mw, mh = 2 * cw, 2 * ch + 2; y = 14
def mat(x, cols, role):
    for j, c in enumerate(cols):
        text(ax, x + cw * (j + 0.5), y + mh / 2, c[0] + '\n' + c[1], role, 'm')
    for sx, d in ((x, 1.2), (x + mw, -1.2)):
        line(ax, [(sx + d, y), (sx, y), (sx, y + mh), (sx + d, y + mh)], role)
def times(cx):
    line(ax, [(cx - 1.4, y + mh / 2 - 1.4), (cx + 1.4, y + mh / 2 + 1.4)], 'fixe')
    line(ax, [(cx - 1.4, y + mh / 2 + 1.4), (cx + 1.4, y + mh / 2 - 1.4)], 'fixe')
xs = [4, 26, 48, 70]
mat(xs[0], [('1', '0'), ('1', '1')], 'varie')
mat(xs[1], [('1', '3'), ('2', '4')], 'sujet')
mat(xs[2], [('1', '−1'), ('0', '1')], 'varie')
mat(xs[3], [('−2', '−1'), ('6', '4')], 'resultat')
times(22); times(44)
for dy in (-1, 1):
    line(ax, [(63, y + mh / 2 + dy), (69, y + mh / 2 + dy)], 'fixe')
for x, lab, r in zip(xs, [r'$P$', r'$M$', r'$R^{-1}$', r'$PMR^{-1}$'], ['varie', 'sujet', 'varie', 'resultat']):
    text(ax, x + mw / 2, y + mh + 5, lab, r, 'm')
text(ax, xs[1] + mw / 2, 7, r'$\det=-2$', 'sujet', 's')
text(ax, xs[3] + mw / 2, 7, r'$\det=-2$', 'resultat', 's')
save(fig, '73-216')
