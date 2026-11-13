import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def P(o, r, deg): return (o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg)))
def arc(ax, c, r, t1, t2, role='encre', lw=0.8): ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, ec=COL[role], lw=lw, zorder=3))
def rmark(ax, v, d1, d2, s=2.2, role='encre'):
    p1 = P(v, s, d1); p3 = P(v, s, d2); p2 = (p1[0] + p3[0] - v[0], p1[1] + p3[1] - v[1]); line(ax, [p1, p2, p3], role, lw=0.7)
def sn(d): return math.sin(math.radians(d))
def cs(d): return math.cos(math.radians(d))
fig, ax = canvas(70)
x0 = 22; k = 60 / 120; ks = 60 / 0.9903
rows = [(r'$a$', 92.82, 'sujet', '92,82', 62), (r'$b$', 120, 'sujet', '120', 54),
        (r'$\sin A$', 0.7660, 'autre', '0,7660', 38), (r'$\sin B$', 0.9903, 'autre', '0,9903', 30)]
for lab, v, role, vt, y in rows:
    w = v * (k if role == 'sujet' else ks)
    box(ax, x0, y, w, 6.5, role, label=None)
    text(ax, x0 + 2, y + 3.25, vt, role, 's', ha='left')
    text(ax, x0 - 2, y + 3.25, lab, role, 'm', ha='right')
box(ax, 2, 4, 40, 10, 'sujet', label=r'$92{,}82\div 120\approx 0{,}7735$', size='s')
box(ax, 46, 4, 40, 10, 'autre', label=r'$0{,}7660\div 0{,}9903\approx 0{,}7735$', size='s')
text(ax, 44, 9, r'$=$', 'resultat', 'xl')
save(fig, '36-035')
