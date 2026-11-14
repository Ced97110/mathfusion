import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def circ(ax, cx, cy, R):
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))
    line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)
fig, ax = canvas(60)
cx, cy, R = 24, 30, 19
circ(ax, cx, cy, R)
ky = cy + 0.5 * R
dx = R * math.cos(math.radians(30))
line(ax, [(cx - R - 2, ky), (cx + R + 2, ky)], 'varie', lw=1.1)
disc(ax, cx + dx, ky, 1.7, 'sujet'); disc(ax, cx - dx, ky, 1.7, 'resultat')
text(ax, cx + dx + 3.2, ky + 3, r'$P$', 'sujet', 'm')
text(ax, cx - dx - 3.2, ky + 3, r"$P'$", 'resultat', 'm')
text(ax, 58, 46, r'$P$', 'sujet', 'xl'); text(ax, 74, 46, 'premier point', 'sujet', 's')
text(ax, 58, 30, r"$P'$", 'resultat', 'xl')
text(ax, 74, 33, 'second point,', 'resultat', 's'); text(ax, 74, 28, 'même hauteur', 'resultat', 's')
text(ax, 69, 10, "′ = marque, pas un nombre", 'fixe', 's')
save(fig, '32-017')
