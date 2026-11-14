import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
pts = [5, 2, 4, 1]; tot = [5, 7, 11, 12]
text(ax, 10, 50, 'points', 'varie', 's'); text(ax, 10, 10, 'totaux', 'resultat', 's')
for i in range(4):
    x = 22 + 16 * i
    box(ax, x, 46, 14, 8, 'varie', label=str(pts[i]))
    box(ax, x, 28, 14, 8, 'sujet', label=f'n° {i}')
    box(ax, x, 6, 14, 8, 'resultat', label=str(tot[i]))
    arrow(ax, (x + 7, 46), (x + 7, 36.5), 'fixe', lw=0.6)
    arrow(ax, (x + 7, 28), (x + 7, 14.5), 'fixe', lw=0.6)
    if i < 3: arrow(ax, (x + 14.5, 32), (x + 15.5, 32), 'sujet', lw=0.8)
save(fig, '80-273')
