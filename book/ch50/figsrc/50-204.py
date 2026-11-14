import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
assert 11 == 3 * 3 + 2 and 1 == 0 * 3 + 1
text(ax, 44, 57, r'$n_3$ divise 11 : 1 ou 11', 'encre', 'm')
text(ax, 24, 49, r'$n_3=11$', 'sujet', 'm'); text(ax, 66, 49, r'$n_3=1$', 'sujet', 'm')
for yb in (38, 31, 24):
    box(ax, 17, yb, 14, 5.5, 'fixe', r=0.5)
    for k in range(3): disc(ax, 20.5 + 3.5 * k, yb + 2.75, 1.2, 'sujet')
for k in range(2): disc(ax, 20.5 + 3.5 * k, 17, 1.3, 'varie')
disc(ax, 66, 17, 1.3, 'varie')
text(ax, 66, 33, 'aucun groupe de 3', 'fixe', 's')
text(ax, 24, 10, r'$11=3\times3+2$', 'encre', 'm'); text(ax, 66, 10, r'$1=0\times3+1$', 'encre', 'm')
text(ax, 24, 3.5, 'reste 2 : exclu', 'limite', 's', weight='bold'); text(ax, 66, 3.5, 'reste 1 : retenu', 'resultat', 's', weight='bold')
save(fig, '50-204')
