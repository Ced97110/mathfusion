import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = {3: 14, 15: 44, 27: 74}; y = 42
line(ax, [(6, y), (82, y)], 'fixe')
for v, x in xs.items(): disc(ax, x, y, 4.5, 'sujet', label=str(v))
arrow(ax, (14, y+4.5), (44, y+4.5), 'varie', curve=-0.5); text(ax, 29, y+13, '12', 'varie', 's')
arrow(ax, (44, y+4.5), (74, y+4.5), 'varie', curve=-0.5); text(ax, 59, y+13, '12', 'varie', 's')
arrow(ax, (14, y-4.5), (74, y-4.5), 'autre', curve=0.28); text(ax, 44, y-17, '24', 'autre', 's')
for i, s in enumerate((r'$27-15=12\times 1$', r'$15-3=12\times 1$', r'$27-3=12\times 2$')):
    text(ax, 44, 18 - i*7, s, 'resultat', 's')
save(fig, '43-028')
