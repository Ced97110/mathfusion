import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$\prod\,(r_i-s_j)$', 'sujet', 'xl')
text(ax, 22, 47, r'racines de $f$ : 1 et 2', 'fixe', 's')
text(ax, 66, 47, r'racines de $g$ : 2 et 3', 'autre', 's')
diffs = [(r'$1-2$', r'$-1$'), (r'$1-3$', r'$-2$'), (r'$2-2$', r'$0$'), (r'$2-3$', r'$-1$')]
for i, (d, v) in enumerate(diffs):
    x = 3.5 + i * 21
    text(ax, x + 9, 36, d, 'fixe', 's')
    box(ax, x, 22, 18, 10, 'sujet', label=v, size='l')
brace(ax, 3.5, 84.5, 21, 'fixe', label='on les multiplie tous', down=True)
text(ax, 44, 8, r'$(-1)(-2)\cdot0\cdot(-1)=0$', 'resultat', 'm')
save(fig, '70-065')
