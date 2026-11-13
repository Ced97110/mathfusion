import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
u, ox, oy = 18, 10, 8
P = lambda x, y: (ox + u*x, oy + u*y)
fig, ax = canvas(78)
for i in range(4): line(ax, [P(i, 0), P(i, 3)], 'fixe', 0.25)
for j in range(4): line(ax, [P(0, j), P(3, j)], 'fixe', 0.25)
arrow(ax, P(0, 0), P(3.4, 0), 'encre', 0.8); arrow(ax, P(0, 0), P(0, 3.4), 'encre', 0.8)
text(ax, P(3.4, 0)[0] + 3.5, oy, 'x', 'encre', 'm'); text(ax, ox, P(0, 3.4)[1] + 3.5, 'y', 'encre', 'm')
arrow(ax, P(0, 0), P(1, 0), 'varie', 1.8); arrow(ax, P(1, 0), P(1, 1), 'varie', 1.8)
disc(ax, *P(1, 1), 1.9, 'sujet')
text(ax, P(1, 1)[0] + 3, P(1, 1)[1] + 6, 'A (x₁, y₁) = (1, 1)', 'sujet', 'm', ha='left', weight='bold')
text(ax, 66, 50, 'x₁ : 1 à droite', 'varie', 'm', ha='left')
text(ax, 66, 43, 'y₁ : 1 en haut', 'varie', 'm', ha='left')
for v in (1, 2, 3):
    text(ax, P(v, 0)[0], 4, str(v), 'fixe', 's'); text(ax, 6.5, P(0, v)[1], str(v), 'fixe', 's')
save(fig, '37-095')
