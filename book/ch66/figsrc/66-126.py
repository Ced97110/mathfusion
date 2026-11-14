import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$h(x)=x^{4}\,(x-2)^{5}$', 'encre', 'l')
box(ax, 2, 42, 18, 12, 'fixe', label=r'$x^{4}$')
text(ax, 24, 48, r'$\times$', 'encre', 'l')
box(ax, 28, 42, 34, 12, 'sujet', label=r'$(x-2)^{5}$')
text(ax, 66, 48, '=', 'encre', 'l')
box(ax, 70, 42, 16, 12, 'resultat', label=r'$h$')
for i in range(5):
    disc(ax, 31.4 + 6.8 * i, 32, 2.2, 'varie')
text(ax, 45, 24, 'racine 2 : 5 fois', 'varie', 's')
text(ax, 44, 12, r'degré $=4+5=9$', 'resultat', 'm')
save(fig, '66-126')
