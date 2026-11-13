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

fig, ax = canvas(48)
text(ax, 44, 41, r'Pourquoi pas 5 ni 7 ?', 'encre', 'l')
for n in range(1, 8):
    cx = 11 + 11 * (n - 1); cy = 27
    r = 'resultat' if n in (1, 2, 3, 4, 6) else 'limite'
    disc(ax, cx, cy, 4.2, r, fill=False, lw=1.0)
    for k in range(n):
        a = math.radians(90 + 360 * k / n)
        disc(ax, cx + 4.2 * math.cos(a), cy + 4.2 * math.sin(a), 0.9, r)
    text(ax, cx, 17, str(n), r, 'm', weight='bold')
disc(ax, 14, 7, 1.2, 'resultat'); text(ax, 17.5, 7, 'ordre observé', 'resultat', 's', ha='left')
disc(ax, 52, 7, 1.2, 'limite'); text(ax, 55.5, 7, 'jamais observé', 'limite', 's', ha='left')
save(fig, '74-017')
