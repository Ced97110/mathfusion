import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 42, 86, r'Stab $A$ : 2 éléments', 'sujet', 's')
arrow(ax, (30, 79), (54, 79), 'fixe', both=True)
for i, n in enumerate('ABCD'):
    y0 = 60 - i * 12
    box(ax, 30, y0, 12, 12, 'sujet', r=0.3); box(ax, 42, y0, 12, 12, 'sujet', r=0.3)
    text(ax, 22, y0 + 6, n, 'resultat', 'm')
arrow(ax, (62, 24), (62, 72), 'fixe', both=True)
text(ax, 76, 48, 'orbite :\n4 points', 'resultat', 's')
text(ax, 44, 12, r'$4 \times 2 = 8 = |D_4|$', 'encre', 'l')
save(fig, '49-165')
