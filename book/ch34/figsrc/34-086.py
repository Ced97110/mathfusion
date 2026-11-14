import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(84)
fig, ax = canvas(80)
u = 40; x0 = 8
rows = [(r'$\cos^2 A - \sin^2 A$', 0.75, '− 0,25'), (r'$2\cos^2 A - 1$', 1.5, '− 1'), (r'$1 - 2\sin^2 A$', 1.0, '− 0,5')]
for i, (lab, tot, rm) in enumerate(rows):
    y = 52 - i * 22
    text(ax, x0, y + 13, lab, 'sujet', 's', ha='left')
    box(ax, x0, y, 0.5 * u, 8, 'resultat', label='0,5', size='s')
    box(ax, x0 + 0.5 * u, y, (tot - 0.5) * u, 8, 'varie', label=rm, size='s')
line(ax, [(x0 + 0.5 * u, 12), (x0 + 0.5 * u, 62)], 'resultat', dash=True)
text(ax, x0 + 0.25 * u, 5, r'$\cos 2A = 0{,}5$', 'resultat', 's')
text(ax, 44, 76, 'trois écritures, une valeur', 'encre', 'm')
save(fig, '34-086')
