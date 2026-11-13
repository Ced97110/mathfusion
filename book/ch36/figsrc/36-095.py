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
fig, ax = canvas(62)
f = lambda d: 8 + 0.42 * d
box(ax, f(130), 8, f(180) - f(130), 50, 'limite')
text(ax, (f(130) + f(180)) / 2, 54, 'impossible', 'limite', 's'); text(ax, (f(130) + f(180)) / 2, 50, 'plus de 130°', 'limite', 's')
for y, lab, role in ((36, 'côté 120 : 2 candidats', 'sujet'), (18, 'côté 90, le plus petit :\nangle forcément aigu, 1 seul', 'resultat')):
    line(ax, [(8, y), (f(180), y)], 'fixe', 1.0)
    for d in (0, 130, 180): line(ax, [(f(d), y - 1.2), (f(d), y + 1.2)], 'fixe', 0.8)
    text(ax, 8, y + 9.5, lab, role, 's', ha='left')
for d, y, up, role in ((82.03, 36, 1, 'varie'), (97.97, 36, -1, 'varie'), (47.97, 18, 1, 'resultat'), (132.03, 18, 1, 'limite')):
    disc(ax, f(d), y, 1.8, role); text(ax, f(d), y + 4.5 * up, f'{d:g}°'.replace('.', ','), role, 's')
for d in (0, 130, 180): text(ax, f(d), 13.3, f'{d}°', 'fixe', 's')
text(ax, 30, 4.8, '180° − 50° = 130° au plus', 'fixe', 's')
save(fig, '36-095')
