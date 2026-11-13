import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-032 : b = ‖v‖ sin θ : même forme pour quatre cas ; barres à l'échelle (0,18 mm par unité)
fig, ax = canvas(66)
s = 0.18
x0 = 50
text(ax, 44, 59, r'$b = \|v\| \times \sin\theta$', 'sujet', 'l', weight='bold')
rows = [  # (formule, norme, b)
    ('100 × sin 60° = 86,6', 100, 86.6),
    ('10 × sin 30° = 5', 10, 5.0),
    ('200 × sin 60° = 173,2', 200, 173.2),
    (r'$\|v\|$ × sin 0° = 0', 100, 0.0),
]
y = 47
for lab, n, b in rows:
    text(ax, 3, y, lab, 'encre', 's', ha='left')
    ax.add_patch(Rectangle((x0, y + 0.8), n * s, 2.2, ec=COL['fixe'], fc=FILL['fixe'], lw=0.6, zorder=2))
    if b > 0:
        ax.add_patch(Rectangle((x0, y - 3.0), b * s, 2.2, ec=COL['resultat'], fc=FILL['resultat'], lw=0.6, zorder=2))
    else:
        disc(ax, x0, y - 1.9, 0.7, 'resultat')
    y -= 11
ax.add_patch(Rectangle((50, 3.5), 4, 2.2, ec=COL['fixe'], fc=FILL['fixe'], lw=0.6, zorder=2))
text(ax, 56, 4.6, 'norme', 'fixe', 's', ha='left')
ax.add_patch(Rectangle((68, 3.5), 4, 2.2, ec=COL['resultat'], fc=FILL['resultat'], lw=0.6, zorder=2))
text(ax, 74, 4.6, '$b$', 'resultat', 's', ha='left')
save(fig, '41-032')
