import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 2, 44, 38, 20, 'sujet', label=r'$x + y = 5$', size='m')
disc(ax, 15, 49, 2.8, 'sujet'); disc(ax, 27, 49, 2.8, 'autre')
box(ax, 48, 44, 38, 20, 'fixe', label=r'$2x + 2y = 10$', size='m')
for i, r in enumerate(('sujet', 'sujet', 'autre', 'autre')): disc(ax, 55 + i * 8, 49, 2.8, r)
arrow(ax, (40.5, 54), (47.5, 54), 'varie'); text(ax, 44, 59, r'$\times 2$', 'varie', 's')
text(ax, 67, 40, 'répète la première', 'fixe', 's')
box(ax, 8, 22, 72, 10, 'resultat', label='une seule information', size='m')
for x, w, s in ((2, 18, r'$(1,\,4)$'), (22, 18, r'$(2,\,3)$'), (42, 30, r'$(4{,}5\;;\;0{,}5)$'), (74, 12, '…')):
    box(ax, x, 4, w, 11, 'fixe', label=s, size='s')
save(fig, '24-031')
