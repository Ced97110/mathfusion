import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c = 9
for i in range(2):
    for j in range(2):
        d = i == j
        box(ax, 5 + j * c, 33 - i * c, c - 0.8, c - 0.8, 'sujet' if d else 'fixe', label='2' if d else '0')
text(ax, 14, 52, 'double le plan', 'sujet', 's')
box(ax, 34, 44, 50, 11, 'limite', label=r'$f=(\lambda-2)^2$')
text(ax, 59, 39.5, 'racine double : test faux', 'limite', 's')
box(ax, 34, 18, 50, 11, 'resultat', label=r'$m=\lambda-2$')
text(ax, 59, 13.5, 'racine simple : test juste', 'resultat', 's')
arrow(ax, (25, 41), (33, 49), 'fixe')
arrow(ax, (25, 38), (33, 24), 'fixe')
save(fig, '60-252')
