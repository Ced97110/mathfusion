import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'mots de 7 bits : $q$ = 0,01 par bit', 'encre', 'm')
S = 80  # mm par unité de probabilité
for y, cap, p, val, role in [(52, 'aucune erreur', 0.932, '0,932', 'sujet'),
                             (33, 'une erreur', 0.066, '0,066', 'varie'),
                             (14, 'deux erreurs ou plus', 0.002, '0,002', 'autre')]:
    text(ax, 4, y, cap, role, 'm', ha='left')
    text(ax, 84, y, r'$\approx$ ' + val, role, 'm', ha='right')
    ax.add_patch(Rectangle((4, y - 9), p * S, 4, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
save(fig, '68-096')
