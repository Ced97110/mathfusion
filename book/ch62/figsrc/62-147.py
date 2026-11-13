import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
# tour de deux étages de degré 2 ; à droite, la base de 4 éléments
text(ax, 22, 82, '2i ÷ 2 = i : même corps', 'encre', 's')
box(ax, 2, 52, 40, 14, 'resultat', label='ℚ(√2, i)\n= ℚ(√2, 2i)', size='s')
box(ax, 2, 30, 40, 10, 'sujet', label='ℚ(√2)', size='s')
box(ax, 2, 8, 40, 10, 'fixe', label='ℚ', size='s')
arrow(ax, (22, 40), (22, 52), 'varie', lw=1.2)
arrow(ax, (22, 18), (22, 30), 'varie', lw=1.2)
text(ax, 25, 46, 'ajouter i : ×2', 'varie', 's', ha='left')
text(ax, 25, 24, 'ajouter √2 : ×2', 'varie', 's', ha='left')
text(ax, 67, 70, 'base de ℚ(√2, i)', 'resultat', 's')
cells = [('1', 55, 56), ('√2', 71, 56), ('i', 55, 42), ('√2 i', 71, 42)]
for l, x, y in cells:
    box(ax, x, y, 14, 10, 'resultat', label=l, size='s')
text(ax, 70, 34, '4 éléments', 'resultat', 's')
text(ax, 70, 18, r'$2\times2=4$', 'resultat', 'l', weight='bold')
text(ax, 70, 12, 'degré du corps', 'resultat', 's')
save(fig, '62-147')
