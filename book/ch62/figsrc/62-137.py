import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 74.5, 77, 'reste', 'encre', 's')
# division 1 : f par f'
box(ax, 2, 62, 24, 10, 'sujet', label=r'$x^3-3x+2$', size='s')
text(ax, 29, 67, '÷', 'encre', 'l')
box(ax, 32, 62, 22, 10, 'varie', label=r'$3x^2-3$', size='s')
arrow(ax, (55, 67), (63, 67), 'fixe', lw=1.0)
box(ax, 64, 62, 22, 10, 'fixe', label=r'$-2x+2$', size='s')
text(ax, 44, 56, 'reste ≠ 0 : on continue', 'fixe', 's')
# division 2 : f' par x - 1
box(ax, 2, 34, 24, 10, 'varie', label=r'$3x^2-3$', size='s')
text(ax, 29, 39, '÷', 'encre', 'l')
box(ax, 32, 34, 22, 10, 'resultat', label=r'$x-1$', size='s')
arrow(ax, (55, 39), (63, 39), 'fixe', lw=1.0)
box(ax, 64, 34, 22, 10, 'resultat', label='0', size='s')
text(ax, 75, 30, 'reste 0 :', 'resultat', 's')
text(ax, 75, 26.5, 'on s’arrête', 'resultat', 's')
# le diviseur 2 vient du reste 1, divisé par -2
arrow(ax, (72, 62), (50, 45), 'varie', lw=0.9, curve=-0.2)
text(ax, 77, 52, r'$\div\,(-2)$', 'varie', 's')
box(ax, 22, 6, 44, 11, 'resultat', label=r'PGCD $=x-1$')
arrow(ax, (43, 34), (43, 18), 'resultat', lw=1.0)
save(fig, '62-137')
