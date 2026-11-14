import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Le vent (12,5 ; 21,65 mm) dessiné à deux endroits : même longueur, même direction.
fig, ax = canvas(56)
dx, dy = 12.5, 21.65
P1 = (10, 12)
P2 = (46, 18)
line(ax, [P1, P2], 'fixe', lw=0.7, dash=True)
line(ax, [(P1[0] + dx, P1[1] + dy), (P2[0] + dx, P2[1] + dy)], 'fixe', lw=0.7, dash=True)
arrow(ax, P1, (P1[0] + dx, P1[1] + dy), 'sujet', lw=1.6)
arrow(ax, P2, (P2[0] + dx, P2[1] + dy), 'sujet', lw=1.6)
disc(ax, P1[0], P1[1], 1.3, 'encre')
disc(ax, P2[0], P2[1], 1.3, 'encre')
text(ax, P1[0] + dx + 2, P1[1] + dy / 2, r'$v$', 'sujet', 'm', ha='left')
text(ax, P2[0] + dx + 2, P2[1] + dy / 2, r'$v$', 'sujet', 'm', ha='left')
text(ax, P1[0], 6.5, 'départ 1', 'fixe', 's')
text(ax, P2[0], 12.5, 'départ 2', 'fixe', 's')
box(ax, 62, 4, 24, 11, 'resultat', label='même vecteur')
text(ax, 44, 50, 'mêmes longueur et direction', 'sujet', 's')
save(fig, '41-019')
