import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

def arc(x, y, r, a, b, role='fixe', lw=0.9):
    ax.add_patch(Arc((x, y), 2 * r, 2 * r, theta1=a, theta2=b, color=COL[role], lw=lw, zorder=3))

fig, ax = canvas(72)
# Triangle 1 : un côté (200 m) et deux angles
A, B, S = (5, 46), (41, 46), (30, 66)
poly(ax, [A, B, S], 'sujet')
a_deg = math.degrees(math.atan2(S[1] - A[1], S[0] - A[0]))
b_deg = 180 - math.degrees(math.atan2(S[1] - B[1], B[0] - S[0]))
arc(A[0], A[1], 5, 0, a_deg, 'sujet')
arc(B[0], B[1], 5, b_deg, 180, 'sujet')
text(ax, 23, 42.5, '200 m', 'sujet', 's', weight='bold')
# Triangle 2 : deux côtés (269,5 m et 347,4 m) et l'angle de 30° entre eux
k = 0.09
V = (50, 46)
P1 = (V[0] + 269.5 * k, V[1])
P2 = (V[0] + 347.4 * k * math.cos(math.radians(30)), V[1] + 347.4 * k * math.sin(math.radians(30)))
poly(ax, [V, P1, P2], 'autre')
arc(V[0], V[1], 6, 0, 30, 'autre')
text(ax, 62, 42.5, '269,5 m', 'autre', 's', weight='bold')
text(ax, 58, 56, '347,4 m', 'autre', 's', weight='bold')
text(ax, 60.5, 47.6, '30°', 'autre', 's')
# Ce qu'on connaît -> la loi
text(ax, 23, 33, 'un côté + les angles', 'sujet', 's')
text(ax, 66, 33, '2 côtés + angle entre eux', 'autre', 's')
box(ax, 3, 9, 40, 9, 'sujet', label='loi des sinus', weight='bold')
box(ax, 45, 9, 40, 9, 'autre', label='loi des cosinus', weight='bold')
arrow(ax, (23, 30.5), (23, 19.5), 'sujet')
arrow(ax, (66, 30.5), (66, 19.5), 'autre')
save(fig, '38-025')
