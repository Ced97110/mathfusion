import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, 'chapitre 15', 'fixe', 's')
box(ax, 14, 40, 60, 11, 'sujet', label=r'$4x+8x=12x$')
arrow(ax, (44, 40), (44, 24), 'varie')
text(ax, 48, 32, r'$\sqrt{3}$ joue le rôle de $x$', 'varie', 's', ha='left')
box(ax, 14, 13, 60, 11, 'autre', label=r'$4\sqrt{3}+8\sqrt{3}=12\sqrt{3}$')
save(fig, '22-098')
