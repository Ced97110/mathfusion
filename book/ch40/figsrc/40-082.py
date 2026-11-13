import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

def spiral(ox, oy, f, t0, t1, n=500):
    pts = []
    for i in range(n + 1):
        t = t0 + (t1 - t0) * i / n
        pts.append((ox + f(t) * math.cos(t), oy + f(t) * math.sin(t)))
    return pts

# gauche : r = a/θ avec a = 1, 1 unité = 9 mm
ox, oy, s = 22, 38, 9
line(ax, spiral(ox, oy, lambda t: s / t, 0.5, 4 * math.pi), 'sujet', lw=1.2)
disc(ax, ox, oy, 0.7, 'fixe')
for th, r, lab in [(0.5, 2, '2'), (1, 1, '1'), (2, 0.5, '0,5'), (4, 0.25, '0,25')]:
    px, py = ox + s * r * math.cos(th), oy + s * r * math.sin(th)
    disc(ax, px, py, 1.0, 'varie')
    d = s * r + 4.5
    text(ax, ox + d * math.cos(th), oy + d * math.sin(th), lab, 'varie', 's')
text(ax, 22, 62, r'$r = a/\theta$', 'sujet', 'l')
text(ax, 22, 12, 'θ : 0,5 ; 1 ; 2 ; 4', 'varie', 's')
text(ax, 22, 6.5, 'r : 2 ; 1 ; 0,5 ; 0,25', 'sujet', 's')

# droite : r = aθ (voisine)
ox2, oy2, k = 66, 38, 18 / (4 * math.pi)
line(ax, spiral(ox2, oy2, lambda t: k * t, 0.0, 4 * math.pi), 'autre', lw=1.2)
disc(ax, ox2, oy2, 0.7, 'fixe')
text(ax, 66, 62, r'$r = a\theta$', 'autre', 'l')
text(ax, 66, 12, 'r grandit avec θ', 'autre', 's')
text(ax, 66, 6.5, 'r = a/θ : r diminue', 'sujet', 's') if False else None
save(fig, '40-082')
