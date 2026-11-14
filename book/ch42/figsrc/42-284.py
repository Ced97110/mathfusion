import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
xs = {v: 30 + 10.5 * (v - 1) for v in range(1, 7)}
for v in range(1, 7): line(ax, [(xs[v], 22), (xs[v], 50)], 'fixe', lw=0.5, dash=True)
text(ax, 2, 44, r'$A\setminus B$', 'sujet', 'l', ha='left'); text(ax, 2, 31, r'$B\setminus A$', 'autre', 'l', ha='left')
for v in (1, 2): disc(ax, xs[v], 44, 3.4, 'sujet', label=str(v))
disc(ax, xs[4], 31, 3.4, 'autre', label='4')
box(ax, 2, 6, 84, 11, 'resultat', label=r'$(A\setminus B)\cap(B\setminus A)=\varnothing$', size='m')
text(ax, 44, 54, r'exemple : $A=\{1,2,3\}$ ; $B=\{3,4\}$', 'fixe', 's')
text(ax, 44, 2.5, 'un cas, pas une preuve', 'limite', 'm', weight='bold')
text(ax, 58, 19.8, 'une colonne = un nombre', 'fixe', 's')
save(fig, '42-284')
