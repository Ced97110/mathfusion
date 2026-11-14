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
box(ax, 6, 59, 76, 17, 'sujet', True)
text(ax, 44, 70.5, r'$\cos A=QN\ \div\ QP$', 'sujet', 'l')
text(ax, 44, 63, r'$=12\ \div\ 13\approx 0{,}9231$', 'sujet', 'm')

tri([P, N, Q], 'sujet'); tri([N, R, Q], 'fixe')
line(ax, [Q, N], 'sujet', lw=2.4); line(ax, [P, Q], 'sujet', lw=2.4)
arc(8, -aA, 0, 'sujet', 1.0); text(ax, Q[0] - 2.3, Q[1] - 11.5, 'A', 'sujet', 's')
letters()
text(ax, N[0] + 2.5, (N[1] + Q[1]) / 2, 'QN = 12', 'sujet', 's', ha='left')
text(ax, (P[0] + Q[0]) / 2 - 5, (P[1] + Q[1]) / 2 + 3, 'QP = 13', 'sujet', 's')
save(fig, '34-071')
