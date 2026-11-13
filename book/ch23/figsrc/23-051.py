import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 2, 62, 38, 12, 'sujet', label=r'$x^2+6x-16=0$'); box(ax, 48, 62, 38, 12, 'autre', label=r'$x^2+10x-11=0$')
text(ax, 21, 56, r'$b=6,\ c=-16$', 'sujet', 's'); text(ax, 67, 56, r'$b=10,\ c=-11$', 'autre', 's')
arrow(ax, (21, 52), (38, 38), 'varie'); arrow(ax, (67, 52), (50, 38), 'varie')
box(ax, 14, 24, 60, 13, 'varie', label=r'$x^2+bx+c=0$   ($a=1$)')
arrow(ax, (44, 23.5), (44, 15.5), 'varie')
box(ax, 8, 2, 72, 13, 'resultat', label='un seul calcul, avec des lettres')
save(fig, '23-051')
