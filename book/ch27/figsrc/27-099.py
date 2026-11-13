import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax, c, r, a0, a1, role, lw=0.9, n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
def square(ax, p, u, v, s, role="fixe"):
    line(ax, [(p[0] + u[0] * s, p[1] + u[1] * s), (p[0] + (u[0] + v[0]) * s, p[1] + (u[1] + v[1]) * s), (p[0] + v[0] * s, p[1] + v[1] * s)], role, lw=0.7)
fig, ax = canvas(62)
x0, x1 = 26, 80; f = lambda a: x0 + a / 90 * (x1 - x0)
rows = [(48, 'ℎ = 0', [0, 0]), (36, 'ℎ = 6', [59.49, 67.38]), (24, 'ℎ = 600', [89.66, 89.76])]
for a in (0, 90): line(ax, [(f(a), 17), (f(a), 54)], 'fixe', dash=True)
for y, lab, (al, be) in rows:
    text(ax, 13, y, lab, 'encre', 'm')
    line(ax, [(x0, y), (x1, y)], 'fixe', lw=0.5)
    disc(ax, f(be), y, 1.3, 'autre'); disc(ax, f(al), y, 2.0, 'sujet', fill=True)
    disc(ax, f(be), y, 1.0, 'autre')
numberline(ax, x0, x1, 14, 0, 90, step=30, arrow_right=False, size='s')
arrow(ax, (3, 44), (3, 26), 'varie')
disc(ax, 40, 58, 1.8, 'sujet'); text(ax, 44, 58, r'$\alpha$', 'sujet', 'm'); disc(ax, 56, 58, 1.2, 'autre'); text(ax, 60, 58, r'$\beta$', 'autre', 'm')
save(fig, '27-099')
