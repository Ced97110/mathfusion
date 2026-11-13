import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grp(ax, x, y, u, n, role, label=None, h=8):
    box(ax, x, y, n * u, h, role, label=label)
    for i in range(1, n):
        xx = x + i * u
        line(ax, [(xx, y), (xx, y + 1.6)], role, lw=0.6); line(ax, [(xx, y + h - 1.6), (xx, y + h)], role, lw=0.6)

fig, ax = canvas(50)
u, x0, y = 8, 4, 26
grp(ax, x0, y, u, 2, 'sujet', label='2'); grp(ax, x0 + 2 * u, y, u, 3, 'varie', label='3'); grp(ax, x0 + 5 * u, y, u, 4, 'autre', label='4')
brace(ax, x0, x0 + 5 * u, y + 8.5, 'fixe', label="2 + 3 d'abord", down=False)
brace(ax, x0 + 2 * u, x0 + 9 * u, y - 0.5, 'fixe', label="3 + 4 d'abord")
text(ax, 80, y + 4, '= 9', 'encre', 'l')
text(ax, 44, 8, '9 : reste 4 (mod 5)', 'resultat', 'l')
save(fig, '44-154')
