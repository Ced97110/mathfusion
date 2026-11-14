import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
V = ['1, 0', '0, 1', '1, 1']
disc(ax, 5, 46, 1.8, 'fixe')
ys1 = [76, 46, 16]
text(ax, 22, 88, r'$u_1$', 'sujet', 'm'); text(ax, 62, 88, r'$u_2$', 'varie', 'm')
for a, y1 in enumerate(ys1):
    box(ax, 16, y1 - 3.5, 14, 7, 'sujet', label=V[a], size='s')
    line(ax, [(6.8, 46), (16, y1)], 'sujet', lw=1.0)
    others = [b for b in range(3) if b != a]
    for k, b in enumerate(others):
        y2 = y1 + (6 if k == 0 else -6)
        line(ax, [(30, y1), (54, y2)], 'varie', lw=1.0)
        box(ax, 54, y2 - 3.5, 14, 7, 'varie', label=V[b], size='s')
text(ax, 78, 46, '6 bases', 'resultat', 'm')
save(fig, '75-105')
