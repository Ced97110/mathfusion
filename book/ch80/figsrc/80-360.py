import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
T = (35, 66); BL = (10, 22); BR = (60, 22)
mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
G = ((T[0] + BL[0] + BR[0]) / 3, (T[1] + BL[1] + BR[1]) / 3)
M = {'110': mid(T, BL), '101': mid(T, BR), '011': mid(BL, BR)}
line(ax, [T, BL, BR, T], 'fixe')
line(ax, [T, M['011']], 'fixe'); line(ax, [BL, M['101']], 'fixe'); line(ax, [BR, M['110']], 'fixe')
rr = math.hypot(M['011'][0] - G[0], M['011'][1] - G[1])
disc(ax, G[0], G[1], rr, 'fixe', fill=False, lw=0.9)
pts = {'100': T, '010': BL, '001': BR, '111': G}; pts.update(M)
for lab, (x, y) in pts.items():
    p = box(ax, x - 5, y - 2.9, 10, 5.8, 'sujet', label=lab, size='s'); p.set_zorder(3.5)
box(ax, 68, 34, 18, 9, 'fixe', label='000', dash=True)
text(ax, 77, 29, 'partie vide', 'fixe', 's')
text(ax, 77, 62, '7 points', 'sujet', 's')
save(fig, '80-360')
