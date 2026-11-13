import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, R = 38, 40, 23
def pt(deg, r=R):
    a = math.radians(deg); return (cx + r * math.cos(a), cy + r * math.sin(a))
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, zorder=1))
arrow(ax, (cx - R - 4, cy), (cx + R + 4, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - R - 4), (cx, cy + R + 4), 'fixe', lw=0.6)
for deg, role in [(180, 'sujet'), (90, 'resultat'), (270, 'resultat')]:
    disc(ax, *pt(deg), 1.6, role)
t = [math.radians(90 * k / 20) for k in range(21)]
line(ax, [(cx + 9 * math.cos(v), cy + 9 * math.sin(v)) for v in t], 'varie', lw=0.9)
t = [math.radians(90 - 180 * k / 30) for k in range(31)]
line(ax, [(cx + 15 * math.cos(v), cy + 15 * math.sin(v)) for v in t], 'resultat', lw=0.9)
line(ax, [(cx, cy), pt(180)], 'sujet', lw=0.9)
text(ax, cx - R - 3, cy + 4, r'$-1$', 'sujet', ha='right')
text(ax, cx - R - 3, cy - 4, '180°', 'sujet', 's', ha='right')
text(ax, cx + 4, cy + R + 3.5, r'$i$ : 90°', 'resultat', ha='left')
text(ax, cx + 4, cy - R - 3.5, r'$-i$ : 270°', 'resultat', ha='left')
text(ax, cx + 10, cy + 3.5, r'$180^\circ\!/2$', 'varie', 's', ha='left')
text(ax, cx + 17, cy - 6, '+180°', 'resultat', 's', ha='left')
save(fig, '39-132')
