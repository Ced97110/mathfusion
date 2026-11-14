import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
box(ax, 4, 44, 38, 16, 'sujet', label="$d=1$\n$1\\times9=9$", size='m')
box(ax, 46, 44, 38, 16, 'autre', label="$d=2$\n$-1\\times3=-3$", size='m')
box(ax, 24, 26, 40, 10, 'varie', label=r"$9-3=6$", size='m')
arrow(ax, (23, 44), (36, 36), 'varie'); arrow(ax, (65, 44), (52, 36), 'varie')
box(ax, 14, 6, 60, 12, 'resultat', label=r"$N(2,3)=6/2=3$", size='m')
arrow(ax, (44, 26), (44, 18), 'varie')
save(fig, '80-414')
