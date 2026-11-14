import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 22, 44, 'cahiers', 'sujet', 's'); text(ax, 70, 44, 'prix', 'resultat', 's')
for y, n, p, who in [(26, 1, 3, 'Marie'), (6, 4, 9, 'Léo')]:
    text(ax, 2, y + 5, who, 'encre', 'm', ha='left')
    for i in range(n): box(ax, 22 + i * 7, y, 6, 10, 'sujet')
    arrow(ax, (52, y + 5), (60, y + 5), 'varie')
    box(ax, 62, y, 20, 10, 'resultat', label=f'{p} €', size='l')
text(ax, 44, 20, 'le prix change avec les cahiers', 'varie', 's')
save(fig, '19-002')
