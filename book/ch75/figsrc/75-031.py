import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def vec(ax, o, v, u, role, lw=1.3):
    arrow(ax, o, (o[0] + u * v[0], o[1] + u * v[1]), role, lw)
def para(ax, o, x, y, u, role='fixe'):
    p = lambda a, b: (o[0] + u * (a[0] * 1 + b[0]), o[1] + u * (a[1] + b[1]))
    poly(ax, [o, (o[0] + u * x[0], o[1] + u * x[1]), (o[0] + u * (x[0] + y[0]), o[1] + u * (x[1] + y[1])), (o[0] + u * y[0], o[1] + u * y[1])], role)
def arc(ax, o, r, a0, a1, role='varie', n=30):
    pts = [(o[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), o[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:n - 2], role, lw=1.0); arrow(ax, pts[n - 3], pts[n], role, lw=1.0)
fig, ax = canvas(74)
c = 7.5; gap = 1.2
x0 = 14
def row(y, n_left, label, removed_from):
    # 6 cases : les cases retirées sont en pointillés
    for i in range(6):
        x = x0 + i * (c + gap)
        if i < n_left: box(ax, x, y, c, c, 'sujet', r=0.6)
        else: box(ax, x, y, c, c, 'fixe', fill=False, dash=True, r=0.6)
    text(ax, 3, y + c / 2, label, 'sujet', 's', ha='left')
ys = [58, 42, 26, 10]
row(ys[0], 6, '6', 0); row(ys[1], 4, '4', 0); row(ys[2], 2, '2', 0); row(ys[3], 0, '0', 0)
for k in range(3):
    xs = x0 + (6 - 2 * (k + 1)) * (c + gap)
    xe = x0 + (6 - 2 * k) * (c + gap) - gap
    # cadre orange autour des 2 cases retirées de l'étape (ligne du dessous)
    box(ax, xs - 0.8, ys[k + 1] - 0.8, xe - xs + 1.6 + 0.0, c + 1.6, 'varie', fill=False, r=1.0, lw=1.0)
    text(ax, 72, ys[k + 1] + c / 2 + 8.5, 'paire ' + str(k + 1) + ' : $-2$', 'varie', 's')
    arrow(ax, (xs + 4, ys[k] - 0.5), (xs + 4, ys[k + 1] + c + 1.4), 'varie', lw=0.9)
text(ax, 3, 70, 'dimensions qui restent', 'sujet', 's', ha='left')
save(fig, '75-031')
