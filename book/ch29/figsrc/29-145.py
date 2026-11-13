import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Wedge
def pt(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arcpts(c, r, a0, a1, n=60): return [pt(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
fig, ax = canvas(66)
O = (44, 58); L = 46
A = pt(O, L, -90 - 20); B = pt(O, L, -90 + 20)
poly(ax, [O, A, B], 'sujet')
line(ax, [O, (44, A[1])], 'varie', lw=1.0, dash=True)
text(ax, 44, 5, 'pliure', 'varie', 's')
line(ax, arcpts(O, 14, -110, -70, 20), 'sujet', lw=1.0)
text(ax, 44, 38, '40°', 'sujet', 's')
for p, s in ((A, -1), (B, 1)):
    q = pt(p, 9, 90 + (20 if s < 0 else -20) + (0))
    text(ax, p[0] + s * 1.0 + (7 if s < 0 else -7), p[1] + 5.5, '70°', 'resultat', 's')
    m = ((O[0] + p[0]) / 2, (O[1] + p[1]) / 2)
    line(ax, [(m[0] - 1.4, m[1] - 0.8 * s * -1 - 0.0), (m[0] + 1.4, m[1] + 0.0)], 'sujet', lw=0) if False else None
    text(ax, m[0] + s * 8, m[1], '5 cm', 'fixe', 's')
text(ax, 44, 63.5, 'O', 'sujet', 'm'); text(ax, A[0] - 4, A[1], 'A', 'sujet', 'm'); text(ax, B[0] + 4, B[1], 'B′', 'sujet', 'm')
save(fig, '29-145')
