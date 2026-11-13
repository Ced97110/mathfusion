import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, cx, cy, r, a0, a1, role):
    line(ax, [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(a0, a1 + 1, 2)], role, lw=1.0)
fig, ax = canvas(66)
cx, cy, R = 44, 28, 21
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))
line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5)
line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)
ky = cy + 0.5 * R; dx = R * math.cos(math.radians(30))
line(ax, [(2, ky), (86, ky)], 'varie', lw=1.1)
line(ax, [(cx, cy), (cx + dx, ky)], 'fixe', lw=0.6); line(ax, [(cx, cy), (cx - dx, ky)], 'fixe', lw=0.6)
arc(ax, cx, cy, 9, 0, 30, 'resultat'); arc(ax, cx, cy, 13, 0, 150, 'resultat')
disc(ax, cx + dx, ky, 1.8, 'resultat'); disc(ax, cx - dx, ky, 1.8, 'resultat')
text(ax, cx + dx + 6.5, ky + 3, '30°', 'resultat', 'm'); text(ax, cx - dx - 7.5, ky + 3, '150°', 'resultat', 'm')
text(ax, 77, ky - 3.5, r'$y=0{,}5$', 'varie', 's')
text(ax, 44, 60, 'une droite, deux points', 'resultat', 'l')
save(fig, '32-019')
