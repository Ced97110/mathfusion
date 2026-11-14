import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
for i, (role, sym, l1, l2) in enumerate([('fixe', '0', 'un nombre', 'une quantité'), ('sujet', '∅', 'ensemble vide', '0 objet'), ('fixe', r'$\{a\}$', 'un sac', '1 objet')]):
    x = 2 + i * 28.5
    box(ax, x, 4, 27, 54, role, dash=(i == 1))
    text(ax, x + 13.5, 50, sym, role, 22 if i != 2 else 14, weight='bold')
    text(ax, x + 13.5, 14, l1, role, 's', weight='bold'); text(ax, x + 13.5, 8.5, l2, role, 's')
box(ax, 2 + 28.5 + 6.5, 24, 14, 14, 'sujet', dash=True, fill=False)
box(ax, 2 + 57 + 6.5, 24, 14, 14, 'fixe', fill=False); disc(ax, 2 + 57 + 13.5, 31, 2.5, 'fixe')
f = numberline(ax, 6, 22, 31, 0, 2, labels=False, arrow_right=False); disc(ax, f(0), 31, 1.6, 'fixe')
save(fig, '42-009')
