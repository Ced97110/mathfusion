import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
text(ax, 44, 46, r'$A=\mathrm{diag}(2,\ \frac{1}{2})$', 'varie', 'l')
box(ax, 5, 20, 20, 16, 'sujet', label='800 px', size='s')
box(ax, 45, 20, 40, 8, 'resultat', label='400 px', size='s')
text(ax, 15, 16, '1 000 px', 'sujet', 's'); text(ax, 65, 16, '2 000 px', 'resultat', 's')
arrow(ax, (27, 28), (43, 28), 'varie')
text(ax, 35, 32, 'largeur × 2', 'varie', 's'); text(ax, 35, 23.5, 'hauteur ÷ 2', 'varie', 's')
text(ax, 15, 10, 'aire 800 000', 'sujet', 's'); text(ax, 65, 10, 'aire 800 000', 'resultat', 's')
text(ax, 44, 3, r'$2\times\frac{1}{2}=1$', 'encre', 'm')
save(fig, '73-148')
