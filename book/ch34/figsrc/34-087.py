import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(84)
fig, ax = canvas(70)
u = 40; x0 = 8
box(ax, x0, 52, 0.75 * u, 8, 'sujet', label='0,75', size='s'); text(ax, x0 + 0.75 * u + 3, 56, r'$\cos^2 A$', 'sujet', 's', ha='left')
box(ax, x0, 32, 0.75 * u, 8, 'varie', label='0,75', size='s'); box(ax, x0 + 0.75 * u, 32, 0.75 * u, 8, 'varie', label='0,75', size='s')
text(ax, x0 + 1.5 * u + 3, 36, r'$\times 2 = 1{,}5$', 'varie', 's', ha='left')
box(ax, x0, 12, 0.5 * u, 8, 'resultat', label='0,5', size='s'); box(ax, x0 + 0.5 * u, 12, 1.0 * u, 8, 'fixe', label='− 1', size='s')
text(ax, x0 + 1.5 * u + 3, 16, r'$\cos 2A$', 'resultat', 's', ha='left')
arrow(ax, (x0 + 0.4 * u, 51), (x0 + 0.4 * u, 41), 'varie'); arrow(ax, (x0 + 0.4 * u, 31), (x0 + 0.4 * u, 21), 'varie')
text(ax, 44, 66, r'$\cos 2A = 2\cos^2 A - 1$', 'encre', 'm')
save(fig, '34-087')
