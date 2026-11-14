import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
box(ax, 14, 74, 60, 14, 'fixe', label='polynômes en $t$,\ncoefficients modulo $p$', size='s')
arrow(ax, (44, 74), (44, 64), 'varie', lw=1.2)
text(ax, 49, 69, 'faire des quotients', 'varie', 's', ha='left')
box(ax, 2, 8, 84, 55, 'sujet')
text(ax, 44, 58, r'$F=(\mathbb{Z}/p\mathbb{Z})(t)$', 'sujet', 'm', weight='bold')
box(ax, 8, 41, 30, 10, 'encre', label=r'$t$', size='s')
box(ax, 44, 41, 36, 10, 'encre', label=r'$t\,/\,(t+1)$', size='s')
labs = ['1', r'$t$', r'$t^2$', r'$t^3$', '…']
for i, l in enumerate(labs):
    box(ax, 8 + i * 15.5, 22, 12, 9, 'autre', label=l, size='s')
brace(ax, 8, 8 + 4 * 15.5 + 12, 21, 'autre', label='toutes différentes : infini', down=True)
text(ax, 44, 12, r'$p\times1=0$', 'sujet', 's')
save(fig, '62-142')
