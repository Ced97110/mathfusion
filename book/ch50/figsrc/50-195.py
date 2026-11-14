import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
R, rd, cy = 13.0, 1.5, 38.0
def pos(cx, v, rad=R):
    a = math.radians(90 - 30 * v); return (cx + rad * math.cos(a), cy + rad * math.sin(a))
def clock(cx, members, role):
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, zorder=1))
    for v in range(12):
        x, y = pos(cx, v)
        if v in members: disc(ax, x, y, rd, role)
        else: ax.add_patch(Circle((x, y), 0.6, ec=COL['fixe'], fc=COL['fixe'], zorder=2))
def shrink(p, q, d):
    L = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / L, (q[1] - p[1]) / L)
    return (p[0] + u[0] * d, p[1] + u[1] * d), (q[0] - u[0] * d, q[1] - u[1] * d)
cl, cr = 22.0, 66.0
clock(cl, {0, 3, 6, 9}, 'sujet'); clock(cr, {0, 2, 4, 6, 8, 10}, 'autre')
text(ax, cl, 57, r'$H$', 'sujet', 'l', weight='bold'); text(ax, cr, 57, r'$K$', 'autre', 'l', weight='bold')
for cx, vs in [(cl, (3, 9)), (cr, (2, 8))]:
    for v in vs:
        x, y = pos(cx, v, R + 4.2); text(ax, x, y, str(v), 'encre', 'm', weight='bold')
p, q = shrink(pos(cl, 3), pos(cl, 9), 2.2); arrow(ax, p, q, 'varie', lw=1.2); text(ax, cl, cy + 3, r'$+6$', 'varie', 'm')
p, q = shrink(pos(cr, 2), pos(cr, 8), 2.2); arrow(ax, p, q, 'varie', lw=1.2); text(ax, cr - 4.5, cy + 4, r'$-6$', 'varie', 'm')
text(ax, 44, 14, r'$3+2=5$', 'resultat', 'm', weight='bold'); text(ax, 44, 7, r'$9+8=17=5$', 'resultat', 'm', weight='bold')
save(fig, '50-195')
