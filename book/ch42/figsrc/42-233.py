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
fig, ax = canvas(72)
box(ax, 22, 46, 18, 14, 'sujet', label='1', size='l'); box(ax, 44, 46, 18, 14, 'varie', label='$S$', size='l')
text(ax, 42, 67, '« un indice $S$ »', 'encre', 'm')
text(ax, 28, 33, 'l’identité', 'sujet', 'm'); text(ax, 62, 33, 'de l’ensemble $S$', 'varie', 'm')
line(ax, [(31, 46), (29, 37)], 'sujet'); line(ax, [(53, 46), (60, 37)], 'varie')
text(ax, 44, 20, '$1_{\\mathbb{Z}}$ : entiers', 'sujet', 'm'); text(ax, 44, 10, '$1_{\\mathbb{R}}$ : réels', 'sujet', 'm')
save(fig, '42-233')
