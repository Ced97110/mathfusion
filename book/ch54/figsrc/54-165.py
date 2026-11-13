import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$f=x^3-2x^2+4$', 'fixe', 'm')
# divisé par x - 1
box(ax, 4, 18, 38, 46, 'sujet')
text(ax, 23, 58, r'divisé par $x-1$', 'sujet', 's')
text(ax, 23, 48, r'$f(1)=1-2+4$', 'sujet', 's')
text(ax, 23, 40, r'$f(1)=3$', 'sujet', 'm')
text(ax, 23, 30, 'reste', 'sujet', 's')
box(ax, 14, 20, 18, 7, 'resultat', label='3', size='m')
# divisé par x - 2
box(ax, 46, 18, 38, 46, 'autre')
text(ax, 65, 58, r'divisé par $x-2$', 'autre', 's')
text(ax, 65, 48, r'$f(2)=8-8+4$', 'autre', 's')
text(ax, 65, 40, r'$f(2)=4$', 'autre', 'm')
text(ax, 65, 30, 'reste', 'autre', 's')
box(ax, 56, 20, 18, 7, 'resultat', label='4', size='m')
text(ax, 44, 8, 'chaque diviseur a son reste', 'encre', 's')
save(fig, '54-165')
