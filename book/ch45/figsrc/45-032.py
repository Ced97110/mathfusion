import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 2, 34, 30, 12, 'sujet', label=r'$3+0=3$')
box(ax, 54, 34, 32, 12, 'autre', label=r'$r_3\circ\eta(0)=r_3$', size='s')
arrow(ax, (33, 40), (53, 40), 'varie'); text(ax, 43, 44, r'$\eta$', 'varie', 's')
box(ax, 20, 8, 48, 12, 'varie', label=r'$\eta(0)$ est-il neutre ?', size='s', dash=True)
arrow(ax, (70, 33), (58, 21), 'varie', lw=0.8)
text(ax, 44, 53, 'la condition 2 est-elle utile ?', 'encre', 's')
save(fig, '45-032')
