import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$V=c\times c\times c=c^3$', 'sujet', 'l')
for c, ox in ((2, 14), (3, 42), (4, 72)):
    cubes(ax, [(i, j, k) for i in range(c) for j in range(c) for k in range(c)], (ox, 16), 3.0, 'sujet')
    text(ax, ox, 48, f'$c={c}$', 'varie', 'm')
    text(ax, ox, 9, f'{c}×{c}×{c} = {c**3}', 'resultat', 's')
save(fig, '11-129')
