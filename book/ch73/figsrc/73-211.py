import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
rows = [(40, '(0, 0, 0, 1) et (1, 0, 0, 0)', r'$(-1)\times 1$', r'$-1$'),
        (14, '(0, 0, 0, 2) et (1, 0, 0, 0)', r'$(-4)\times 1$', r'$-4$')]
for y, head, prod, res in rows:
    text(ax, 3, y + 12.5, head, 'sujet', 's', ha='left')
    box(ax, 3, y, 46, 9, 'sujet', label=prod)
    arrow(ax, (49, y + 4.5), (60, y + 4.5), 'varie')
    box(ax, 61, y, 24, 9, 'resultat', label=res, weight='bold')
arrow(ax, (68, 39.5), (68, 23.5), 'varie')
text(ax, 79, 31.5, r'$\times\,2^2$', 'varie', 'm')
box(ax, 3, 1, 82, 8, 'resultat', label='même classe à un carré près', size='s')
save(fig, '73-211')
