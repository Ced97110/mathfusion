import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(84)
fig, ax = canvas(66)
u = 44; x0 = 8
rows = [('0°', 0.0, '1'), ('30°', 0.5, '0,5'), ('45°', 1.0, '0')]
for i, (a, rm, res) in enumerate(rows):
    y = 38 - i * 16
    text(ax, 4, y + 4, a, 'sujet', 's', ha='left')
    x1 = x0 + 8
    if rm < 1: box(ax, x1, y, (1 - rm) * u, 8, 'resultat', label=res, size='s')
    if rm > 0: box(ax, x1 + (1 - rm) * u, y, rm * u, 8, 'varie', label=('1' if rm == 1 else '0,5'), size='s')
    text(ax, x1 + u + 4, y + 4, res, 'resultat', 's', ha='left')
text(ax, 4, 62, r'$\cos 2A = 1 - 2\sin^2 A$', 'encre', 'm', ha='left')
text(ax, 66, 52, r'$\cos 2A$', 'resultat', 's')
text(ax, x0 + 8 + 0.5 * u, 52, r'$2\sin^2 A$ retiré', 'varie', 's', ha='left')
save(fig, '34-088')
