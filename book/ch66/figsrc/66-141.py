import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 8, 54, 72, 9, 'autre', label=r'groupe de Galois $\cong$ $U_n$ (unités)', size='s')
arrow(ax, (44, 54), (44, 48), 'varie')
for n, units, y, lab in [(5, {1, 2, 3, 4}, 24, r'$n=5$ : $\varphi(5)=4$ unités (bleues)'), (6, {1, 5}, 4, r'$n=6$ : $\varphi(6)=2$ unités (bleues)')]:
    text(ax, 2, y + 14, lab, 'encre', 's', ha='left')
    for r in range(n):
        box(ax, 20 + 8 * r, y, 7, 8, 'sujet' if r in units else 'fixe', label=str(r), r=0.5)
save(fig, '66-141')
