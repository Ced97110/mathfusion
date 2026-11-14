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
s = 20; xd = 44
g = G(FB, 28, 26, s); m = mx(g, xd)
line(ax, [(xd, 4), (xd, 50)], 'encre', lw=1.0, dash=True)
poly(ax, g, 'fixe'); poly(ax, m, 'sujet')
for i in (0, 3, 8):
    line(ax, [g[i], m[i]], 'varie', lw=0.8, dash=True)
    disc(ax, xd, g[i][1], 0.9, 'resultat')
text(ax, xd, 53, r'axe $D$', 'encre', 's')
text(ax, 28, 11, 'départ', 'fixe', 'm'); text(ax, 62, 11, 'image', 'sujet', 'm')
text(ax, 20, 46, 'même distance', 'varie', 's'); text(ax, 70, 46, r'points de $D$ fixes', 'resultat', 's')
save(fig, '74-022')
