import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(74)
R, cy = 15, 52
def rose(cx, n):
    th = np.linspace(0, 2 * math.pi, 800)
    rr = np.cos(n * th)
    line(ax, [(cx + R * r * math.cos(t), cy + R * r * math.sin(t)) for r, t in zip(rr, th)], 'sujet', lw=1.4)
    disc(ax, cx, cy, 1.0, 'fixe')
    for row, (y, role) in enumerate(((31, 'varie'), (24, 'autre'))):
        x0 = cx - (n - 1) * 2.5
        for k in range(n):
            disc(ax, x0 + 5 * k, y, 1.5, role)
rose(24, 3); rose(64, 5)
text(ax, 24, 70, '3 pétales', 'sujet', 'm')
text(ax, 64, 70, '5 pétales', 'sujet', 'm')
text(ax, 24, 16.5, '3 + 3 = 6\nsymétries', 'resultat', 's')
text(ax, 64, 16.5, '5 + 5 = 10\nsymétries', 'resultat', 's')
disc(ax, 8, 6, 1.5, 'varie'); text(ax, 11, 6, 'rotation', 'varie', 's', ha='left')
disc(ax, 34, 6, 1.5, 'autre'); text(ax, 37, 6, 'reflet', 'autre', 's', ha='left')
disc(ax, 56, 6, 1.0, 'fixe'); text(ax, 59, 6, 'pôle immobile', 'fixe', 's', ha='left')
save(fig, '40-123')
