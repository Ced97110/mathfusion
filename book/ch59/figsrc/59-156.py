import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
L = ['diag(1, 20)', r'$\det=1\times20=20$', 'facteurs (1, 20)', r'$\mathbb{Z}/20$']
R = ['diag(2, 10)', r'$\det=2\times10=20$', 'facteurs (2, 10)', r'$\mathbb{Z}/2\oplus\mathbb{Z}/10$']
for k in range(4):
    y = 56 - k * 17
    box(ax, 2, y, 38, 10, 'sujet', label=L[k], size='s')
    box(ax, 48, y, 38, 10, 'autre', label=R[k], size='s')
    if k < 3:
        arrow(ax, (21, y - 0.5), (21, y - 6.5), 'varie')
        arrow(ax, (67, y - 0.5), (67, y - 6.5), 'varie')
text(ax, 44, 44, '=', 'resultat', 'xl', weight='bold')
text(ax, 44, 10, r'$\neq$', 'limite', 'xl', weight='bold')
save(fig, '59-156')
