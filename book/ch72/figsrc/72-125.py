import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 62, 68, '1 case = 1 dimension', 'fixe', 's')
data = [(46, r'$n=2$ : plan entier', 2, 'sujet'), (28, r'$\nu=1$ : maximal', 1, 'resultat'), (10, r'$\{0\}$ : pas maximal', 0, 'limite')]
for y, lab, k, r in data:
    text(ax, 20, y + 7, lab, r, 's')
    for i in range(2):
        if i < k: box(ax, 42 + i * 22, y, 20, 14, r)
        else: box(ax, 42 + i * 22, y, 20, 14, 'fixe', fill=False, dash=True)
save(fig, '72-125')
