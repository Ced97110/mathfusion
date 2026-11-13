import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 6, 82, 36, 0, 42, step=1, labels=True, every=10, arrow_right=False)
for v in (5, 7, 12, 40):
    disc(ax, f(v), 36, 1.2, 'sujet')
disc(ax, f(5), 36, 2.2, 'resultat', fill=False)
text(ax, f(5) + 12, 43, '5 : la plus à gauche', 'resultat', 'm')
numberline(ax, 6, 82, 16, 0, 42, step=1, labels=True, every=100, arrow_right=False)
line(ax, [(6, 20), (79, 20)], 'varie', dash=True)
arrow(ax, (79, 20), (82, 20), 'varie')
text(ax, 84, 24, '?', 'limite', 'l')
text(ax, 44, 8, 'rien de colorié : aucune', 'limite', 'm')
save(fig, '01-154')
