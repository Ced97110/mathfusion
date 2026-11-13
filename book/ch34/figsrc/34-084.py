import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(58)
u = 70; x0 = 8
f = numberline(ax, x0, x0 + u, 14, 0, 1, 0.25, arrow_right=False)
box(ax, f(0), 28, 0.5 * u, 9, 'resultat'); box(ax, f(0.5), 28, 0.25 * u, 9, 'varie')
text(ax, f(0.25), 32.5, '0,5', 'resultat', 's'); text(ax, f(0.625), 32.5, '0,25', 'varie', 's')
brace(ax, f(0), f(0.75), 39, 'sujet', r'$\cos^2 A = 0{,}75$', down=False)
text(ax, f(0.625), 22, r'$- \sin^2 A$', 'varie', 's'); text(ax, f(0.25), 22, r'$\cos 2A$', 'resultat', 's')
arrow(ax, (f(0.625), 25), (f(0.625), 27.5), 'varie')
text(ax, 44, 50, r'$\cos 2A = \cos^2 A - \sin^2 A$', 'encre', 'm')
save(fig, '34-084')
