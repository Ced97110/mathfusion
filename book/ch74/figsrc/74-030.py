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

fig, ax = canvas(76)
x0, y0, u = 6, 6, 9
grid(x0, y0, u, 5, 7)
P = (x0 + u, y0 + 2 * u); Q = (x0 + 4 * u, y0 + 6 * u); K = (Q[0], P[1])
line(ax, [P, K], 'varie', lw=1.6); line(ax, [K, Q], 'varie', lw=1.6); line(ax, [P, Q], 'sujet', lw=1.8)
line(ax, [(K[0] - 2, K[1]), (K[0] - 2, K[1] + 2), (K[0], K[1] + 2)], 'fixe', lw=0.7)
disc(ax, *P, 1.1, 'sujet'); disc(ax, *Q, 1.1, 'sujet')
text(ax, P[0] - 3, P[1] - 3, r'$P$', 'sujet', 'm'); text(ax, Q[0] + 3, Q[1] + 3, r'$Q$', 'sujet', 'm')
text(ax, (P[0] + K[0]) / 2, P[1] - 3.5, r'$h=3$', 'varie', 'm'); text(ax, K[0] + 3, (K[1] + Q[1]) / 2, r'$k=4$', 'varie', 'm', ha='left')
text(ax, (P[0] + Q[0]) / 2 - 7, (P[1] + Q[1]) / 2 + 3, r'$d=5$', 'sujet', 'l')
text(ax, 70, 46, r'$3^2+4^2=5^2$', 'encre', 'm'); text(ax, 70, 38, r'$9+16=25$', 'encre', 'm')
save(fig, '74-030')
