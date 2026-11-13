import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 4, 54, 80, 9, 'sujet', label=r'$\theta$ = 0,6109 rad = 35°   cos $\theta$ = 0,8192')
# ligne fausse
box(ax, 4, 30, 46, 14, 'limite', label='90 − 0,6109 = 89,3891')
box(ax, 58, 30, 26, 14, 'limite', label='sin = 0,9893')
arrow(ax, (50, 37), (58, 37), 'limite')
text(ax, 27, 47, 'avec 90 en radians', 'limite', 's')
text(ax, 71, 47, '≠ 0,8192', 'limite', 's')
# ligne vraie
box(ax, 4, 6, 46, 14, 'resultat', label='1,5708 − 0,6109 = 0,9599')
box(ax, 58, 6, 26, 14, 'resultat', label='sin = 0,8192')
arrow(ax, (50, 13), (58, 13), 'resultat')
text(ax, 27, 23, 'avec π/2 = 1,5708', 'resultat', 's')
text(ax, 71, 23, '= cos θ', 'resultat', 's')
save(fig, '31-083')
