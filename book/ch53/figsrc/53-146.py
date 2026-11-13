import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$s \equiv m^{d} \ (\mathrm{mod}\ n)$', 'sujet', 'xl')
box(ax, 2, 24, 22, 14, 'sujet', label='Bob')
text(ax, 13, 18, 'seul à pouvoir', 'sujet', 's')
text(ax, 13, 14.5, 'la fabriquer', 'sujet', 's')
arrow(ax, (25, 31), (36, 31), 'varie')
box(ax, 37, 25, 16, 12, 'resultat', label=r'$s$')
text(ax, 45, 20, 'signature', 'resultat', 's')
for i, y in enumerate((38, 27, 16)):
    arrow(ax, (54, 31), (67, y + 3.5), 'fixe', lw=0.7)
    box(ax, 68, y, 18, 7, 'fixe', label='vérifie', size='s')
text(ax, 77, 10, 'tout le monde', 'fixe', 's')
save(fig, '53-146')
