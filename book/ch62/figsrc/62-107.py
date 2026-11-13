import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

def grid(x0, role_head, head, bad):
    text(ax, x0 + 20, 62, head, role_head, 'm', weight='bold')
    n = 0
    for r in range(2):
        for c in range(3):
            x = x0 + 2 + c * 12.5; y = 40 - r * 11
            if bad and n == 5:
                box(ax, x, y, 11, 9.5, 'limite', label=r'$x^2+t$', size='s')
            else:
                box(ax, x, y, 11, 9.5, 'resultat')
            n += 1

grid(2, 'sujet', 'ℚ', False)
grid(46, 'autre', r'fractions en $t$, $1+1=0$', True)
text(ax, 44, 27, 'une case = un polynôme irréductible', 'fixe', 's')
box(ax, 2, 6, 38, 11, 'resultat', label='tous séparables', size='s')
box(ax, 46, 6, 40, 11, 'limite', label='un non séparable', size='s')
save(fig, '62-107')
