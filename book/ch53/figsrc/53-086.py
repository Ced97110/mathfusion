import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 14, 52, r'$p$ : secret', 'fixe', 's')
text(ax, 38, 52, r'$q$ : secret', 'fixe', 's')
text(ax, 70, 52, r'$n$ : publié', 'resultat', 's')
for y, (p, q, n) in [(34, (5, 11, 55)), (8, (23, 29, 667))]:
    box(ax, 6, y, 16, 11, 'fixe', fill=False, dash=True, label=str(p))
    text(ax, 26, y + 5.5, r'$\times$', 'encre', 'l')
    box(ax, 30, y, 16, 11, 'fixe', fill=False, dash=True, label=str(q))
    arrow(ax, (49, y + 5.5), (57, y + 5.5), 'varie')
    box(ax, 59, y, 22, 11, 'resultat', label=str(n))
save(fig, '53-086')
