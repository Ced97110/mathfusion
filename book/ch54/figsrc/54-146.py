import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# Rangée 1 : entiers, on compare des nombres
text(ax, 44, 79, 'Entiers : on compare les nombres', 'sujet', 'm')
f = numberline(ax, 8, 70, 62, 0, 20, step=2, every=2, arrow_right=False)
line(ax, [(f(12), 59), (f(12), 68)], 'sujet', lw=1.4)
disc(ax, f(7), 62, 1.6, 'resultat'); disc(ax, f(15), 62, 1.6, 'limite')
text(ax, f(7), 70, r'$7<12$ : accepté', 'resultat', 's')
text(ax, f(15) + 4, 70, r'$15\geq12$ : refusé', 'limite', 's')
text(ax, f(12), 56, 'diviseur 12', 'sujet', 's', ha='center')
# Rangée 2 : polynômes, on compare des degrés
text(ax, 44, 40, 'Polynômes : on compare les degrés', 'autre', 'm')
h = numberline(ax, 12, 60, 24, 0, 3, step=1, arrow_right=False)
line(ax, [(h(1), 21), (h(1), 30)], 'sujet', lw=1.4)
disc(ax, h(0), 24, 1.6, 'resultat'); disc(ax, h(1), 24, 1.6, 'limite')
text(ax, h(0) + 6, 32, r'$r=3$ : degré 0', 'resultat', 's')
text(ax, h(1) + 20, 32, r'$r=2x+1$ : degré 1', 'limite', 's')
text(ax, h(1), 14, r'degré du diviseur $x-1$', 'sujet', 's')
save(fig, '54-146')
