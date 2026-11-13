import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(74)
box(ax, 1.5, 4, 41, 62, 'resultat', fill=False, dash=True)
box(ax, 45.5, 4, 41, 62, 'limite', fill=False, dash=True)
text(ax, 22, 60, 'un même triangle :\nplus grand côté,\nplus grand sinus', 'resultat', 's')
text(ax, 66, 60, 'deux triangles :\nplus petit côté,\nplus grand sinus', 'limite', 's')
ks = 1 / 120 * 30; kc = 30 / 0.9903
left = [(90, '90 m', 0.7428, '0,7428', 38), (92.82, '92,82 m', 0.7660, '0,7660', 23), (120, '120 m', 0.9903, '0,9903', 8)]
for cv, ct, sv, st, y in left:
    box(ax, 5, y + 7, cv * ks, 6, 'sujet', label=None); text(ax, 7, y + 10, ct, 'sujet', 's', ha='left')
    box(ax, 5, y, sv * kc, 6, 'autre', label=None); text(ax, 7, y + 3, st, 'autre', 's', ha='left')
right = [(10, '10 m', 0.5, '0,5', 38), (5, '5 m', 1, '1', 20)]
for cv, ct, sv, st, y in right:
    box(ax, 49, y + 7, cv * 3, 6, 'sujet', label=None); text(ax, 51, y + 10, ct, 'sujet', 's', ha='left')
    box(ax, 49, y, sv * 24, 6, 'autre', label=None); text(ax, 51, y + 3, st, 'autre', 's', ha='left')
save(fig, '36-036')
