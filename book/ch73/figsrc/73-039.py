import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 20, 52, r'$G$ : restes non nuls', 'sujet', 's'); text(ax, 68, 52, r'$H$ : $1$ et $-1$', 'autre', 's')
L = ['1 × 1 = 1', '1 × 2 = 2', '2 × 2 = 1']
R = [r'$1 \times 1 = 1$', r'$1 \times (-1) = -1$', r'$(-1) \times (-1) = 1$']
for k in range(3):
    y = 40 - k*13
    box(ax, 3, y-5, 34, 10, 'sujet', label=L[k]); box(ax, 50, y-5, 36, 10, 'autre', label=R[k], size='s')
    arrow(ax, (38, y), (49, y), 'varie')
text(ax, 44, 4, r'$G \cong H$ : 2 devient $-1$', 'varie', 'm')
save(fig, '73-039')
