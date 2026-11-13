import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 3.5
def row(y, par):
    x = 4
    box(ax, x, y, 10 * u, 10, 'fixe', label='$10$'); x += 10 * u
    box(ax, x, y, 3 * u, 10, 'varie', label='$3$'); x += 3 * u
    box(ax, x, y, 4 * u, 10, 'varie', label='$4$'); x += 4 * u
    if par: box(ax, 10 * u + 3.5, y - 2, 7 * u + 1, 14, 'sujet', fill=False, dash=True)
    text(ax, 76, y + 5, '= 17', 'resultat', 'l')
row(34, True)
row(10, False)
text(ax, 4, 52, 'avec parenthèses', 'sujet', 's', ha='left')
text(ax, 4, 28, 'sans parenthèses', 'fixe', 's', ha='left')
save(fig, '15-084')
