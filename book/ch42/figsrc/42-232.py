import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R = 3.0
def dots(ax, x, labs, ys, role):
    for l, y in zip(labs, ys): disc(ax, x, y, R, role, label=l)
def link(ax, pa, pb, role, dy=0.0, curve=0.0):
    s = 1 if pb[0] > pa[0] else -1
    arrow(ax, (pa[0] + s * R, pa[1] + dy), (pb[0] - s * R, pb[1] + dy), role, curve=curve)
def ed(ax, p, q, role, r=R, curve=0.0):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    arrow(ax, (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r), role, curve=curve)
fig, ax = canvas(66)
ys = [44, 32, 20]; r = 2.2
def panel(p, pairs, role, tit, note):
    x0 = 16 + 26 * p; x1 = x0 + 12
    for y in ys: disc(ax, x0, y, r, role); disc(ax, x1, y, r, role)
    for i, j in pairs: ed(ax, (x0, ys[i]), (x1, ys[j]), role, r=r)
    text(ax, (x0 + x1) / 2, 57, tit, role, 'm'); text(ax, (x0 + x1) / 2, 9, note, role, 's')
panel(0, [(0, 0), (1, 1), (2, 2)], 'sujet', 'identité', 'ne déplace rien')
panel(1, [(0, 0), (1, 0), (2, 0)], 'limite', 'constante', 'rassemble tout')
panel(2, [(0, 1), (1, 2), (2, 0)], 'limite', 'décalage', 'déplace tout')
for y, t in zip(ys, '123'): text(ax, 7, y, t, 'fixe', 's'); text(ax, 84, y, t, 'fixe', 's')
save(fig, '42-232')
