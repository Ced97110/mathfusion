import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, x1 = 8, 70
text(ax, 44, 57, 'selon la droite du sol choisie', 'varie', 's')
f = numberline(ax, x0, x1, 40, 0, 60, step=10, arrow_right=False)
for n, v, vs in (('AC', 21.80, '21,80°'), ('AB', 42.03, '42,03°'), ('AD', 56.15, '56,15°')):
    disc(ax, f(v), 40, 1.3, 'varie')
    text(ax, f(v), 46, f'{n} {vs}', 'varie', 's')
line(ax, [(2, 27), (86, 27)], 'fixe', 0.6, dash=True)
text(ax, 44, 22, 'avec le projeté AC', 'resultat', 's')
f2 = numberline(ax, x0, x1, 10, 0, 60, step=10, arrow_right=False)
disc(ax, f2(21.80), 10, 1.8, 'resultat')
text(ax, f2(21.80) + 13, 16, '21,80°, pour tous', 'resultat', 's')
save(fig, '27-048')
