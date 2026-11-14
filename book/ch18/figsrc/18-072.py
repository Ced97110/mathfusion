import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$p\times q=-6$ : $c$ négatif', 'sujet', 'l')
rows = [(r'$1$ et $-6$', 58), (r'$-1$ et $6$', 48), (r'$2$ et $-3$', 38), (r'$-2$ et $3$', 28)]
for s, y in rows:
    box(ax, 8, y, 34, 8, 'sujet', label=s)
    box(ax, 48, y, 32, 8, 'resultat', label='positif et négatif', size='s')
text(ax, 44, 19, r'$p\times q=6$ : $c$ positif', 'fixe', 'l')
box(ax, 8, 4, 34, 8, 'fixe', label=r'$2$ et $3$')
box(ax, 48, 4, 32, 8, 'fixe', label='positif et positif', size='s')
save(fig, '18-072')
