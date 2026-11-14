import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx, cy, r = 44, 38, 12
disc(ax, cx, cy, r, 'autre', fill=False, lw=1.8)
line(ax, [(cx - 8, cy), (cx + 8, cy)], 'sujet', lw=1.8); line(ax, [(cx, cy - 8), (cx, cy + 8)], 'sujet', lw=1.8)
text(ax, 14, cy, 'le plus :\nl’addition', 'sujet'); arrow(ax, (24.5, cy), (cx - 8.5, cy), 'sujet')
text(ax, 76, cy, 'le rond :\nles couples', 'autre'); arrow(ax, (65, cy), (cx + r + 0.5, cy), 'autre')
text(ax, 44, 15, r'$G\oplus H$', 'sujet', 'xl'); text(ax, 44, 6, 'G somme directe H', 'encre')
save(fig, '45-175')
