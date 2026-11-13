import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wave(ax, f, x0, w, y0, k, role, lw=1.1, dash=False, n=400, t0=0.0, t1=2 * math.pi):
    line(ax, [(x0 + w * i / n, y0 + k * f(t0 + (t1 - t0) * i / n)) for i in range(n + 1)], role, lw, dash)

fig, ax = canvas(62)
x0, w, y0, k = 8, 72, 30, 4.2
a = math.atan2(4, 3); xd = lambda d: x0 + d / 360 * w
arrow(ax, (x0, y0), (x0 + w + 6, y0), 'fixe', 0.7)
wave(ax, lambda t: math.sin(t), x0, w, y0, k, 'fixe', 1.3, True)
wave(ax, lambda t: 5 * math.sin(t + a), x0, w, y0, k, 'resultat', 1.6)
d = math.degrees(math.pi / 2 - a)
for dd in (d, 90): line(ax, [(xd(dd), y0), (xd(dd), y0 + (5 if dd == d else 1) * k)], 'fixe', 0.5, True)
arrow(ax, (xd(90), y0 - 3.5), (xd(d), y0 - 3.5), 'varie', 1.2)
text(ax, 20.5, y0 - 8.5, '53,13° plus tôt', 'varie', 's')
brace(ax, x0, x0 + w, 53, 'fixe', 'même période : 360°', False)
text(ax, 64, 46, 'hauteur 5', 'resultat', 's'); text(ax, 43, 40, 'hauteur 1', 'fixe', 's')
save(fig, '35-014')
