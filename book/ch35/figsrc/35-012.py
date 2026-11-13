import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wave(ax, f, x0, w, y0, k, role, lw=1.1, dash=False, n=400, t0=0.0, t1=2 * math.pi):
    line(ax, [(x0 + w * i / n, y0 + k * f(t0 + (t1 - t0) * i / n)) for i in range(n + 1)], role, lw, dash)

fig, ax = canvas(64)
x0, w, y0, k = 8, 72, 33, 4.8
a = math.atan2(4, 3); xd = lambda d: x0 + d / 360 * w
arrow(ax, (x0, y0), (x0 + w + 6, y0), 'fixe', 0.7)
wave(ax, lambda t: 3 * math.sin(t), x0, w, y0, k, 'sujet', 1.0, True)
wave(ax, lambda t: 4 * math.cos(t), x0, w, y0, k, 'varie', 1.0, True)
wave(ax, lambda t: 3 * math.sin(t) + 4 * math.cos(t), x0, w, y0, k, 'resultat', 1.8)
wave(ax, lambda t: 5 * math.sin(t + a), x0, w, y0, k, 'encre', 0.6, True)
d = math.degrees(math.pi / 2 - a)
disc(ax, xd(d), y0 + 5 * k, 1.2, 'encre', fill=False)
line(ax, [(xd(d), y0), (xd(d), y0 + 5 * k)], 'encre', 0.6, True)
text(ax, xd(d) + 15, y0 + 5 * k, 'sommet : 5', 'encre', 's')
for g in (0, 90, 180, 270, 360):
    line(ax, [(xd(g), y0 - 1), (xd(g), y0 + 1)], 'fixe', 0.7)
    text(ax, xd(g), y0 - 3, f'{g}°', 'fixe', 's')
text(ax, xd(d) - 7, y0 + 3, '36,87°', 'encre', 's')
text(ax, 73, 19, r'$3\,\sin x$', 'sujet', 's'); text(ax, 27, 11.5, r'$4\,\cos x$', 'varie', 's')
text(ax, 64, 7, r'somme $=5\,\sin(x+\alpha)$', 'resultat', 's')
save(fig, '35-012')
