import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def seg(p, q, r=4.5):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return [(p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r)]
def hasse(cx, top, bot):
    pts = {'t': (cx, 38), 'l': (cx - 9, 26), 'r': (cx + 9, 26), 'b': (cx, 14)}
    for a, b in [('t', 'l'), ('t', 'r'), ('b', 'l'), ('b', 'r')]: line(ax, seg(pts[a], pts[b]), 'fixe')
    disc(ax, *pts['l'], 4.5, 'sujet', label='12'); disc(ax, *pts['r'], 4.5, 'sujet', label='20')
    disc(ax, *pts['t'], 4.5, top[1], label=top[0]); disc(ax, *pts['b'], 4.5, bot[1], label=bot[0])
    return pts
text(ax, 21, 56, 'Livre : 1 en bas', 'fixe', 's', weight='bold')
text(ax, 67, 56, 'Retourné : 1 en haut', 'fixe', 's', weight='bold')
hasse(21, ('60', 'resultat'), ('1', 'fixe'))
hasse(67, ('1', 'fixe'), ('60', 'resultat'))
text(ax, 21, 48, 'PPCM(12, 20) au-dessus', 'resultat', 's')
text(ax, 67, 5, 'PPCM(12, 20) au-dessous', 'resultat', 's')
arrow(ax, (38, 26), (50, 26), 'varie')
save(fig, '79-110')
