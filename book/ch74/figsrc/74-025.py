import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def glyph(ax, k, cx, cy, s, role, lw=1.2):
    cyb = -.2 if k == 'b' else .2
    st = [(-.25, .5), (-.25, -.5)]
    bowl = [(.03 + .28 * math.cos(t * math.pi / 12), cyb + .28 * math.sin(t * math.pi / 12)) for t in range(25)]
    for pts in (st, bowl):
        line(ax, [(cx + x * s, cy + y * s) for x, y in pts], role, lw=lw)
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

fig, ax = canvas(78)
s = 11; xs = [26 + 10.5 * i for i in range(6)]
for i, x in enumerate(xs):
    poly(ax, G(FB, x, 68, s), 'sujet')
    glyph(ax, 'b' if i % 2 == 0 else 'p', x, 40, 11, 'sujet')
    poly(ax, G(HB, x, 12, s), 'sujet')
line(ax, [(20, 40), (82, 40)], 'resultat', lw=1.0, dash=True)
arrow(ax, (xs[0], 28), (xs[1], 28), 'varie')
text(ax, 46, 28, 'glisser d’une demi-période', 'varie', 's', ha='left')
text(ax, 2, 68, 'glissements', 'encre', 's', ha='left'); text(ax, 2, 40, 'glissée', 'encre', 's', ha='left')
text(ax, 2, 12, 'miroirs', 'encre', 's', ha='left')
text(ax, 51, 50, 'retourner autour de $D$', 'resultat', 's')
save(fig, '74-025')
