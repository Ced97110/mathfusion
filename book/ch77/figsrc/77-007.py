import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 38, 22, 10, 'sujet', label='nombre', size='s')
arrow(ax, (24, 43), (32, 43), 'varie')
for i in range(2):
    for j in range(2):
        box(ax, 34 + i * 8, 34 + j * 9, 8, 9, 'autre', r=0.3)
text(ax, 42, 56, 'matrice', 'autre', 's')
arrow(ax, (52, 43), (58, 43), 'varie')
box(ax, 58, 36, 28, 14, 'resultat', label='déterminant\n= norme', size='s')
text(ax, 44, 24, r'norme de $3+2\sqrt{2}$ : $1$', 'resultat', 'm')
text(ax, 44, 14, r'norme de $1+3\sqrt{2}$ : $-17$', 'resultat', 'm')
text(ax, 44, 5, r'norme de $a+b\sqrt{2}$ : ?', 'varie', 'm')
save(fig, '77-007')
