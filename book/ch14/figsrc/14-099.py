import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
box(ax, 3, 70, 38, 14, 'sujet', label=r'48 000 $\approx 5 \times 10^4$', size='s')
box(ax, 47, 70, 38, 14, 'autre', label=r'0,0002 $= 2 \times 10^{-4}$', size='s')
arrow(ax, (22, 70), (22, 60), 'varie'); arrow(ax, (66, 70), (66, 60), 'varie')
text(ax, 22, 63.5, 'mantisses', 'sujet', 's', ha='left') if False else None
box(ax, 3, 46, 38, 13, 'sujet', label=r'$5 \times 2 = 10$', size='m')
box(ax, 47, 46, 38, 13, 'fixe', label=r'$4 + (-4) = 0$', size='m')
text(ax, 22, 41, 'petit produit', 'sujet', 's'); text(ax, 66, 41, 'petite somme', 'fixe', 's')
arrow(ax, (22, 38), (38, 26), 'resultat'); arrow(ax, (66, 38), (50, 26), 'resultat')
box(ax, 24, 12, 40, 13, 'resultat', label=r'$10 \times 10^0 = 10$', size='m')
text(ax, 44, 5, 'calcul exact : 9,6', 'fixe', 's')
save(fig, '14-099')
