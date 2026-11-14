import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, 'symétries du carré : 8', 'encre', 's')
text(ax, 12, 62, 'centre : 2', 'sujet', 's')
for i in range(4):
    x = 4 + 20.5 * i; r = 'sujet' if i == 0 else 'fixe'
    box(ax, x, 46, 16, 10, r)
    disc(ax, x + 5, 51, 1.6, r); disc(ax, x + 11, 51, 1.6, r)
    arrow(ax, (x + 8, 44), (x + 8, 31), 'varie')
    box(ax, x + 3, 19, 10, 10, 'resultat')
text(ax, 44, 12, 'quotient : 4 éléments', 'resultat', 's')
text(ax, 44, 6, 'abélien', 'resultat', 'm', weight='bold')
save(fig, '50-247')
