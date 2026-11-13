import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
x = lambda v: 44 + v * 5.5
text(ax, 44, 77, r'dans $\mathbb{Z}$ avec $+$', 'encre', 's')
text(ax, 44, 69, r'$\mathbb{N}$ : un neutre, des sommes', 'sujet', 's')
for v in range(0, 7):
    disc(ax, x(v), 58, 2.2, 'sujet')
disc(ax, x(-3), 58, 2.2, 'limite', fill=False)
text(ax, x(3), 51, '$3$', 'sujet', 's'); text(ax, x(-3), 51, '$-3$', 'limite', 's')
arrow(ax, (x(3) - 2, 62), (x(-3) + 2, 62), 'limite', curve=0.25)
text(ax, 44, 43, 'pas d’opposé : pas un sous-groupe', 'limite', 's')
text(ax, 44, 33, 'pairs : aussi les opposés', 'resultat', 's')
for v in range(-6, 7, 2):
    disc(ax, x(v), 22, 2.2, 'resultat')
arrow(ax, (x(4) - 1.5, 26), (x(-4) + 1.5, 26), 'resultat', curve=0.25)
text(ax, 44, 9, 'sous-groupe', 'resultat', 'm')
save(fig, '44-107')
