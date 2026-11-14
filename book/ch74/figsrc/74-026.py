import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
FB = [(0,0),(.3,0),(.3,.4),(.6,.4),(.6,.58),(.3,.58),(.3,.72),(.8,.72),(.8,1),(0,1)]
HB = [(0,0),(.25,0),(.25,.38),(.55,.38),(.55,0),(.8,0),(.8,1),(.55,1),(.55,.62),(.25,.62),(.25,1),(0,1)]
def G(B, cx, cy, s):
    return [(cx + s * (x - .4), cy + s * (y - .5)) for x, y in B]
def mx(P, x0): return [(2 * x0 - x, y) for x, y in P]
def my(P, y0): return [(x, 2 * y0 - y) for x, y in P]
def sh(P, dx, dy): return [(x + dx, y + dy) for x, y in P]
def rot(P, c, deg):
    a = math.radians(deg); ca, sa = math.cos(a), math.sin(a)
    return [(c[0] + ca * (x - c[0]) - sa * (y - c[1]), c[1] + sa * (x - c[0]) + ca * (y - c[1])) for x, y in P]
def outline(ax, P, role, dash=True):
    line(ax, list(P) + [P[0]], role, lw=0.8, dash=dash)

fig, ax = canvas(76)
s = 10; xs = [14 + 11 * i for i in range(6)]
for x in xs: poly(ax, G(FB, x, 68, s), 'sujet')
for k in (1, 2, 3):
    y = 57 - 5 * (k - 1)
    arrow(ax, (xs[0], y), (xs[k], y), 'varie')
    text(ax, xs[k] + 3, y, f'{k} pas', 'varie', 's', ha='left')
text(ax, 70, 52, 'elle retombe', 'resultat', 's')
poly(ax, mx(G(FB, 20, 26, s * 1.4), 20), 'limite')
poly(ax, rot(G(FB, 62, 26, s * 1.4), (62, 26), 180), 'limite')
text(ax, 20, 11, 'retournée : change', 'limite', 's'); text(ax, 62, 11, 'demi-tour : à l’envers', 'limite', 's')
save(fig, '74-026')
