import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'commutateur de $a$ et $b$', 'encre', 'm')
labs = [(r'$a$', 'sujet'), (r'$b$', 'autre'), (r'$a^{-1}$', 'sujet'), (r'$b^{-1}$', 'autre')]
for i, (l, r) in enumerate(labs):
    x = 6 + i * 20
    box(ax, x, 38, 16, 10, r, label=l, size='l')
    text(ax, x + 8, 32, r'dét $\pm1$', r, 's')
text(ax, 44, 24, r'$a$ et $a^{-1}$ : même signe', 'fixe', 's')
arrow(ax, (44, 20), (44, 15), 'resultat')
box(ax, 14, 2, 60, 12, 'resultat', label=r'dét $=1$ : dans $O^{+}(V,B)$', size='s')
save(fig, '72-151')
