import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
# départ
box(ax, 4, 66, 80, 18, 'fixe')
text(ax, 44, 78, r'$x^2+3x+1=(x-2)(x+5)+r$', 'fixe', 'm')
text(ax, 44, 70, r'diviseur de degré 1 : $r$ est une constante', 'fixe', 's')
arrow(ax, (44, 66), (44, 52), 'varie', lw=1.6)
text(ax, 48, 59, r'on remplace $x$ par 2', 'varie', 's', ha='left')
# étape qui porte le poids
box(ax, 4, 30, 80, 22, 'varie', lw=1.6)
text(ax, 44, 46, r'$2^2+3\cdot2+1=0\times7+r$', 'varie', 'm')
text(ax, 44, 36, r'$(x-2)$ devient $0$ : le terme disparaît', 'varie', 's')
arrow(ax, (44, 30), (44, 18), 'varie')
# arrivée
box(ax, 4, 4, 80, 14, 'resultat')
text(ax, 44, 11, r'$11=r$ : le reste est $f(2)$', 'resultat', 'm')
save(fig, '54-164')
