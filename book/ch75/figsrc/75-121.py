import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def pair(cx, cy, u, v, role):
    p = [(cx, cy), (cx + u[0] * 8, cy + u[1] * 8), (cx + (u[0] + v[0]) * 8, cy + (u[1] + v[1]) * 8), (cx + v[0] * 8, cy + v[1] * 8)]
    poly(ax, p, role); arrow(ax, p[0], p[1], role); arrow(ax, p[0], p[3], role)
pair(6, 40, (1, 0), (0, 1), 'sujet'); text(ax, 14, 32, 'aire 1', 'sujet', 's')
pair(62, 40, (1, 0), (1, 1), 'resultat'); text(ax, 74, 32, 'aire 1', 'resultat', 's')
arrow(ax, (28, 46), (56, 46), 'resultat'); text(ax, 42, 50, 'possible', 'resultat', 's')
text(ax, 14, 62, 'paire de départ', 'sujet', 's')
poly(ax, [(62, 12), (70, 12), (70, 12.1), (62, 12.1)], 'limite', fill=False)
arrow(ax, (14, 26), (56, 14), 'limite', curve=0.0); text(ax, 40, 24, 'impossible', 'limite', 's')
line(ax, [(33, 17.5), (37, 21.5)], 'limite', lw=1.4); line(ax, [(33, 21.5), (37, 17.5)], 'limite', lw=1.4)
text(ax, 70, 7, 'aire 0', 'limite', 's')
save(fig, '75-121')
