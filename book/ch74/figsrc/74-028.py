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

fig, ax = canvas(56)
s = 14; xs = [14 + 12 * i for i in range(6)]; y = 28
for x in xs: poly(ax, G(HB, x, y, s), 'sujet')
for xv in (38, 44): line(ax, [(xv, 10), (xv, 46)], 'resultat', lw=1.0, dash=True)
line(ax, [(6, y), (82, y)], 'resultat', lw=1.0, dash=True)
for xv in (38, 44): disc(ax, xv, y, 1.3, 'varie')
text(ax, 41, 51, 'miroirs verticaux', 'resultat', 's'); text(ax, 18, 42, 'miroir horizontal', 'resultat', 's')
text(ax, 41, 5, 'centres de demi-tour', 'varie', 's')
save(fig, '74-028')
