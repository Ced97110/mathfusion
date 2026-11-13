import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'racines de $x^2 - 2$', 'sujet', 'm', weight='bold')
xl, xr = 26, 62
top, bot = 58, 22
for y in (top, bot):
    disc(ax, xl, y, 5.2, 'sujet', label=r'$-\sqrt{2}$', size='s')
    disc(ax, xr, y, 5.2, 'sujet', label=r'$\sqrt{2}$', size='s')
line(ax, [(xl - 3, top - 5.2), (xl - 3, bot + 5.2)], 'fixe', lw=1.1)
line(ax, [(xr + 3, top - 5.2), (xr + 3, bot + 5.2)], 'fixe', lw=1.1)
arrow(ax, (xl + 2, top - 5.2), (xr - 2, bot + 5.2), 'varie', lw=1.2)
arrow(ax, (xr - 2, top - 5.2), (xl + 2, bot + 5.2), 'varie', lw=1.2)
text(ax, 5, 40, r'$e$ :', 'fixe', 's', ha='left'); text(ax, 5, 34, 'en place', 'fixe', 's', ha='left')
text(ax, 83, 40, 'échange', 'varie', 's', ha='right')
text(ax, 83, 46, r'$\sigma$ :', 'varie', 's', ha='right')
box(ax, 14, 2, 60, 8, 'resultat', label='une seule orbite : 2 racines', size='s')
save(fig, '49-300')
