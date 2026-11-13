import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = 54
text(ax, X, 70, r'$P\,A\,P^{-1}\;=\;B$', 'sujet', 'l')
arrow(ax, (6, 66), (6, 57), 'varie')
text(ax, 10, 61.5, r'on compose par $P^{-1}$ à gauche, $P$ à droite', 'varie', 's', ha='left')
text(ax, X, 51, r'$P^{-1}P\,A\,P^{-1}P\;=\;P^{-1}\,B\,P$', 'encre', 'm')
arrow(ax, (6, 47), (6, 38), 'varie')
text(ax, 10, 42.5, r'étape décisive : $P^{-1}P=I$', 'varie', 's', ha='left')
text(ax, X, 32, r'$I\,A\,I\;=\;P^{-1}\,B\,P$', 'encre', 'm')
arrow(ax, (6, 28), (6, 19), 'varie')
text(ax, 10, 23.5, r'$I$ ne change rien', 'varie', 's', ha='left')
text(ax, X, 12, r'$A\;=\;P^{-1}\,B\,P$', 'resultat', 'l')
save(fig, '43-057')
