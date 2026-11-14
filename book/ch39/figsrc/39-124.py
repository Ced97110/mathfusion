import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
cx, cy, R = 44, 49, 26
def pt(k, r=R):
    a = math.radians(45 * k); return (cx + r * math.cos(a), cy + r * math.sin(a))
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, zorder=1, ls='--'))
names = [r'$\omega^8=1$', r'$\omega$', r'$\omega^2=i$', r'$\omega^3$', r'$\omega^4=-1$', r'$\omega^5$', r'$\omega^6=-i$', r'$\omega^7$']
for k in range(8):
    p, q = pt(k), pt(k + 1)
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + 2.2 * ux, p[1] + 2.2 * uy), (q[0] - 2.2 * ux, q[1] - 2.2 * uy), 'resultat', lw=0.9)
for k in range(8):
    role = 'sujet' if k % 2 == 1 else 'fixe'
    x, y = pt(k)
    disc(ax, x, y, 1.9, role)
    lx, ly = pt(k, R + 4.5)
    ha = 'left' if math.cos(math.radians(45 * k)) > 0.3 else ('right' if math.cos(math.radians(45 * k)) < -0.3 else 'center')
    if k == 0: lx = x + 3
    if k == 4: lx = x - 3
    text(ax, lx, ly, names[k], role, 's', ha=ha)
box(ax, 2, 2, 40, 7, 'sujet', label='primitives : 45°, 135°…', size='s')
box(ax, 46, 2, 40, 7, 'fixe', label='sur les axes', size='s')
save(fig, '39-124')
