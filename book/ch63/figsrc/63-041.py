import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$|G|$ : un ensemble devient un nombre', 'fixe', 's')
box(ax, 3, 36, 34, 18, 'sujet')
for x, l in zip([14, 28], ['1', r'$\sigma$']):
    disc(ax, x, 45, 5, 'sujet', label=l)
arrow(ax, (39, 45), (56, 45), 'varie')
box(ax, 58, 39, 26, 12, 'resultat', label=r'$|G|=2$')
box(ax, 3, 8, 46, 18, 'autre')
for x, l in zip([12, 22.5, 33, 43.5], ['1', r'$\sigma$', r'$\tau$', r'$\sigma\tau$']):
    disc(ax, x, 17, 4.5, 'autre', label=l, size='s')
arrow(ax, (51, 17), (56, 17), 'varie')
box(ax, 58, 11, 26, 12, 'resultat', label=r'$|G|=4$')
save(fig, '63-041')
