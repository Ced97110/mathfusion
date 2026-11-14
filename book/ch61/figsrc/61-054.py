import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
disc(ax, 44, 48, 8, 'sujet', label=r'$\sqrt{2}$', size='l')
box(ax, 5, 18, 34, 12, 'resultat', label=r'$x^2-2$', size='l')
box(ax, 49, 18, 34, 12, 'fixe', label=r'$x^4-4$', size='l')
arrow(ax, (38, 44), (22, 30.5), 'varie'); arrow(ax, (50, 44), (66, 30.5), 'varie')
text(ax, 22, 12, 'degré 2 : minimal', 'resultat', 's'); text(ax, 66, 12, 'degré 4 : plus gros', 'fixe', 's')
text(ax, 44, 4, 'tous deux nuls en $\\sqrt{2}$', 'varie', 's')
save(fig, '61-054')
