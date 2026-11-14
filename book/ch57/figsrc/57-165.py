import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
pieces = [(11, r'ann $x$ =', 'sujet', 'annulateur de x'), (31, r'{ $d \in R$', 'fixe', 'les d de R'),
          (47, '|', 'varie', 'tels que'), (66, r'$d\,x = 0$ }', 'resultat', 'd x donne 0')]
for x, t, role, lab in pieces:
    text(ax, x, 50, t, role, 'l', weight='bold')
text(ax, 11, 38, 'annulateur de x', 'sujet', 's')
text(ax, 31, 38, 'les d de R', 'fixe', 's')
text(ax, 47, 38, 'tels que', 'varie', 's')
text(ax, 67, 38, 'd x donne 0', 'resultat', 's')
for x, role in [(11, 'sujet'), (31, 'fixe'), (47, 'varie'), (66, 'resultat')]:
    arrow(ax, (x, 45.5), (x, 41), role, lw=0.9)
text(ax, 44, 26, 'sur l’horloge, x = 4 h :', 'encre', 's')
for i, d in enumerate([3, 6, 9, 12]):
    box(ax, 6 + i * 20.5, 6, 17, 13, 'resultat', label=str(d), size='m')
text(ax, 44, 58, 'ensemble des coefficients d', 'encre', 's')
save(fig, '57-165')
