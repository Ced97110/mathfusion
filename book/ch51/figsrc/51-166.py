import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$a_{11}a_{22}-a_{12}a_{21}$', 'encre', 'm')
for (cx, cy, v) in [(6, 32, '1'), (20, 32, '2'), (6, 18, '3'), (20, 18, '4')]:
    box(ax, cx, cy, 14, 14, 'fixe')
    text(ax, cx + 7, cy + 7, v, 'encre', 'l')
arrow(ax, (9.5, 35.5), (30.5, 21.5 - 0.0), 'sujet', lw=1.3) if False else None
arrow(ax, (10, 39 - 3), (24, 25 + 3), 'sujet', lw=1.4)
arrow(ax, (24, 39 - 3), (10, 25 + 3), 'autre', lw=1.4)
text(ax, 40, 50, 'diagonale qui descend', 'sujet', 's', ha='left')
text(ax, 40, 44, r'$1\times 4=4$', 'sujet', 'm', ha='left')
text(ax, 40, 36, 'autre diagonale', 'autre', 's', ha='left')
text(ax, 40, 30, r'$2\times 3=6$', 'autre', 'm', ha='left')
text(ax, 40, 22, 'on soustrait', 'resultat', 's', ha='left')
text(ax, 40, 15, r'$4-6=-2$', 'resultat', 'l', ha='left')
save(fig, '51-166')
