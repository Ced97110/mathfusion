import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(78)
ox, oy = 22, 40
arrow(ax, (3, oy), (41, oy), 'sujet', lw=1.4)
arrow(ax, (ox, 14), (ox, 70), 'autre', lw=1.4)
text(ax, 41, oy + 4, r'$U_1$ : carré 1', 'sujet', 's', ha='right')
text(ax, ox + 2, 73, r'$U_2$ : carré $-1$', 'autre', 's', ha='left')
text(ax, 22, 6, 'plan de la seconde mesure', 'fixe', 's')
box(ax, 46, 58, 40, 16, 'limite')
text(ax, 66, 68, r'$U_1$ et $U_2$ : carrés', 'limite', 's')
text(ax, 66, 63, r'1 et $-1$, pas isométriques', 'limite', 's')
arrow(ax, (50, 57.4), (50, 45.6), 'fixe', lw=1.0)
text(ax, 53, 51.5, 'on passe aux orthogonaux', 'fixe', 's', ha='left')
box(ax, 46, 33, 40, 10, 'autre', label=r'$U_1^{\perp}$ : carré $-1$', size='s')
box(ax, 46, 21, 40, 10, 'sujet', label=r'$U_2^{\perp}$ : carré 1', size='s')
text(ax, 66, 14, 'pas isométriques non plus', 'limite', 's', weight='bold')
text(ax, 66, 8, 'la conclusion tombe', 'limite', 's')
save(fig, '72-113')
