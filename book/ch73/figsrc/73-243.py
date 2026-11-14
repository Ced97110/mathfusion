import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, r=1.2, role='encre'):
    ax.add_patch(Circle((x, y), r, fc=COL[role], ec=COL[role], zorder=6))
def off(p, q, d):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy)
    return (-dy / n * d, dx / n * d)
def shifted_arrow(ax, p, q, d, role, inset=2.2):
    ox, oy = off(p, q, d); dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy); ux, uy = dx / n, dy / n
    arrow(ax, (p[0] + ox + ux * inset, p[1] + oy + uy * inset), (q[0] + ox - ux * inset, q[1] + oy - uy * inset), role, lw=1.2)
fig, ax = canvas(64)
A = (44, 12); C = (20, 38); B = (68, 38)      # (1, 0), (0, 1), (2, 1)
shifted_arrow(ax, A, C, 1.6, 'sujet'); shifted_arrow(ax, C, B, 1.6, 'sujet')     # f
shifted_arrow(ax, B, C, 1.6, 'varie'); shifted_arrow(ax, C, A, 1.6, 'varie')      # inverse (de l'autre côté)
for q in (A, B, C): dot(ax, *q)
text(ax, 44, 6, '(1, 0)'); text(ax, 17, 38, '(0, 1)', ha='right'); text(ax, 71, 38, '(2, 1)', ha='left')
text(ax, 13, 25, r'$f$ : 1. quart de tour', 'sujet', 's')
text(ax, 44, 46, r'$f$ : 2. décalage (2, 0)', 'sujet', 's')
text(ax, 44, 32, r'$f^{-1}$ : 1. retirer (2, 0)', 'varie', 's')
text(ax, 60, 21, r'$f^{-1}$ : 2. quart inverse', 'varie', 's')
save(fig, '73-243')
