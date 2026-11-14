import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
# √3 + i = 2 cis 30° et 1 + i = √2 cis 45° : deux triangles rectangles
fig, ax = canvas(58)
u = 20
def tri(ox, oy, a, b, role, ang, title, calc, hyp, la, lb):
    A, P, B = (ox, oy), (ox + a * u, oy), (ox + a * u, oy + b * u)
    line(ax, [A, P, B], 'fixe', lw=1.2)
    line(ax, [A, B], role, lw=2.0)
    line(ax, [(P[0] - 2, oy), (P[0] - 2, oy + 2), (P[0], oy + 2)], 'fixe', lw=0.7)
    disc(ax, B[0], B[1], 1.5, role)
    ax.add_patch(Arc(A, 22, 22, theta1=0, theta2=ang, ec=COL['varie'], lw=1.1, zorder=3))
    text(ax, ox + 15.5 * math.cos(math.radians(ang / 2 - 8)) + 0.5, oy + 15.5 * math.sin(math.radians(ang / 2 - 8)) + 1, f'{ang}°', 'varie', 's')
    text(ax, (A[0] + P[0]) / 2, oy - 3.7, la, 'fixe', 'm')
    text(ax, P[0] + 2.5, oy + b * u / 2, lb, 'fixe', 'm', ha='left')
    text(ax, (A[0] + B[0]) / 2 - 3.5, (A[1] + B[1]) / 2 + 3.5, hyp, role, 'm', weight='bold')
    text(ax, ox + a * u / 2 + 2, 49, title, role, 's', weight='bold')
    text(ax, ox + a * u / 2 + 2, 6, calc, role, 's')
tri(4, 16, math.sqrt(3), 1, 'sujet', 30, 'z = √3 + i\n= 2 cis 30°', '3 + 1 = 4 : r = 2', '2', '√3', '1')
tri(50, 16, 1, 1, 'autre', 45, 'w = 1 + i\n= √2 cis 45°', '1 + 1 = 2 : r = √2', '√2', '1', '1')
save(fig, '39-070')
