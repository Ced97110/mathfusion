import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 3, 8, 56, 52, 'sujet', fill=False)
text(ax, 31, 55, r'$O(3)$', 'sujet', 'm')
box(ax, 8, 12, 46, 34, 'resultat')
text(ax, 31, 40, 'la matrice qui décale', 'resultat', 's')
text(ax, 31, 31, '(4, 5, 6) → (5, 6, 4)', 'fixe', 's')
text(ax, 31, 19, r'$A^{-1} = A^t$', 'resultat', 'm')
box(ax, 63, 12, 23, 34, 'limite')
text(ax, 74.5, 40, 'cisaille-', 'limite', 's'); text(ax, 74.5, 35, 'ment', 'limite', 's')
text(ax, 74.5, 22, r'$A^{-1} \neq A^t$', 'limite', 's')
text(ax, 74.5, 52, 'hors de l\'ensemble', 'limite', 's', ha='center') if False else None
save(fig, '73-137')
