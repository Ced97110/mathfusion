import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx, cy, R = 30, 30, 22
disc(ax, cx, cy, R, 'fixe', fill=False)
line(ax, [(cx - R, cy), (cx + R, cy)], 'resultat', lw=1.8)
disc(ax, cx + R, cy, 1.5, 'sujet')
disc(ax, cx - R, cy, 1.5, 'sujet')
text(ax, cx + R + 4, cy, '1', 'sujet', 'm')
text(ax, cx - R - 4.8, cy, '−1', 'sujet', 'm')
text(ax, 72, 48, '2 points opposés', 'sujet', 's')
text(ax, 72, 40, 'φ(2) = 1 = 2⁰', 'resultat', 'm')
text(ax, 72, 30, 'diamètre : se trace', 'resultat', 's')
text(ax, 72, 22, 'vert', 'resultat', 'm', weight='bold')
save(fig, '66-108')
