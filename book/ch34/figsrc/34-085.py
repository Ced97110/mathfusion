import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(80)
u = 50; x0 = 8
box(ax, x0, 58, 1.1547 * u, 8, 'sujet', label=r'$2\tan A = 1{,}1547$', size='s')
box(ax, x0, 40, 0.3333 * u, 8, 'varie'); box(ax, x0 + 0.3333 * u, 40, 0.6667 * u, 8, 'autre')
text(ax, x0 + 0.1667 * u, 44, '0,3333', 'varie', 's'); text(ax, x0 + 0.6667 * u, 44, '0,6667', 'autre', 's')
text(ax, x0 + 0.1667 * u, 36, r'$\tan^2 A$', 'varie', 's'); text(ax, x0 + 0.6667 * u, 36, r'$1 - \tan^2 A$', 'autre', 's')
box(ax, x0, 18, 0.6667 * u, 8, 'autre', label='1 fois')
box(ax, x0 + 0.6667 * u, 18, (1.1547 - 0.6667) * u, 8, 'autre', fill=False, dash=True, label='0,732')
arrow(ax, (x0 + 0.6667 * u, 52), (x0 + 0.6667 * u, 54.5), 'autre') if False else None
brace(ax, x0, x0 + 1.1547 * u, 15, 'resultat', 'rentre 1,732 fois', down=True)
text(ax, 44, 74, r'$\tan 2A = 2\tan A / (1 - \tan^2 A)$', 'encre', 'm')
save(fig, '34-085')
