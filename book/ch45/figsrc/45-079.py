import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
for k in range(4):
    y = 66 - k * 14
    box(ax, 4, y, 34, 10, 'sujet', label=f'{k} devient {(k + 1) % 4}', size='s')
line(ax, [(41, 76), (44, 76), (44, 34), (41, 34)], 'fixe', lw=1.0)
arrow(ax, (44, 55), (52, 55), 'varie')
box(ax, 53, 45, 31, 20, 'resultat', label=r'$a_L$', size='xl')
text(ax, 68.5, 38, 'une règle : ajouter 1', 'varie', 's')
text(ax, 68.5, 31, r'$x \mapsto a\,x$', 'encre', 's')
text(ax, 44, 12, r'se lit « $a$ indice $L$ »', 'sujet', 's')
text(ax, 44, 5, 'application, pas un nombre', 'encre', 's')
save(fig, '45-079')
