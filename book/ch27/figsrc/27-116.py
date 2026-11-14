import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
line(ax, [(6, 6), (82, 6)], 'fixe', lw=1.4)
text(ax, 44, 2.2, 'charnière', 'fixe', 's')
for i, y in enumerate((20, 34, 48)):
    line(ax, [(8, y), (62, y)], 'sujet', lw=1.4)
text(ax, 72, 34, 'lignes de\nniveau', 'sujet', 's')
arrow(ax, (14, 8), (14, 56), 'varie', lw=1.2)
text(ax, 16, 56, 'plus grande pente', 'varie', 's', ha='left')
brace(ax, 8, 62, 22, 'resultat', label='même hauteur', down=False)
save(fig, '27-116')
