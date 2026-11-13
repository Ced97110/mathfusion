import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cx, cy, R = 30, 32, 24
ax.add_patch(Circle((cx, cy), R, ec=COL['sujet'], fc='none', lw=0.9, zorder=1))
arrow(ax, (cx - R - 3, cy), (cx + R + 4, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - R - 3), (cx, cy + R + 4), 'fixe', lw=0.6)
line(ax, [(cx, cy), (cx + R, cy)], 'sujet', lw=1.0)
line(ax, [(cx, cy), (cx, cy + R)], 'resultat', lw=1.0)
disc(ax, cx + R, cy, 1.6, 'sujet'); disc(ax, cx, cy + R, 1.6, 'resultat')
t = [math.radians(90 * k / 24) for k in range(25)]
pts = [(cx + 13 * math.cos(v), cy + 13 * math.sin(v)) for v in t]
line(ax, pts, 'varie', lw=1.0)
arrow(ax, pts[-3], pts[-1], 'varie', lw=1.0)
text(ax, cx + R + 2, cy - 3.5, r'$(1,0)$', 'sujet', 's', ha='left')
text(ax, cx + 4, cy + R + 3.5, r'$(0,1)$', 'resultat', 's', ha='left')
text(ax, cx + 16, cy + 9, '90°', 'varie', 's')
text(ax, cx - 14, cy - 9, r'$\mathbb{T}$', 'sujet', 'l')
text(ax, 74, 52, 'tourner de 90°', 'varie', 's')
text(ax, 74, 45, r'$(1,0)\to(0,1)$', 'varie', 's')
text(ax, 74, 32, r'$1\times\mathrm{cis}\,90^\circ=i$', 'resultat', 's')
text(ax, 74, 20, r'$SO(2)=\mathbb{T}$', 'sujet')
save(fig, '39-141')
