import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [(r'$d_1=1$', 'aucune trace', 'fixe'),
        (r'$d_2=3$', r'horloge à 3 heures : $\mathbb{Z}/3$', 'resultat'),
        (r'$d_3=6$', r'horloge à 6 heures : $\mathbb{Z}/6$', 'resultat'),
        (r'$d_4=0$', r'une copie de $\mathbb{Z}$', 'autre')]
for k, (a, b, role) in enumerate(rows):
    y = 64 - k * 15
    box(ax, 2, y, 24, 10, 'sujet', label=a, size='m')
    arrow(ax, (27, y + 5), (36, y + 5), 'varie')
    box(ax, 38, y, 48, 10, role, label=b, size='s')
text(ax, 44, 5, r'$\mathbb{Z}/3\oplus\mathbb{Z}/6\oplus\mathbb{Z}$', 'resultat', 'm', weight='bold')
save(fig, '59-142')
