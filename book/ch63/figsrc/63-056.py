import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$\sigma$ : $r\mapsto jr$, $j$ reste ; $\tau$ : $j\mapsto j^2$, $r$ reste', 'fixe', 's')
box(ax, 3, 54, 30, 12, 'fixe', label='image de $r$ ↓\nimage de $j$ →', size='s')
box(ax, 36, 54, 22, 12, 'sujet', label=r'$j\mapsto j$', size='s')
box(ax, 60, 54, 22, 12, 'sujet', label=r'$j\mapsto j^2$', size='s')
heads = [r'$r\mapsto r$', r'$r\mapsto jr$', r'$r\mapsto j^2r$']
cells = [['1', r'$\tau$'], [r'$\sigma$', r'$\sigma\tau$'], [r'$\sigma^2$', r'$\sigma^2\tau$']]
for r in range(3):
    y = 40 - 14 * r
    box(ax, 3, y, 30, 12, 'sujet', label=heads[r], size='s')
    for c in range(2):
        box(ax, 36 + 24 * c, y, 22, 12, 'resultat', label=cells[r][c], size='m')
text(ax, 44, 6, r'$3\times2=6$ automorphismes', 'resultat', 'm')
save(fig, '63-056')
