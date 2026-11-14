import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# E contient F ; d est dans E hors de F ; d^3 est dans F
box(ax, 2, 6, 84, 58, 'sujet')
text(ax, 44, 68, r'$E=F(d)$ : degré 3, groupe cyclique à 3 éléments', 'sujet', 's')
box(ax, 8, 10, 40, 40, 'fixe')
text(ax, 28, 44, r'$F$', 'fixe', 'l')
disc(ax, 28, 26, 4.2, 'resultat', label=r'$d^3$')
disc(ax, 70, 26, 4.2, 'varie', label=r'$d$')
arrow(ax, (65.3, 28), (32.8, 28), 'varie', curve=0.3)
text(ax, 49, 41, 'puissance 3', 'varie', 's')
text(ax, 70, 15, r'$d$ hors de $F$', 'varie', 's')
text(ax, 28, 14, r'$d^3$ dans $F$', 'resultat', 's')
save(fig, '64-158')
