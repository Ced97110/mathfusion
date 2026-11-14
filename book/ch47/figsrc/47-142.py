import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, 'G', 'sujet', 'xl', weight='bold')
text(ax, 50, 68, '/', 'encre', 'xl')
text(ax, 56, 68, 'N', 'varie', 'xl', weight='bold')
rows = [(r'$\mathbb{Z}\ /\ 5\mathbb{Z}$', 5), (r'$D_{4}\ /$ rotations', 2), ('horloge 12 / mult. de 3', 3)]
for k, (lab, n) in enumerate(rows):
    y = 50 - k * 17
    text(ax, 5, y + 7, lab, 'encre', 's', ha='left')
    for i in range(n):
        box(ax, 5 + i * 11, y - 5, 10, 9, 'resultat')
    text(ax, 76, y - 0.5, f'{n} classes', 'resultat', 's')
text(ax, 44, 3, r'$|G/N|=|G|\ \div\ |N|$', 'encre', 's')
save(fig, '47-142')
