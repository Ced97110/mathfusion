import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 34, 28, 20, 'fixe', label=r'$7 + 5 = 12$', size='m')
text(ax, 16, 60, 'proposition', 'fixe', 'm'); text(ax, 16, 28.5, 'non mise en avant', 'fixe', 's')
box(ax, 36, 34, 50, 20, 'sujet')
text(ax, 61, 47, 'angles d’un triangle', 'sujet', 'm'); text(ax, 61, 40, r'somme $= 180°$', 'sujet', 'm')
text(ax, 61, 60, 'théorème : important', 'sujet', 'm', weight='bold')
for i, x in enumerate((38, 54, 70)):
    box(ax, x, 6, 16, 8, 'resultat', label='calcul', size='s')
    arrow(ax, (61, 33), (x + 8, 15.5), 'varie')
text(ax, 61, 20.5, 'utilisé dans beaucoup de', 'varie', 's') if False else None
text(ax, 16, 10, 'utilisé ici', 'fixe', 's') if False else None
save(fig, '42-102')
