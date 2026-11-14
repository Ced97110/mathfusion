import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

cx, cy, r = 44, 42, 24
fig, ax = canvas(88)
disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.7)
names = ['1', r'$\omega=i$', r'$\omega^2=-1$', r'$\omega^3=-i$']
pos = [(cx + r * math.cos(math.radians(90 * k)), cy + r * math.sin(math.radians(90 * k))) for k in range(4)]
for k in range(4):
    p, q = pos[k], pos[(k + 1) % 4]
    # raccourcir la flèche pour partir et finir au bord des points
    d = math.hypot(q[0] - p[0], q[1] - p[1])
    ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * 2.2, p[1] + uy * 2.2); b = (q[0] - ux * 2.2, q[1] - uy * 2.2)
    arrow(ax, a, b, 'varie' if k < 3 else 'fixe', lw=1.1)
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    text(ax, cx + (mx - cx) * 0.72, cy + (my - cy) * 0.72, r'$\times\,\omega$', 'varie' if k < 3 else 'fixe', 's')
for k in range(4):
    disc(ax, pos[k][0], pos[k][1], 1.5, 'sujet')
text(ax, pos[0][0] + 3, pos[0][1] + 3.5, names[0], 'sujet', 'm', ha='left')
text(ax, pos[1][0] + 3, pos[1][1] + 1.5, names[1], 'sujet', 'm', ha='left')
text(ax, pos[2][0] - 3, pos[2][1] + 3.5, names[2], 'sujet', 'm', ha='right')
text(ax, pos[3][0] + 3, pos[3][1] - 1.5, names[3], 'sujet', 'm', ha='left')
text(ax, 4, 83, r'$n=4$', 'encre', 'l', ha='left')
save(fig, '39-101')
