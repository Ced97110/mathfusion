import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$f=x+1$ : degré 1', 'sujet', 'm')
text(ax, 44, 49, r'$f\,g=1$ donne $1+\deg g=0$', 'encre', 'm')
y = 24
f = lambda v: 22 + (v + 1) / 4 * 48
arrow(ax, (14, y), (80, y), 'fixe', lw=0.9)
for v in range(-1, 4):
    ax.plot([f(v), f(v)], [y - 1.2, y + 1.2], color=COL['fixe'], lw=0.8, zorder=1.5)
    text(ax, f(v), y - 4, ('−1' if v < 0 else str(v)), 'limite' if v < 0 else 'fixe', 's')
disc(ax, f(-1), y, 1.8, 'limite')
for v in (0, 2, 3):
    disc(ax, f(v), y, 1.5, 'resultat')
disc(ax, f(1), y, 1.8, 'sujet')
text(ax, f(-1), 31, 'aucun polynôme', 'limite', 's')
text(ax, f(-1), 27.5, 'de degré −1', 'limite', 's')
arrow(ax, (f(1), 36), (f(0) + 1, 36), 'varie')
text(ax, f(0.5), 40, 'il faudrait −1', 'limite', 's')
text(ax, f(2), 10, 'degrés possibles : 0, 1, 2…', 'resultat', 's')
save(fig, '54-138')
