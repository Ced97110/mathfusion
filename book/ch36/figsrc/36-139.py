import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(100)
s = 9; A = (26, 66); C = (A[0] + 4*s, A[1]); B = (C[0], A[1] + 3*s)
poly(ax, [A, C, B], 'resultat'); line(ax, [A, C, B, A], 'sujet', lw=1.4)
rightangle(ax, C, 180, 90, 2.6, 'fixe'); arc(ax, A, 9, 0, 36.87, 'varie', lw=1.1)
text(ax, *pol(A, 14, 14), 'A', 'varie', 's')
text(ax, (A[0] + C[0]) / 2, A[1] - 4, '4', 'sujet', 's'); text(ax, C[0] + 3, (C[1] + B[1]) / 2, '3', 'sujet', 's')
text(ax, (A[0] + B[0]) / 2 - 3.5, (A[1] + B[1]) / 2 + 3.5, '5', 'sujet', 's')
text(ax, 44, 70, '6', 'resultat', 'l')
ys = [48, 33, 18]
arrow(ax, (44, ys[0] - 3), (44, ys[1] + 3), 'varie'); arrow(ax, (44, ys[1] - 3), (44, ys[2] + 3), 'varie')
text(ax, 44, ys[0], r'$\cos A=32\div40=0{,}8$', 'encre', 'm')
text(ax, 44, ys[1], r'$\sin A=0{,}6$ car $0{,}6^2=1-0{,}8^2$', 'encre', 'm')
text(ax, 44, ys[2], 'aire = ½ × 4 × 5 × 0,6 = 6', 'resultat', 'm')
save(fig, '36-139')
