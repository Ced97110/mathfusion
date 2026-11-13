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

def grid(x0, y0, u, nx, ny):
    for i in range(nx + 1): line(ax, [(x0 + i * u, y0), (x0 + i * u, y0 + ny * u)], 'fixe', lw=0.3)
    for j in range(ny + 1): line(ax, [(x0, y0 + j * u), (x0 + nx * u, y0 + j * u)], 'fixe', lw=0.3)

fig, ax = canvas(68)
x0, y0, u = 19, 6, 10
grid(x0, y0, u, 5, 5)
O = (x0, y0); V = (x0 + 3 * u, y0 + 4 * u); K = (V[0], O[1])
line(ax, [O, K], 'fixe', lw=1.0, dash=True); line(ax, [K, V], 'fixe', lw=1.0, dash=True)
arrow(ax, O, V, 'sujet', lw=1.8); disc(ax, *O, 1.1, 'encre')
text(ax, O[0] - 3, O[1] - 3, r'$O$', 'encre', 'm')
text(ax, (O[0] + K[0]) / 2, O[1] + 3.2, '3 cases', 'fixe', 's'); text(ax, K[0] + 2.5, (K[1] + V[1]) / 2, '4 cases', 'fixe', 's', ha='left')
text(ax, (O[0] + V[0]) / 2 - 8, (O[1] + V[1]) / 2 + 4, r'$|v|=5$', 'sujet', 'l')
save(fig, '74-031')
