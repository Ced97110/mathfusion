import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$E\simeq E^\prime$ (isomorphisme fixant $F$)', 'varie', 's')
xs = [8, 34, 60]
for i, x in enumerate(xs):
    box(ax, x, 38, 20, 10, 'sujet', label=r'$x-r_%d$' % (i + 1), size='s')
    box(ax, x, 10, 20, 10, 'autre', label=r'$x-r_%d^\prime$' % (i + 1), size='s')
    arrow(ax, (x + 10, 37), (x + 10, 21), 'varie')
text(ax, 2, 43, '$E$', 'sujet', 'm', ha='left')
text(ax, 2, 15, '$E^\\prime$', 'autre', 'm', ha='left')
text(ax, 44, 52, r'$k_1=k_2=k_3=1$', 'sujet', 's')
text(ax, 44, 4, r'$k_1=k_2=k_3=1$', 'autre', 's')
save(fig, '62-089')
