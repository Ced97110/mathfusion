import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, 'dans ℝ (caractéristique 0)', 'sujet', 'm')
f = numberline(ax, 10, 70, 32, 0, 3, 1)
for v in (1, 2, 3):
    disc(ax, f(v), 32, 1.3, 'sujet')
disc(ax, f(1 / 3), 32, 1.3, 'varie')
disc(ax, f(2 / 3), 32, 1.3, 'resultat')
text(ax, f(1 / 3) - 1.5, 38, '1/3', 'varie', 's')
text(ax, f(2 / 3) + 2.5, 38, '2/3', 'resultat', 's')
text(ax, 44, 19, '2 = 1 + 1   et   3 = 1 + 1 + 1, non nuls', 'sujet', 's')
text(ax, 44, 12, '1/3 : l’inverse de 3', 'varie', 's')
text(ax, 44, 5, '2/3 = 2 × 1/3', 'resultat', 's')
save(fig, '54-073')
