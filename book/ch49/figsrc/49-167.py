import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 96, 'Groupe : 8 éléments', 'resultat', 's')
for i in range(4):
    x = 6 + i * 20.5
    box(ax, x, 76, 18, 10, 'resultat'); disc(ax, x + 5.5, 81, 2.3, 'resultat'); disc(ax, x + 12.5, 81, 2.3, 'resultat')
text(ax, 44, 68, '4 classes égales : 4 divise 8', 'resultat', 's')
text(ax, 44, 56, 'Monoïde : 5 éléments', 'limite', 's')
for i in range(5):
    disc(ax, 14 + i * 15.5, 34, 5, 'fixe' if i == 0 else 'limite', label=str(i), size='m')
brace(ax, 14 + 15.5 - 5, 14 + 4 * 15.5 + 5, 41, 'limite', label='orbite de 1 : 4 points', down=False)
text(ax, 44, 14, '4 ne divise pas 5', 'limite', 'm')
save(fig, '49-167')
