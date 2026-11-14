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
fig, ax = canvas(62)
L = r'$\lambda$'; M1 = '−1'
mat(ax, 18, 50, [[L, M1], [M1, L]], 'sujet', cw=10)
text(ax, 18, 40, r'$\lambda 1 - A$', 'sujet', 'm')
text(ax, 60, 54, r'$\det = \lambda\lambda-(-1)(-1)$', 'varie', 's')
text(ax, 60, 46, r'$f(\lambda)=\lambda^2-1$', 'resultat', 'm')
text(ax, 60, 39, 'degré 2', 'resultat', 's')
f = numberline(ax, 12, 76, 16, -2, 2, arrow_right=False)
for v in (-1, 1):
    disc(ax, f(v), 16, 1.6, 'resultat')
    text(ax, f(v), 24, r'$f=0$', 'resultat', 's')
text(ax, 44, 4, 'f s’annule en −1 et en 1', 'resultat', 's')
save(fig, '60-157')
