import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'on reçoit 001', 'varie', 'm')
S = 4000  # mm par unité de probabilité
for y, w, role, cap, p, lab in [(36, '000', 'sujet', 'une erreur (bit 3)', 0.0098, r'$\approx$ 0,0098'),
                                (12, '111', 'autre', 'deux erreurs (bits 1, 2)', 0.0001, r'$\approx$ 0,0001')]:
    box(ax, 3, y, 17, 9, role, label=w)
    text(ax, 24, y + 14, cap, role, 's', ha='left')
    ax.add_patch(Rectangle((24, y + 2), p * S, 5, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, 24 + p * S + 2, y + 4.5, lab, role, 's', ha='left')
text(ax, 44, 3, 'environ 100 fois plus probable', 'resultat', 's')
save(fig, '68-095')
