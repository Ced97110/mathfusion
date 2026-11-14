import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# q = 3 inside the field with 9 elements : keep u if u^3 = u ; i^2 = 2 so i^3 = 2i, different from i
text(ax, 44, 80, r'on teste $u^3 = u$', 'sujet', 'm')
us = ['0', '1', '2', '$i$']
vs = ['0', '1', '2', r'$2i$']
text(ax, 8, 64, '$u$', 'sujet', 's')
text(ax, 8, 40, '$u^3$', 'varie', 's')
for k in range(4):
    x = 20 + k * 17
    ok = k < 3
    box(ax, x, 59, 14, 10, 'sujet', label=us[k], size='s')
    arrow(ax, (x + 7, 58), (x + 7, 51), 'varie')
    box(ax, x, 41, 14, 10, 'resultat' if ok else 'limite', label=vs[k], size='s')
arrow(ax, (20 + 7, 40), (44, 31), 'resultat')
arrow(ax, (20 + 17 + 7, 40), (44, 31), 'resultat')
arrow(ax, (20 + 34 + 7, 40), (44, 31), 'resultat')
box(ax, 14, 18, 60, 12, 'resultat', label=r'gardés : 0, 1 et 2', size='s')
text(ax, 80, 33, 'rejeté', 'limite', 's')
text(ax, 44, 8, r'$\mathbb{F}_3 = \{0, 1, 2\}$', 'resultat', 'm')
save(fig, '67-077')
