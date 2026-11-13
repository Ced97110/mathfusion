import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$f=x^2+3x+1$ et $a=2$', 'sujet', 'm')
# division par x - 2
text(ax, 4, 62, r'division par $x-2$ :', 'fixe', 's', ha='left')
text(ax, 38, 52, r'$f=(x-2)(x+5)+$', 'fixe', 'm')
box(ax, 66, 46, 16, 11, 'resultat', label='11', size='l')
text(ax, 74, 41, 'reste', 'resultat', 's')
# évaluation en 2
text(ax, 4, 24, r'valeur en $a=2$ :', 'fixe', 's', ha='left')
text(ax, 38, 14, r'$f(2)=4+6+1=$', 'fixe', 'm')
box(ax, 66, 8, 16, 11, 'resultat', label='11', size='l')
arrow(ax, (74, 36), (74, 22), 'varie', both=True)
text(ax, 71, 29, 'égaux', 'varie', 's', ha='right')
save(fig, '54-163')
