import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, t0, t1, role='varie', lw=1.0, dash=False):
    ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t0, theta2=t1, color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3))
def ring(ax, c, r, role='varie', lw=1.0, dash=False):
    ax.add_patch(Circle(c, r, ec=COL[role], fc='none', lw=lw, ls='--' if dash else '-', zorder=3))
def side(ax, p, q, cen, s, role='encre', d=3.2, size='s'):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2; vx, vy = mx - cen[0], my - cen[1]; n = math.hypot(vx, vy)
    text(ax, mx + d * vx / n, my + d * vy / n, s, role, size)
def inner(v, cen, k): return (v[0] + k * (cen[0] - v[0]), v[1] + k * (cen[1] - v[1]))
fig, ax = canvas(76)
V = {'A': (0, 0), 'B': (18, 0), 'C': (6, 14)}
E = {'AB': ('A', 'B'), 'AC': ('A', 'C'), 'BC': ('B', 'C')}
ANG = {'A': ('B', 'C'), 'B': ('A', 'C'), 'C': ('A', 'B')}
cases = [('CCC', {'AB', 'AC', 'BC'}, set(), '1 triangle', 'resultat'), ('CAC', {'AB', 'AC'}, {'A'}, '1 triangle', 'resultat'),
         ('ACA', {'AB'}, {'A', 'B'}, '1 triangle', 'resultat'), ('AAC', {'BC'}, {'A', 'B'}, '1 triangle', 'resultat'),
         ('AAA', set(), {'A', 'B', 'C'}, 'taille inconnue', 'varie'), ('CCA', {'AC', 'BC'}, {'A'}, 'deux possibles', 'varie')]
for i, (code, sides, angs, badge, role) in enumerate(cases):
    col, row = i % 3, i // 3
    ox = 5 + col * 28.5 + 5.2; oy = 52 if row == 0 else 18
    Q = {k: (ox + p[0], oy + p[1]) for k, p in V.items()}
    poly(ax, [Q['A'], Q['B'], Q['C']], 'fixe')
    for e, (p, q) in E.items():
        if e in sides: line(ax, [Q[p], Q[q]], 'sujet', 2.0)
        else: line(ax, [Q[p], Q[q]], 'fixe', 0.8, dash=True)
    for v in angs:
        p, q = ANG[v]; a1 = math.degrees(math.atan2(Q[p][1] - Q[v][1], Q[p][0] - Q[v][0])); a2 = math.degrees(math.atan2(Q[q][1] - Q[v][1], Q[q][0] - Q[v][0]))
        d = (a2 - a1 + 180) % 360 - 180; t0, t1 = (a1, a1 + d) if d >= 0 else (a1 + d, a1)
        arc(ax, Q[v], 3.4, t0, t1, 'sujet', 1.3)
    cx = 5 + col * 28.5 + 14.25
    text(ax, cx, oy + 18.5, code, 'sujet', 'm', weight='bold'); text(ax, cx, oy - 4.5, badge, role, 's')
text(ax, 24, 4, 'épais = donné', 'sujet', 's'); text(ax, 64, 4, 'pointillé = à trouver', 'fixe', 's')
save(fig, '36-078')
