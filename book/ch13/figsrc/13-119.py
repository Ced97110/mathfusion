import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 2, 58, 38, 12, 'sujet', label='anneau commutatif', size='s')
text(ax, 44, 64, '+', 'encre', 'xl')
box(ax, 48, 58, 38, 12, 'varie', label='un ordre', size='m')
arrow(ax, (44, 56), (44, 47), 'resultat')
box(ax, 8, 35, 72, 11, 'resultat', label='anneau commutatif ordonné', size='m')
f = numberline(ax, 8, 70, 14, -3, 3, 1, arrow_right=True)
for v in (-2, 3):
    disc(ax, f(v), 14, 1.7, 'varie')
arrow(ax, (f(-2), 18), (f(3), 18), 'varie', curve=-0.35)
text(ax, (f(-2) + f(3)) / 2, 29, '−2 < 3', 'varie', 'l')
save(fig, '13-119')
