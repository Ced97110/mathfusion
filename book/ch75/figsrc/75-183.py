import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 12, 66, '6 éléments', 'sujet', 's'); text(ax, 66, 66, '720 éléments', 'autre', 's')
box(ax, 50, 8, 34, 54, 'autre', r=1.5)
for i in range(6):
    y = 56 - i*8
    disc(ax, 12, y, 2.2, 'sujet'); disc(ax, 60, y, 2.2, 'autre')
    arrow(ax, (14.8, y), (57, y), 'resultat', lw=0.8)
text(ax, 67, 24, '…', 'autre', 'l')
text(ax, 67, 12, 'sans partenaire', 'limite', 's')
text(ax, 12, 8, 'une paire par élément', 'resultat', 's', ha='left')
save(fig, '75-183')
