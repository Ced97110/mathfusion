import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 8; O = (10, 18)
P = lambda x, y: (O[0] + x * u, O[1] + y * u)
line(ax, [P(0, 0), P(3, 4)], 'fixe', dash=True); line(ax, [P(0, 0), P(5, 4)], 'limite', dash=True)
line(ax, [P(3, 4), P(5, 0)], 'sujet', lw=1.3); line(ax, [P(5, 4), P(7, 0)], 'varie', lw=1.3)
arrow(ax, P(3.2, 4), P(4.8, 4), 'varie', lw=0.8); arrow(ax, P(5.2, 0), P(6.8, 0), 'varie', lw=0.8)
for (x, y), r in [((3, 4), 'sujet'), ((5, 0), 'sujet'), ((5, 4), 'varie'), ((7, 0), 'varie')]:
    disc(ax, *P(x, y), 1.1, r)
text(ax, P(3, 4)[0], 54, '(3, 4)', 'sujet', 's'); text(ax, P(5, 4)[0], 54, '(5, 4)', 'varie', 's')
text(ax, P(5, 0)[0], 13.5, '(5, 0)', 'sujet', 's'); text(ax, P(7, 0)[0], 13.5, '(7, 0)', 'varie', 's')
text(ax, 44, 7.5, 'distance gardée : √20 et √20', 'resultat', 's')
text(ax, 44, 3.5, 'longueur changée : 5 → √41', 'limite', 's')
save(fig, '73-087')
