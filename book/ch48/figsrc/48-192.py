import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 70, '⟨2⟩ : 6 éléments', 'sujet', 's'); text(ax, 44, 4, 'horloge à 6 : 6 éléments', 'autre', 's')
for i in range(6):
    x = 9 + i * 14
    box(ax, x - 5.5, 48, 11, 10, 'sujet', label=str(2 * i))
    box(ax, x - 5.5, 16, 11, 10, 'autre', label=str(i))
    arrow(ax, (x, 27), (x, 47), 'resultat', both=True)
text(ax, 44, 11, 'n ↔ 2 × n', 'resultat', 's')
save(fig, '48-192')
