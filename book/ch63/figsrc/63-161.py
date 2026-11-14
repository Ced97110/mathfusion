import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cx, cy, R = 25, 38, 21
def P(k):
    a = math.radians(90 + 72 * k); return (cx + R * math.cos(a), cy + R * math.sin(a))
def sh(p, q, d):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy); return (p[0] + dx / n * d, p[1] + dy / n * d)
def lab(p, q, rad, off):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2; dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy)
    d = rad * n / 2 + off
    return (mx + d * dy / n, my - d * dx / n)
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, ls='--', zorder=1))
names = ['1', r'$\omega$', r'$\omega^2$', r'$\omega^3$', r'$\omega^4$']
roles = ['fixe', 'sujet', 'fixe', 'varie', 'fixe']
for k in range(5):
    x, y = P(k); disc(ax, x, y, 4.3, roles[k], label=names[k], size='s')
p1, p3 = P(1), P(3)
a, b = sh(p1, p3, 4.8), sh(p3, p1, 4.8)
arrow(ax, a, b, 'varie', curve=0.3)
arrow(ax, b, a, 'sujet', curve=0.3)
x, y = lab(a, b, 0.3, 3.2); text(ax, x, y, r'$\sigma_3$', 'varie', 's')
x, y = lab(b, a, 0.3, 3.2); text(ax, x, y, r'$\sigma_2$', 'sujet', 's')
x0 = 52
text(ax, x0, 62, r'$\sigma_3:\ \omega \mapsto \omega^3$', 'varie', 'm', ha='left')
text(ax, x0, 50, r'$\sigma_2:\ \omega^3 \mapsto \omega^6 = \omega$', 'sujet', 'm', ha='left')
text(ax, x0, 38, r'$2 \times 3 = 6 = 5 + 1$', 'encre', 'm', ha='left')
text(ax, x0, 26, r'$\omega^5 = 1$ donc $\omega^6 = \omega$', 'fixe', 's', ha='left')
box(ax, x0 - 1, 8, 36, 10, 'resultat', label=r'$\sigma_2$ après $\sigma_3$ = $\sigma_1$')
save(fig, '63-161')
