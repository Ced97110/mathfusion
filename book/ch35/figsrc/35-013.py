import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wave(ax, f, x0, w, y0, k, role, lw=1.1, dash=False, n=400, t0=0.0, t1=2 * math.pi):
    line(ax, [(x0 + w * i / n, y0 + k * f(t0 + (t1 - t0) * i / n)) for i in range(n + 1)], role, lw, dash)

fig, ax = canvas(60)
x0, w, y0, k = 14, 60, 10, 7
xd = lambda d: x0 + d / 90 * w
wave(ax, lambda t: 3 * math.sin(t) + 4 * math.cos(t), x0, w, y0, k, 'sujet', 1.6, t1=math.pi / 2)
line(ax, [(10, y0), (78, y0)], 'fixe', 0.8)
d = math.degrees(math.pi / 2 - math.atan2(4, 3))
for dd, v, r, s, lab in ((0, 4, 'fixe', '0°', '4'), (d, 5, 'resultat', '36,87°', '5'), (90, 3, 'fixe', '90°', '3')):
    line(ax, [(xd(dd), y0), (xd(dd), y0 + v * k)], 'fixe', 0.6, True)
    disc(ax, xd(dd), y0 + v * k, 1.5, r)
    text(ax, xd(dd), y0 + v * k + 3.5, lab, r, 's')
    text(ax, xd(dd), 5.5, s, r, 's')
arrow(ax, (xd(0), 54), (xd(90), 54), 'varie', 1.0, both=True)
text(ax, 44, 57.5, 'le maximum est entre 0° et 90°', 'varie', 's')
save(fig, '35-013')
