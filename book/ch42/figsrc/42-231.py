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
fig, ax = canvas(74)
box(ax, 4, 4, 24, 26, 'sujet'); box(ax, 32, 44, 24, 26, 'sujet'); box(ax, 60, 4, 24, 26, 'sujet')
text(ax, 9, 28, '$S$', 'sujet', 'l'); text(ax, 37, 68, '$T$', 'sujet', 'l'); text(ax, 79, 8, '$U$', 'sujet', 'l')
P = {'S': (16, 17), 'T': (44, 57), 'U': (72, 17)}
for c, ys in (('S', (23, 11)), ('T', (63, 51)), ('U', (23, 11))):
    for y in ys: disc(ax, P[c][0], y, 2, 'fixe')
for c in P: disc(ax, P[c][0], P[c][1], 2.4, 'resultat')
ed(ax, P['S'], P['T'], 'varie', r=2.6); ed(ax, P['T'], P['U'], 'varie', r=2.6)
ed(ax, P['S'], P['U'], 'sujet', r=2.6)
text(ax, 22, 44, '$f$', 'varie', 'm'); text(ax, 66, 44, '$g$', 'varie', 'm')
text(ax, 44, 12, '$g \\circ f$', 'sujet', 'm')
text(ax, 44, 38, 'chemin par $T$', 'varie', 's'); text(ax, 44, 23, 'chemin direct', 'sujet', 's')
text(ax, 44, 2.5, 'même point d’arrivée', 'resultat', 's') if False else None
save(fig, '42-231')
