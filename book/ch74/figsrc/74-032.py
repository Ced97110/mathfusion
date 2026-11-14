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

fig, ax = canvas(44)
u = 1.8; y = 24
def seg(cx, L, role, vert=False):
    a, b = ((cx, y - L / 2), (cx, y + L / 2)) if vert else ((cx - L / 2, y), (cx + L / 2, y))
    line(ax, [a, b], role, lw=1.6); disc(ax, *a, 1.1, role); disc(ax, *b, 1.1, role)
seg(11, 5 * u, 'sujet'); seg(33, 5 * u, 'resultat'); seg(55, 5 * u, 'resultat', True); seg(77, 10 * u, 'limite')
for x, n, r, L in [(11, 'départ', 'sujet', '5 cm'), (33, 'glisse', 'resultat', '5 cm'), (55, 'tourne', 'resultat', '5 cm'), (77, 'agrandit', 'limite', '10 cm')]:
    text(ax, x, 38, n, 'encre', 'm'); text(ax, x, 11, L, r, 'm', weight='bold')
save(fig, '74-032')
