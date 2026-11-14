import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grp(ax, x, y, u, n, role, label=None, h=8):
    box(ax, x, y, n * u, h, role, label=label)
    for i in range(1, n):
        xx = x + i * u
        line(ax, [(xx, y), (xx, y + 1.6)], role, lw=0.6); line(ax, [(xx, y + h - 1.6), (xx, y + h)], role, lw=0.6)

fig, ax = canvas(46)
u, x0 = 8, 26
grp(ax, x0, 33, u, 3, 'sujet', label='3'); grp(ax, x0 + 3 * u, 33, u, 4, 'varie', label='4')
grp(ax, x0, 19, u, 4, 'varie', label='4'); grp(ax, x0 + 4 * u, 19, u, 3, 'sujet', label='3')
text(ax, 13, 37, '3 + 4', 'encre', 'l'); text(ax, 13, 23, '4 + 3', 'encre', 'l')
brace(ax, x0, x0 + 7 * u, 17.5, 'fixe', label='même entier : 7')
text(ax, 44, 6, 'même reste : 2 (mod 5)', 'resultat', 'l')
save(fig, '44-152')
