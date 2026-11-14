import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'conjuguer un élément de $N$ par $\sigma$', 'encre', 'm')
top = [('1', 'sujet'), ('(1 2 3)', 'sujet'), ('(1 3 2)', 'sujet')]
bot = [('1', 'resultat'), ('3-cycle', 'resultat'), ('3-cycle', 'resultat')]
for i in range(3):
    x = 6 + i * 27
    box(ax, x, 48, 22, 9, top[i][1], label=top[i][0], size='s')
    box(ax, x, 18, 22, 9, bot[i][1], label=bot[i][0], size='s')
    arrow(ax, (x + 11, 47.4), (x + 11, 27.6), 'varie')
text(ax, 15, 37.5, r'$\sigma x\sigma^{-1}$', 'varie', 's', ha='left')
box(ax, 3, 15, 82, 15, 'sujet', fill=False, dash=True, lw=0.7)
text(ax, 44, 7, r'toujours dans $N=A_3$ : normal', 'resultat', 's')
save(fig, '47-173')
