import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 4, 20, 80, 34, 'sujet', fill=False)
text(ax, 44, 50, 'ker $\\eta$ : multiples de 6', 'sujet', 's')
disc(ax, 20, 36, 7, 'sujet', label='30'); disc(ax, 68, 36, 7, 'resultat', label='210')
arrow(ax, (27, 36), (61, 36), 'varie'); text(ax, 44, 40, r'$\times\,7$', 'varie')
text(ax, 20, 12, "$\\eta(30) = 0'$", 'sujet', 's'); text(ax, 68, 12, "$\\eta(210) = 0'$", 'resultat', 's')
text(ax, 68, 25, '210 = 35 × 6', 'resultat', 's'); text(ax, 44, 3, 'le noyau absorbe le produit', 'varie', 's')
save(fig, '52-148')
