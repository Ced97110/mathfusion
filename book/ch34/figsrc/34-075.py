import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
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

tri([P, N, Q], 'sujet'); tri([N, R, Q], 'varie')
arc(9, -aA, 0, 'sujet', 1.3); arc(9, 0, aB, 'varie', 1.3)
text(ax, Q[0] - 2.4, Q[1] - 13, 'A', 'sujet', 's', weight='bold'); text(ax, Q[0] + 3.4, Q[1] - 13, 'B', 'varie', 's', weight='bold')
letters()
text(ax, 22, 52, r'$A\approx 22{,}62°$', 'sujet', 'm'); text(ax, 66, 52, r'$B\approx 36{,}87°$', 'varie', 'm')
text(ax, 44, 66, 'deux angles : A et B', 'encre', 'l')
save(fig, '34-075')
