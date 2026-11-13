import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(72)
k = 7.17; P = (6, 10); O = (6 + 3.905 * k, 10); V = (O[0], 10 + 6.98 * k)
poly(ax, [P, O, V], 'sujet'); square(ax, O, (-1, 0), (0, 1), 2.5)
arc(ax, P, 9, 0, 60.78, 'resultat', lw=1.1)
text(ax, V[0], V[1] + 4, r'$V$', 'sujet', 'l'); text(ax, O[0] + 3, 6, r'$O$', 'sujet', 'l'); text(ax, P[0] - 2, 6, r'$P$', 'sujet', 'l')
text(ax, 11, 38, '8', 'varie', 'l'); text(ax, 17, 6, '3,905', 'varie', 'm')
text(ax, 17, 14.2, r'$\alpha$', 'resultat', 'm')
text(ax, 22, 60, r'$\cos\,\alpha \approx 0{,}488$', 'encre', 'm'); text(ax, 22, 68, r'$\alpha \approx 60{,}78°$', 'resultat', 'l')
rx, ry, rw, rh = 52, 14, 32, 26.7
box(ax, rx, ry, rw, rh, 'fixe', r=0.3)
line(ax, [(rx, ry), (rx + rw, ry + rh)], 'varie', lw=1.1)
disc(ax, rx + rw / 2, ry + rh / 2, 1.0, 'sujet')
text(ax, rx + rw / 2 - 4, ry + rh / 2 + 3.5, r'$O$', 'sujet', 's')
text(ax, rx + rw / 2, ry - 4, '6', 'fixe', 'm'); text(ax, rx - 3, ry + rh / 2, '5', 'fixe', 'm')
text(ax, rx + rw / 2, ry + rh + 5, 'diagonale 7,81', 'varie', 's')
save(fig, '27-098')
