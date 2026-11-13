import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, 'corps pour $x^2-2$ sur les fractions', 'encre', 'm')
box(ax, 6, 8, 36, 14, 'limite', label='ℚ : pas de produit', size='s')
line(ax, [(2, 28), (74, 28)], 'varie', lw=1.2, dash=True)
text(ax, 80, 28, 'seuil\n(i)', 'varie', 's')
for i, (nm, y) in enumerate([('ℚ(√2)', 34), ('ℝ', 44), ('ℂ', 54)]):
    box(ax, 6, y, 36, 8.5, 'resultat', label=f'{nm} : $f$ se casse', size='s')
arrow(ax, (56, 12), (56, 64), 'fixe', lw=1.0)
text(ax, 70, 38, 'plus gros :\npas de limite', 'fixe', 's')
text(ax, 24, 3, 'en dessous : exclu', 'limite', 's')
save(fig, '62-031')
