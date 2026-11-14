import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 10, 14, 68, 56, 'fixe')
line(ax, [(10, 14), (78, 14)], 'fixe', lw=2.0)
text(ax, 44, 74, 'faîtage (haut du toit)', 'fixe', 's')
text(ax, 44, 8, 'gouttière (bord bas)', 'fixe', 's')
bx = 44
arrow(ax, (bx, 14), (bx, 66), 'sujet', lw=2.0)
s = 4
line(ax, [(bx, 14 + s), (bx + s, 14 + s), (bx + s, 14)], 'encre', lw=0.7)
line(ax, [(12, 36), (76, 36)], 'autre', lw=1.6, dash=True)
arrow(ax, (bx - 14, 14), (bx + 20, 56), 'varie', lw=1.4)
text(ax, bx - 2.5, 56, 'plus grande pente', 'sujet', 's', rot=90, ha='right')
text(ax, 13, 32.8, 'niveau :', 'autre', 's', ha='left')
text(ax, 13, 29.4, 'même hauteur', 'autre', 's', ha='left')
text(ax, 73, 58, 'en biais', 'varie', 's', ha='right')
save(fig, '27-053')
