import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(60)
text(ax, 44, 54, 'classe de 100 : {100, 011}', 'encre', 's')
for y, word, n, role in ((32, '100', 1, 'sujet'), (10, '011', 2, 'fixe')):
    box(ax, 6, y, 18, 8, role, label=word)
    for k in range(n):
        disc(ax, 33 + 5.5 * k, y + 4, 1.8, role)
    text(ax, 50, y + 4, f'poids {n}', role, 's', ha='left')
text(ax, 76, 36, 'chef', 'sujet', 'm', weight='bold')
save(fig, '68-163')
