import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for x0, sg, lab in ((2, r'$=$', r'$2n-30=0$'), (46, r'$<$', r'$2n-30<0$')):
    box(ax, x0, 54, 15, 12, 'varie', label=r'$6n+40$', size='s')
    text(ax, x0 + 20, 60, sg, 'varie', 'xl', weight='bold')
    box(ax, x0 + 25, 54, 15, 12, 'fixe', label=r'$4n+70$', size='s')
    arrow(ax, (x0 + 20, 52), (x0 + 20, 38), 'varie')
    box(ax, x0 + 3, 25, 34, 12, 'sujet', label=lab, size='m')
text(ax, 44, 45, r'retirer $4n+70$ des deux côtés', 'varie', 's')
box(ax, 8, 4, 72, 12, 'sujet', label='mêmes étapes, seul le signe change', size='m')
save(fig, '15-135')
