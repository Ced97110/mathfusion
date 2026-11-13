import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, '2 × 3 = 0', 'resultat', 'xl', weight='bold')
text(ax, 44, 49, '3 sauts de 2 heures', 'encre', 's')
y = 26
f = numberline(ax, 8, 80, y, 0, 6, arrow_right=False)
for i in range(3):
    arrow(ax, (f(2 * i), y + 1.5), (f(2 * i + 2), y + 1.5), 'varie', curve=-0.5)
    text(ax, f(2 * i + 1), y + 10.5, '+2', 'varie', 's', weight='bold')
disc(ax, f(0), y, 1.6, 'sujet')
disc(ax, f(6), y, 1.6, 'resultat')
arrow(ax, (f(6), y - 9), (f(0), y - 9), 'resultat', curve=-0.25)
text(ax, f(3), y - 21, '6 devient 0 : retour au départ', 'resultat', 's')
save(fig, '51-009')
