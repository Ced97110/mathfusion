import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
U = 3.0; Y0 = 14
def panel(x0, vals, role, title, labels, steps):
    line(ax, [(x0, Y0), (x0 + 38, Y0)], 'fixe')
    pts = [(x0 + 7 + i * 12, Y0 + v * U) for i, v in enumerate(vals)]
    line(ax, pts, role, lw=1.1)
    for i, (px, py) in enumerate(pts):
        disc(ax, px, py, 1.4, role)
        text(ax, px, Y0 - 4, str(i + 1), 'fixe', 's')
        if labels: text(ax, px - 3.5, py + 2.8, str(vals[i]), role, 's')
    for i, s in enumerate(steps):
        (ax_, ay_), (bx_, by_) = pts[i], pts[i + 1]
        dy = -3.0 if by_ > ay_ else 3.2
        text(ax, (ax_ + bx_) / 2 + 4.5, (ay_ + by_) / 2 + dy, s, 'varie' if role == 'autre' else 'sujet', 's')
    text(ax, x0 + 19, 52, title, role, 'm')
panel(4, [1, 4, 9], 'autre', r'$x^2$', True, ['+3', '+5'])
panel(48, [6, 4, 2], 'sujet', r'$2x + y = 8$', False, [r'$-2$', r'$-2$'])
text(ax, 23, 4, 'écarts qui changent', 'varie', 's')
text(ax, 67, 4, 'même écart : linéaire', 'sujet', 's')
save(fig, '24-020')
