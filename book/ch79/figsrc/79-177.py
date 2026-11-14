import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
P = {'0': (44, 8), 'u': (28, 26), 'v': (28, 44), '1': (44, 62), 'w': (62, 35)}
for a, b in [('0','u'),('u','v'),('v','1')]: line(ax, [P[a], P[b]], 'sujet', lw=1.6)
for a, b in [('0','w'),('w','1')]: line(ax, [P[a], P[b]], 'varie', lw=1.6)
for k, (x, y) in P.items():
    r = {'0':'fixe','1':'fixe','u':'sujet','v':'sujet','w':'varie'}[k]
    disc(ax, x, y, 3.8, r, label=k)
text(ax, 12, 35, '3 marches', 'sujet', 's')
text(ax, 78, 35, '2 marches', 'varie', 's')
text(ax, 44, 35, r'$3\neq2$', 'limite', 'l', weight='bold')
text(ax, 44, 66, 'pentagone', 'fixe', 's')
for _p in ax.patches:
    if isinstance(_p, Circle): _p.set_zorder(3.5)
save(fig, '79-177')
