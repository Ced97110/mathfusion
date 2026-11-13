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

fig, ax = canvas(92)
s = 14
cells = [(2.5, 48, 'translation'), (44.5, 48, 'rotation'), (2.5, 4, 'réflexion'), (44.5, 4, 'symétrie glissée')]
for x0, y0, name in cells:
    box(ax, x0, y0, 41, 40, 'fixe', fill=False, lw=0.7)
    text(ax, x0 + 20.5, y0 + 35, name, 'encre', 's', weight='bold')
cx, cy = 2.5 + 20.5, 48 + 16
poly(ax, G(FB, cx - 10, cy, s), 'fixe'); poly(ax, G(FB, cx + 10, cy, s), 'sujet')
cx, cy = 44.5 + 20.5, 48 + 16
C = (cx, cy - 4)
poly(ax, G(FB, cx + 10, cy - 4, s), 'fixe'); poly(ax, rot(G(FB, cx + 10, cy - 4, s), C, 90), 'sujet')
disc(ax, C[0], C[1], 0.9, 'encre')
cx, cy = 2.5 + 20.5, 4 + 16
line(ax, [(cx, 8), (cx, 34)], 'encre', dash=True)
poly(ax, G(FB, cx - 10, cy, s), 'fixe'); poly(ax, mx(G(FB, cx - 10, cy, s), cx), 'sujet')
cx, cy = 44.5 + 20.5, 4 + 16
line(ax, [(47.5, cy), (82.5, cy)], 'encre', dash=True)
P = G(FB, cx - 11, cy + 8, s)
poly(ax, P, 'fixe'); poly(ax, sh(my(P, cy), 22, 0), 'sujet')
save(fig, '74-019')
