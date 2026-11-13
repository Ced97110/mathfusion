import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(75)
Y0, S = 36, 3.0
X = lambda t: 12 + t * 28
line(ax, [(4, Y0), (84, Y0)], 'fixe')
for k in range(3):
    line(ax, [(X(k), 8), (X(k), 66)], 'fixe', dash=True)
for k in range(2):
    pts = []
    for i in range(61):
        a = 0.15 + (math.pi - 0.3) * i / 60
        pts.append((X(k) + a / math.pi * 28, Y0 + S * math.cos(a) / math.sin(a)))
    line(ax, pts, 'sujet', lw=1.4)
for k, s in enumerate(['$x=0$', r'$x=\pi$', r'$x=2\pi$']):
    text(ax, X(k), 4, s, 'encre', 's')
text(ax, 21, 61, r'$+\infty$', 'sujet', 's')
text(ax, 49, 61, r'$+\infty$', 'sujet', 's')
text(ax, 34, 11, r'$-\infty$', 'sujet', 's')
text(ax, 24, 50, 'cotan', 'sujet', 'm')
text(ax, 40, 71, 'sin x = 0 sur ces droites', 'encre', 's')
save(fig, '30-065')
