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

fig, ax = canvas(84)
s = 10; xs = [14 + 11 * i for i in range(6)]
rows = [(68, 'F', '+ rien d’autre'), (42, 'A', '+ retournement'), (16, 'H', '+ miroirs, demi-tours')]
for y, kind, lab in rows:
    for i, x in enumerate(xs):
        if kind == 'F': poly(ax, G(FB, x, y, s), 'sujet')
        elif kind == 'A':
            g = G(FB, x, y, s); poly(ax, g if i % 2 == 0 else my(g, y), 'sujet')
        else: poly(ax, G(HB, x, y, s), 'sujet')
    text(ax, 2, y + 11, lab, 'autre', 's', ha='left')
    arrow(ax, (xs[0], y - 8), (xs[1], y - 8), 'varie')
    text(ax, xs[1] + 3, y - 8, 'même glissement', 'varie', 's', ha='left')
save(fig, '74-029')
