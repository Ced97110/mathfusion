import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
import math
u = 3.3
N = (44, 9); P = (N[0] - 5 * u, N[1]); R = (N[0] + 9 * u, N[1]); Q = (N[0], N[1] + 12 * u)
def tri(pts, role, fill=True):
    poly(ax, pts, role, fill=fill, lw=0.7)
def arc(r, a0, a1, role, lw=1.0):
    n = 14
    line(ax, [(Q[0] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n)), Q[1] - r * math.cos(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw=lw)
aA = math.degrees(math.atan(5 / 12)); aB = math.degrees(math.atan(9 / 12))
def letters():
    text(ax, P[0] - 2.5, P[1] + 0.2, 'P', 'encre', 's'); text(ax, N[0], N[1] - 3.4, 'N', 'encre', 's')
    text(ax, Q[0], Q[1] + 3.2, 'Q', 'encre', 's'); text(ax, R[0] + 2.5, R[1] + 0.2, 'R', 'encre', 's')
box(ax, 6, 59, 76, 17, 'varie', True)
text(ax, 44, 70.5, r'$\cos B=QN\ \div\ QR$', 'varie', 'l')
text(ax, 44, 63, r'$=12\ \div\ 15=0{,}8$', 'varie', 'm')

tri([P, N, Q], 'fixe'); tri([N, R, Q], 'varie')
line(ax, [Q, N], 'varie', lw=2.4); line(ax, [R, Q], 'varie', lw=2.4)
arc(8, 0, aB, 'varie', 1.0); text(ax, Q[0] + 3.2, Q[1] - 11.5, 'B', 'varie', 's')
letters()
text(ax, N[0] + 3.2, (N[1] + Q[1]) / 2 - 6, 'QN = 12', 'varie', 's', ha='left')
text(ax, (R[0] + Q[0]) / 2 + 5, (R[1] + Q[1]) / 2 + 3, 'QR = 15', 'varie', 's')
save(fig, '34-073')
