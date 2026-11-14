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

fig, ax = canvas(52)
s = 14; y = 24
xs = [11, 33, 55, 77]
names = ['translation', 'rotation', 'réflexion', 'glissée']
c0 = (xs[0], y)
poly(ax, G(FB, xs[0], y, s), 'sujet')
poly(ax, rot(G(FB, xs[1], y, s), (xs[1], y), 90), 'sujet')
poly(ax, mx(G(FB, xs[2], y, s), xs[2]), 'sujet')
poly(ax, my(mx(G(FB, xs[3], y, s), xs[3]), y), 'sujet')
for x, n in zip(xs, names): text(ax, x, 9, n, 'encre', 's')
brace(ax, 3, 41, 36, 'resultat', 'se lit en tournant la tête', down=False)
brace(ax, 47, 85, 36, 'limite', 'demande un miroir', down=False)
save(fig, '74-024')
