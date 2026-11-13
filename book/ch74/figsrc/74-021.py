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

fig, ax = canvas(60)
s = 20; C = (26, 20)
g = G(FB, 42, 24, s)
poly(ax, g, 'fixe'); poly(ax, rot(g, C, 90), 'sujet')
R = 26
pts = [(C[0] + R * math.cos(math.radians(t)), C[1] + R * math.sin(math.radians(t))) for t in range(0, 91, 5)]
line(ax, pts, 'varie', lw=1.0); arrow(ax, pts[-2], pts[-1], 'varie')
disc(ax, C[0], C[1], 1.0, 'encre')
text(ax, 26, 12, r'$C$ ne bouge pas', 'encre', 's')
text(ax, 56, 24, 'départ', 'fixe', 'm', ha='left'); text(ax, 21, 47, 'image', 'sujet', 'm')
text(ax, 54, 44, 'quart de tour', 'varie', 's', ha='left')
save(fig, '74-021')
