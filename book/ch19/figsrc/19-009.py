import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 38, 44, 'cahiers', 'sujet', 's'); text(ax, 70, 44, 'euros', 'varie', 's')
for y, who, a, b in [(26, 'Marie', 2, 5), (6, 'Léo', 5, 2)]:
    text(ax, 2, y + 8, who, 'encre', 'm', ha='left'); text(ax, 2, y + 2, f'« {a}, {b} »', 'fixe', 's', ha='left')
    for i in range(a): box(ax, 26 + i * 5.5, y, 4.5, 10, 'sujet', r=0.4)
    for i in range(b): disc(ax, 60 + i * 5, y + 5, 2.1, 'varie')
save(fig, '19-009')
