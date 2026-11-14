import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y, y2 = 52, 22
f = numberline(ax, 14, 54, y, 3, 5, role='sujet')
g = lambda v: 54 - (v - 3) * 20
arrow(ax, (59, y2), (9, y2), 'sujet', lw=0.9)
for v in (3, 4, 5):
    ax.plot([g(v)] * 2, [y2 - 1.2, y2 + 1.2], color=COL['sujet'], lw=0.8)
    text(ax, g(v), y2 - 3.4, str(v), 'sujet', 's')
for v in (3, 5):
    line(ax, [(f(v), y - 6), (g(v), y2 + 4)], 'fixe', dash=True)
disc(ax, f(5), y, 1.8, 'varie')
disc(ax, g(5), y2, 1.8, 'varie')
text(ax, 44, y + 9, 'flèche à droite : 5 à droite de 3', 'sujet', 's')
text(ax, 44, y2 - 9, 'flèche à gauche : 5 à gauche de 3', 'sujet', 's')
text(ax, 44, 4.8, 'même droite, même 5 : les nombres', 'fixe', 's')
text(ax, 44, 1.6, 'grandissent dans le sens de la flèche', 'fixe', 's')
save(fig, '12-013')
