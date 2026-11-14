import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(94)
x0, y0, sx, sy = 52, 52, 15.0, 0.8
f = lambda x: x ** 5 - 4 * x + 2
arrow(ax, (4, y0), (84, y0), 'fixe', lw=0.8)
ts = np.linspace(-2.1, 2.1, 200)
line(ax, [(x0 + t * sx, y0 + f(t) * sy) for t in ts if abs(f(t)) <= 26.5], 'sujet', lw=1.4)
rts = np.roots([1, 0, 0, 0, -4, 2])
for r in rts.real[np.abs(rts.imag) < 1e-6]:
    disc(ax, x0 + r * sx, y0, 1.6, 'resultat')
# the two zeros of the derivative 5x^4 - 4 : x = -+ (4/5)^(1/4), the two turns of the curve
xd = (4 / 5) ** 0.25
for s in (-1, 1):
    px = x0 + s * xd * sx
    line(ax, [(px, y0 + f(s * xd) * sy), (px, 78)], 'varie', dash=True)
    disc(ax, px, y0 + f(s * xd) * sy, 1.3, 'varie')
for v in range(-2, 3):
    line(ax, [(x0 + v * sx, y0 - 1), (x0 + v * sx, y0 + 1)], 'fixe')
text(ax, 4, 22, r'$x$', 'encre', 's', ha='left')
text(ax, 4, 12, r'$f(x)$', 'encre', 's', ha='left')
for v in range(-2, 3):
    text(ax, x0 + v * sx, 22, f'{v}'.replace('-', '−'), 'encre', 's')
    val = f(v)
    role = 'varie' if val < 0 else 'sujet'
    text(ax, x0 + v * sx, 12, f'{val}'.replace('-', '−'), role, 's')
text(ax, x0, 81, r'2 virages : $5x^4-4=0$', 'varie', 's')
text(ax, 44, 90, r'$x^5-4x+2$ : exactement 3', 'resultat', 's')
save(fig, '65-138')
