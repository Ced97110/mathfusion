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
s = 20
c0 = (44, 28)
poly(ax, G(FB, *c0, s), 'sujet')
poly(ax, rot(G(FB, 14, 28, s), (14, 28), 90), 'varie')
poly(ax, mx(G(FB, 74, 28, s), 74), 'varie')
arrow(ax, (35, 28), (27, 28), 'varie'); arrow(ax, (53, 28), (62, 28), 'varie')
text(ax, 44, 11, 'départ', 'sujet', 'm')
text(ax, 15, 11, 'quart de tour', 'varie', 's')
text(ax, 73, 11, 'miroir', 'varie', 's')
text(ax, 44, 46, 'le F change d’aspect à chaque mouvement', 'encre', 's')
save(fig, '74-018')
