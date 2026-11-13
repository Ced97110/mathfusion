import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wave(ax, f, x0, w, y0, k, role, lw=1.1, dash=False, n=400, t0=0.0, t1=2 * math.pi):
    line(ax, [(x0 + w * i / n, y0 + k * f(t0 + (t1 - t0) * i / n)) for i in range(n + 1)], role, lw, dash)

fig, ax = canvas(58)
O = (8, 12); Hh = (20, 12); A = (20, 28); th = math.atan2(4, 3)
poly(ax, [O, Hh, A], 'fixe')
line(ax, [O, Hh], 'fixe', 1.4); line(ax, [Hh, A], 'fixe', 1.4); line(ax, [O, A], 'resultat', 2.0)
line(ax, [(17, 12), (17, 15), (20, 15)], 'fixe', 0.7)
line(ax, [(O[0] + 6 * math.cos(t * th / 30), 12 + 6 * math.sin(t * th / 30)) for t in range(31)], 'varie', 1.2)
text(ax, 14, 17, r'$\alpha$', 'varie', 'm')
text(ax, 11, 24, r'$R$', 'resultat', 'm')
x0, w, y0, k = 34, 50, 30, 3.8
xd = lambda d: x0 + d / 360 * w
arrow(ax, (x0, y0), (x0 + w + 3, y0), 'fixe', 0.7)
wave(ax, lambda t: math.sin(t), x0, w, y0, k, 'fixe', 1.2, True)
wave(ax, lambda t: 5 * math.sin(t + th), x0, w, y0, k, 'resultat', 1.6)
d = math.degrees(math.pi / 2 - th)
line(ax, [(xd(d), y0), (xd(d), y0 + 5 * k)], 'fixe', 0.5, True); line(ax, [(xd(90), y0), (xd(90), y0 + k)], 'fixe', 0.5, True)
line(ax, [(xd(d), y0 + 5 * k), (x0 + w, y0 + 5 * k)], 'resultat', 0.6, True)
text(ax, 66, y0 + 5 * k + 3.5, r'hauteur $R=5$', 'resultat', 's')
arrow(ax, (xd(90), y0 - 3), (xd(d), y0 - 3), 'varie', 1.2)
text(ax, 44, y0 - 8, r'$\alpha=53{,}13°$', 'varie', 's')
text(ax, 17, 5, 'triangle', 'fixe', 's'); text(ax, 62, 5, 'courbe', 'fixe', 's')
save(fig, '35-015')
