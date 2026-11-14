import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
poly(ax, [(30, 16), (60, 14), (62, 44), (32, 46)], 'fixe')
text(ax, 46, 40, 'forêt', 'fixe', 's')
line(ax, [(38, 8), (40, 24), (37, 40), (39, 54)], 'fixe', lw=1.2)
text(ax, 40, 5, 'fleuve', 'fixe', 's')
P1, P2, P3, P4, P5, P6 = (10, 28), (20, 52), (48, 56), (72, 52), (78, 26), (50, 8)
for a, b in [(P1, P2), (P2, P3), (P3, P4), (P4, P5), (P5, P6), (P6, P1)]:
    line(ax, [a, b], 'sujet', lw=0.7, dash=True)
line(ax, [P1, P5], 'varie', lw=1.3, dash=True)
text(ax, 44, 31, '50 km', 'varie', 'm')
for p in (P1, P2, P3, P4, P5, P6):
    disc(ax, p[0], p[1], 1.5, 'sujet')
text(ax, 10, 22, 'ville', 'sujet', 's')
text(ax, 20, 58, 'clocher', 'sujet', 's')
save(fig, '38-003')
