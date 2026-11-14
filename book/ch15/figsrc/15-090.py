import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 24, 50, 27, 10, 'autre', label='$c = 3$')
box(ax, 53, 50, 27, 10, 'autre', label='$d = 4$')
box(ax, 2, 32, 20, 14, 'sujet', label='$a = 1$')
box(ax, 2, 16, 20, 14, 'sujet', label='$b = 2$')
for (y, a), vs in (((32, 'a'), (3, 4)), ((16, 'b'), (6, 8))):
    box(ax, 24, y, 27, 14, 'resultat', label=f'${a}c = {vs[0]}$')
    box(ax, 53, y, 27, 14, 'resultat', label=f'${a}d = {vs[1]}$')
text(ax, 44, 6, r'$3 + 6 + 4 + 8 = 21 = 3 \times 7$', 'resultat', 'm')
save(fig, '15-090')
