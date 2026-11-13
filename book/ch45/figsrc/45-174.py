import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 3, 42, 28, 11, 'fixe', label=r'$G\times H$'); text(ax, 44.5, 47.5, '=', 'sujet', 'xl'); box(ax, 58, 42, 28, 11, 'sujet', label=r'$G\oplus H$')
text(ax, 17, 38, 'produit direct', 'fixe', 's'); text(ax, 72, 38, 'somme directe', 'sujet', 's')
box(ax, 3, 21, 83, 10, 'autre', label='G, H abéliens, notés avec +')
box(ax, 8, 4, 73, 10, 'resultat', label='(1, 2) + (1, 1) = (0, 0)')
save(fig, '45-174')
