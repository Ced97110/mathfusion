import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 18, 70, r'$H$ contient $K$', 'sujet', 's', weight='bold')
text(ax, 70, 70, r'sous-groupes de $G/K$', 'autre', 's', weight='bold')
L = [r'$\langle 6\rangle=K$', r'$\langle 3\rangle$', r'$\langle 2\rangle$', r'$\langle 1\rangle=G$']
R = ['1 paquet', '2 paquets', '3 paquets', '6 paquets']
for i in range(4):
    y = 50 - i * 14
    box(ax, 2, y, 30, 9, 'sujet', label=L[i], size='s')
    box(ax, 56, y, 28, 9, 'autre', label=R[i], size='s')
    arrow(ax, (32.5, y + 4.5), (55.5, y + 4.5), 'varie')
text(ax, 44, 63, r'$H\mapsto H/K$', 'varie', 's')
text(ax, 44, 4, '4 sous-groupes ↔ 4 sous-groupes', 'resultat', 's')
save(fig, '48-090')
