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

fig, ax = canvas(62)
s = 16; yd = 34
g = G(FB, 22, 44, s); f1 = my(g, yd); f2 = sh(f1, 36, 0)
line(ax, [(4, yd), (84, yd)], 'encre', lw=1.0, dash=True)
poly(ax, g, 'fixe'); outline(ax, f1, 'varie'); poly(ax, f2, 'sujet')
arrow(ax, (33, 45), (33, 24), 'varie')
arrow(ax, (24, 10), (58, 10), 'varie')
text(ax, 22, 55, 'départ', 'fixe', 'm'); text(ax, 8, 24, 'retourné', 'varie', 's')
text(ax, 71, 24, 'image', 'sujet', 'm'); text(ax, 36, 40, 'retourne', 'varie', 's', ha='left')
text(ax, 41, 4, r'glisse le long de $D$', 'varie', 's'); text(ax, 82, 38, r'axe $D$', 'encre', 's')
text(ax, 68, 52, 'aucun point fixe', 'encre', 's')
save(fig, '74-023')
