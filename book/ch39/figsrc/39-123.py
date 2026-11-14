import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 28, 30, 22
def pt(deg, r=R):
    return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
arrow(ax, (cx - R - 3, cy), (cx + R + 4, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - R - 3), (cx, cy + R + 4), 'fixe', lw=0.6)
for deg, r in [(0, 'fixe'), (45, 'sujet'), (90, 'varie')]:
    q = pt(deg)
    if deg: line(ax, [(cx, cy), q], r, lw=0.8)
    disc(ax, q[0], q[1], 1.3, r)
for a0, a1, r in [(0, 45, 'sujet'), (45, 90, 'varie')]:
    t = [math.radians(a0 + (a1 - a0) * k / 20) for k in range(21)]
    line(ax, [(cx + 9 * math.cos(v), cy + 9 * math.sin(v)) for v in t], r, lw=0.9)
text(ax, pt(0)[0] + 2, cy - 3.5, r'$1$', 'fixe', ha='left')
text(ax, pt(45)[0] + 2.5, pt(45)[1] + 1.5, r'$\omega$', 'sujet', ha='left')
text(ax, pt(90)[0] + 3, pt(90)[1] + 1, r'$\omega^2=i$', 'varie', ha='left')
text(ax, cx + 13, cy + 5, '45°', 'sujet', 's')
text(ax, cx + 4, cy + 14, '45°', 'varie', 's')
text(ax, 71, 52, r'$\omega=\mathrm{cis}\,45^\circ$', 'sujet')
text(ax, 71, 42, r'$(1+i)^2=2i$', 'sujet')
text(ax, 71, 34, r'$2i\div 2=i$', 'varie')
text(ax, 71, 24, r'$\omega^2=i$ : $90^\circ$', 'varie')
save(fig, '39-123')
