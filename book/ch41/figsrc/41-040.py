import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-040 : vecteur unitaire = norme 1, même direction. ⟨5 ; −12⟩ (norme 13) et ⟨5/13 ; −12/13⟩ (norme 1), 4 mm par unité
fig, ax = canvas(72)
s = 4.0
C = (30, 62)
arrow(ax, (8, C[1]), (62, C[1]), 'fixe', lw=0.6)
arrow(ax, (C[0], C[1] + 4), (C[0], 6), 'fixe', lw=0.6)
long_end = (C[0] + 5 * s, C[1] - 12 * s)
unit_end = (C[0] + 5 * s / 13, C[1] - 12 * s / 13)
arrow(ax, C, long_end, 'sujet', lw=1.6)
arrow(ax, C, unit_end, 'resultat', lw=2.4)
ax.add_patch(Circle(C, s, ec=COL['resultat'], fc='none', lw=0.7, ls='--', zorder=1))
text(ax, 72, 42, '⟨5 ; −12⟩', 'sujet', 'm')
text(ax, 72, 36, 'norme 13', 'sujet', 'm')
text(ax, 20, 46, '⟨5/13 ; −12/13⟩', 'resultat', 's', ha='center')
text(ax, 20, 41, 'norme 1', 'resultat', 'm')
text(ax, 68, 24, 'même direction', 'fixe', 's')
save(fig, '41-040')
