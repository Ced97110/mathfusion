import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import cos, sin, radians, degrees, atan2
from matplotlib.patches import Arc

def wedge(P, Q, R, r, role='fixe'):
    a1 = degrees(atan2(Q[1]-P[1], Q[0]-P[0])); a2 = degrees(atan2(R[1]-P[1], R[0]-P[0]))
    d = (a2 - a1 + 180) % 360 - 180
    t1, t2 = (a1, a1 + d) if d > 0 else (a1 + d, a1)
    ax.add_patch(Arc(P, 2*r, 2*r, theta1=t1, theta2=t2, ec=COL[role], lw=0.9, zorder=3))

s = 0.075
fig, ax = canvas(98)
def rel(o, dist, ang): return (o[0] + dist*s*cos(radians(ang)), o[1] + dist*s*sin(radians(ang)))
ys = (70, 38, 6)
# ligne 1 : triangle ABP
A = (8, ys[0]); B = (A[0] + 200*s, A[1]); P = rel(A, 269.459, 80)
poly(ax, [A, B, P], 'fixe'); line(ax, [A, B, P, A], 'fixe', 1.0); line(ax, [A, P], 'varie', 2.0)
wedge(A, B, P, 4); wedge(B, A, P, 4)
text(ax, 34, ys[0] + 14, 'sinus : côté 200 m, angles 80° et 60°', 'fixe', 's', ha='left')
text(ax, 34, ys[0] + 6, 'AP ≈ 269,5 m', 'varie', 'm', ha='left', weight='bold')
# ligne 2 : triangle ABQ
A = (8, ys[1]); B = (A[0] + 200*s, A[1]); Q = rel(A, 347.362, 50)
poly(ax, [A, B, Q], 'fixe'); line(ax, [A, B, Q, A], 'fixe', 1.0); line(ax, [A, Q], 'varie', 2.0)
wedge(A, B, Q, 4); wedge(B, A, Q, 4)
text(ax, 34, ys[1] + 14, 'sinus : côté 200 m, angles 50° et 95°', 'fixe', 's', ha='left')
text(ax, 34, ys[1] + 6, 'AQ ≈ 347,4 m', 'varie', 'm', ha='left', weight='bold')
# ligne 3 : triangle APQ
A = (8, ys[2]); P = rel(A, 269.459, 80); Q = rel(A, 347.362, 50)
poly(ax, [A, P, Q], 'resultat'); line(ax, [A, P], 'varie', 2.0); line(ax, [A, Q], 'varie', 2.0)
line(ax, [P, Q], 'resultat', 2.0)
wedge(A, Q, P, 7, 'fixe')
text(ax, 34, ys[2] + 14, 'cosinus : 269,5 m, 347,4 m, angle 30°', 'fixe', 's', ha='left')
text(ax, 34, ys[2] + 6, 'PQ ≈ 176,5 m', 'resultat', 'm', ha='left', weight='bold')
for y in (ys[0], ys[1]):
    arrow(ax, (20, y - 2), (20, y - 9), 'varie')
save(fig, '38-056')
