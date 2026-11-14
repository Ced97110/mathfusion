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
fig, ax = canvas(72)
L = r'$\lambda$'; M1 = '−1'
# left : P, constante
text(ax, 22, 66, r'$P$ inversible', 'sujet', 's')
mat(ax, 22, 56, [['1', '0'], ['2', '1']], 'sujet', cw=8)
text(ax, 22, 44, r'$\det P=1\cdot1-0\cdot2=1$', 'sujet', 's')
# right : lambda 1 - A, polynôme
text(ax, 66, 66, r'$\lambda 1 - A$', 'autre', 's')
mat(ax, 66, 56, [[L, M1], [M1, L]], 'autre', cw=10)
text(ax, 66, 44, r'$\det=\lambda^2-1$', 'autre', 's')
# graphes : constante (plat) et polynôme (courbe)
for cx, role in ((22, 'sujet'), (66, 'autre')):
    line(ax, [(cx - 15, 22), (cx + 15, 22)], 'fixe', lw=0.7)
    line(ax, [(cx, 10), (cx, 34)], 'fixe', lw=0.7)
xs = [i / 20 for i in range(-30, 31)]
line(ax, [(22 + 8 * x, 22 + 7) for x in (-1.5, 1.5)], 'resultat', lw=1.3)
line(ax, [(66 + 8 * x, 22 + 7 * (x * x - 1)) for x in xs], 'varie', lw=1.3)
text(ax, 22, 5, 'constante non nulle', 'resultat', 's')
text(ax, 66, 5, 'polynôme', 'varie', 's')
save(fig, '60-158')
