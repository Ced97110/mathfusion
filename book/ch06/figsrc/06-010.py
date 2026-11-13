import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 16, 42, '1', 'sujet', 'l')
line(ax, [(10, 37.5), (22, 37.5)], 'encre', lw=1.2)
text(ax, 16, 33, '4', 'fixe', 'l')
arrow(ax, (25, 42), (46, 42), 'sujet')
text(ax, 62, 42, '1 morceau pris', 'sujet')
arrow(ax, (25, 33), (44, 33), 'fixe')
text(ax, 62, 33, '4 morceaux faits', 'fixe')
for j in range(4):
    box(ax, 8 + j * 18, 10, 18, 9, 'sujet' if j == 0 else 'fixe', r=0.3)
brace(ax, 8, 80, 10, 'fixe', "4 morceaux égaux : l'unité")
save(fig, '06-010')
