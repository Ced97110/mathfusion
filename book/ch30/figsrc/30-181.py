import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
cx, cy, R = 30, 41, 16
a1 = 7 - 2 * math.pi
disc(ax, cx, cy, R, 'fixe', fill=False, lw=1.0)
line(ax, [(cx, cy), (cx + 24, cy)], 'fixe')
pts = [(cx + 22 * math.cos(7 * i / 100), cy + 22 * math.sin(7 * i / 100)) for i in range(101)]
line(ax, pts[:-1], 'varie', lw=1.2); arrow(ax, pts[-2], pts[-1], 'varie', lw=1.2)
line(ax, [(cx, cy), (cx + 24 * math.cos(a1), cy + 24 * math.sin(a1))], 'resultat', lw=1.2)
line(ax, [(cx + 8 * math.cos(a1 * i / 20), cy + 8 * math.sin(a1 * i / 20)) for i in range(21)], 'resultat', lw=1.2)
disc(ax, cx + R * math.cos(a1), cy + R * math.sin(a1), 1.5, 'resultat')
text(ax, 57, 62, 'angle 7 rad :\nun tour complet,\npuis 0,717 rad', 'varie', 's', ha='left')
text(ax, 57, 38, 'angle 0,717 rad', 'resultat', 's', ha='left')
text(ax, 57, 20, 'même rotation :\nmême point d’arrivée', 'encre', 's', ha='left')
save(fig, '30-181')
