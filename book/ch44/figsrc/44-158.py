import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
x0 = 30
for r in range(2):
    for c in range(7):
        disc(ax, x0 + 6 * c, 38 - 6 * r, 2.1, 'sujet' if c < 3 else 'varie')
text(ax, 20, 35, '2 ×', 'encre', 'l')
text(ax, 44, 54, '2 × (3 + 4) = 2 × 3 + 2 × 4', 'encre', 'm')
brace(ax, x0 - 2.5, x0 + 38.5, 43, 'fixe', label='3 + 4', down=False)
brace(ax, x0 - 2.5, x0 + 14.5, 29, 'sujet', label='2 × 3 = 6')
brace(ax, x0 + 17.5, x0 + 38.5, 29, 'varie', label='2 × 4 = 8')
text(ax, 44, 12, '14 : reste 0 (mod 7)', 'resultat', 'l')
save(fig, '44-158')
