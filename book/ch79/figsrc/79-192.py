import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
A = [(10+6*i, 8+16*i) for i in range(4)]; B = [(36+6*i, 24+16*i) for i in range(4)]
la, lb = ['1','2','4','8'], ['3','6','12','24']
for i in range(3):
    line(ax, [A[i], A[i+1]], 'sujet', lw=1.6); line(ax, [B[i], B[i+1]], 'autre', lw=1.6)
line(ax, [A[0], B[0]], 'fixe', lw=1.2)
for i in range(1, 4): line(ax, [A[i], B[i]], 'fixe', lw=1.2)
for i in range(4):
    disc(ax, *A[i], 4.2, 'sujet', label=la[i]); disc(ax, *B[i], 4.2, 'autre', label=lb[i])
text(ax, 6, 17, r'$\times2$', 'sujet', 's')
text(ax, 24, 14, r'$\times3$', 'fixe', 's')
text(ax, 72, 44, '8 diviseurs', 'encre', 's'); text(ax, 70, 34, 'deux rangées', 'encre', 's')
for _p in ax.patches:
    if isinstance(_p, Circle): _p.set_zorder(3.5)
save(fig, '79-192')
