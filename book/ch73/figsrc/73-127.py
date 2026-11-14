import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'$g^{-1}h^{-1}gh$', 'encre', 'l')
text(ax, 16, 40, 'deux translations', 'fixe', 's'); text(ax, 62, 40, 'quart de tour et translation', 'fixe', 's')
A = [(10, 12), (10, 24), (22, 24), (22, 12), (10, 12)]
for a, b in zip(A[:-1], A[1:]):
    d = math.hypot(b[0] - a[0], b[1] - a[1]); k = 1.8 / d
    arrow(ax, (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k), (b[0] - (b[0] - a[0]) * k, b[1] - (b[1] - a[1]) * k), 'varie')
disc(ax, 10, 12, 1.3, 'sujet'); disc(ax, 10, 12, 3.2, 'resultat', fill=False)
text(ax, 16, 6, 'retour en (0, 0)', 'resultat', 's')
B = [(62, 12), (74, 12), (62, 24), (50, 24)]
arrow(ax, (63.8, 12), (72.2, 12), 'varie'); arrow(ax, (73, 13.5), (63, 22.6), 'varie'); arrow(ax, (60.2, 24), (51.8, 24), 'varie')
arrow(ax, (50, 25.8), (72.5, 25.2), 'varie', curve=-0.45)
disc(ax, 62, 12, 1.3, 'sujet'); disc(ax, 74, 24.6, 1.3, 'resultat'); disc(ax, 62, 24, 1, 'fixe'); disc(ax, 50, 24, 1, 'fixe'); disc(ax, 74, 12, 1, 'fixe')
text(ax, 64, 6, 'arrivée en (1, 1)', 'resultat', 's')
save(fig, '73-127')
