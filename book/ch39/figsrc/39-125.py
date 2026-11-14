import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 27, 32, 21
def pt(k, r=R):
    a = math.radians(90 - 45 * k); return (cx + r * math.cos(a), cy + r * math.sin(a))
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, zorder=1, ls='--'))
path = [5, 6, 7, 0, 1, 2, 3]
for a, b in zip(path, path[1:]):
    p, q = pt(a), pt(b)
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + 3.8 * ux, p[1] + 3.8 * uy), (q[0] - 3.8 * ux, q[1] - 3.8 * uy), 'varie', lw=1.0)
for k in range(8):
    role = {5: 'sujet', 3: 'resultat'}.get(k, 'fixe')
    x, y = pt(k)
    disc(ax, x, y, 3.4, role, label=str(k), size='m')
text(ax, cx, cy + 3, 'horloge à 8', 'fixe', 's')
text(ax, cx, cy - 3, 'heures', 'fixe', 's')
text(ax, 68, 50, r'$5+6=11=8+3$', 'varie')
text(ax, 68, 40, 'on retire un tour de 8', 'varie', 's')
text(ax, 68, 28, r'$\omega^5\cdot\omega^6=\omega^{11}$', 'sujet')
text(ax, 68, 19, r'$=\omega^3$', 'resultat', 'l')
save(fig, '39-125')
