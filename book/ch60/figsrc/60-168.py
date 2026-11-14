import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role='encre', size='m', cw=7.0, P=6.0, lw=0.9):
    r = len(rows); c = len(rows[0]); fs = SIZE[size]
    ls = ((P / (0.3387 * fs)) - 0.2) / 0.8
    for j in range(c):
        t = text(ax, cx + (j - (c - 1) / 2) * cw, cy, '\n'.join(rows[i][j] for i in range(r)), role, size); t.set_linespacing(ls)
    hw = c * cw / 2; hh = r * P / 2 + 0.4
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.2, cy - hh)], role, lw=lw)
fig, ax = canvas(76)
box(ax, 14, 44, 60, 28, 'resultat', fill=False, dash=True)
text(ax, 44, 68, r'tout reste dans $\mathbb{Q}$', 'resultat', 's')
mat(ax, 28, 56, [['0', '1'], ['2', '0']], 'resultat', cw=9)
text(ax, 58, 58, r'compagnon de', 'resultat', 's')
text(ax, 58, 53, r'$\lambda^2-2$', 'resultat', 's')
f = numberline(ax, 8, 76, 18, -2, 2, arrow_right=False)
r2 = 2 ** 0.5
for v, s in ((-r2, r'$-\sqrt{2}$'), (r2, r'$\sqrt{2}$')):
    disc(ax, f(v), 18, 1.6, 'autre')
    text(ax, f(v), 25, s, 'autre', 's')
text(ax, 44, 6, r'les racines sont hors de $\mathbb{Q}$', 'autre', 's')
save(fig, '60-168')
