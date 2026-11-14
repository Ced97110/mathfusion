import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 86, r'$a_L(x)=a\,x$', 'encre', 'l')
box(ax, 4, 66, 14, 9, 'sujet', label=r'$x$'); arrow(ax, (19, 70.5), (31, 70.5), 'varie')
box(ax, 32, 66, 14, 9, 'varie', label=r'$a$'); box(ax, 46, 66, 14, 9, 'sujet', label=r'$x$')
text(ax, 72, 70.5, 'a à gauche', 'varie', 's')
text(ax, 4, 54, 'École : multiplier par un nombre', 'fixe', 's', ha='left')
box(ax, 4, 41, 80, 9, 'fixe', label=r'$3\times4=12$')
text(ax, 4, 31, 'Horloge, a = 1 : ajouter 1', 'sujet', 's', ha='left')
for k in range(4):
    box(ax, 4 + k * 21, 10, 17, 17, 'sujet', label=f'{k} ↦ {(k + 1) % 4}', size='s')
text(ax, 44, 4, 'aucun élément perdu', 'resultat', 's')
save(fig, '45-076')
