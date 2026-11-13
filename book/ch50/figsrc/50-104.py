import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
c = 6.5
text(ax, 44, 55, 'le cas montre', 'encre', 'm')
box(ax, 6, 40, c, c, 'sujet', r=0.3)
text(ax, 17, 43.2, '+', 'encre', 'l')
for k in range(2): box(ax, 22 + k * c, 40, c, c, 'autre', r=0.3)
text(ax, 41, 43.2, '=', 'encre', 'l')
for k in range(3): box(ax, 47 + k * c, 40, c, c, 'resultat', r=0.3)
text(ax, 9.2, 36, '1', 'sujet', 's'); text(ax, 28.5, 36, '2', 'autre', 's'); text(ax, 56.7, 36, '3', 'resultat', 's')
text(ax, 44, 27, 'le cas ne montre pas', 'fixe', 'm')
d = 4.5
for k in range(4): box(ax, 8 + k * d, 14, d, d, 'fixe', fill=False, dash=True, r=0.3, lw=0.6)
for k in range(8): box(ax, 34 + k * d, 14, d, d, 'fixe', fill=False, dash=True, r=0.3, lw=0.6)
text(ax, 17, 9, '4', 'fixe', 's'); text(ax, 52, 9, '8', 'fixe', 's')
save(fig, '50-104')
