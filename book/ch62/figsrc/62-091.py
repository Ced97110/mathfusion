import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'corps à deux éléments : $1+1=0$', 'fixe', 's')
text(ax, 44, 62, r'$f=x^3+x+1$', 'sujet', 'm')
rows = [(48, r'$x^3$', r'$3x^2=x^2$'), (34, r'$x$', r'$1$'), (20, r'$1$', r'$0$')]
for y, a, b in rows:
    box(ax, 4, y, 24, 10, 'sujet', label=a)
    arrow(ax, (29, y + 5), (47, y + 5), 'varie')
    box(ax, 48, y, 36, 10, 'resultat', label=b)
text(ax, 66, 12.5, 'le terme constant disparaît', 'varie', 's', ha='center')
box(ax, 24, 1, 40, 8, 'resultat', label=r'$f^\prime=x^2+1$', size='m')
save(fig, '62-091')
