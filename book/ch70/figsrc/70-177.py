import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 65, 'paramètres', 'fixe', 's'); text(ax, 62, 65, 'à éliminer', 'varie', 's')
for i, (nm, role) in enumerate(((r'$x_1$', 'fixe'), (r'$x_2$', 'fixe'), (r'$x_3$', 'varie'), (r'$x_4$', 'varie'))):
    box(ax, 4 + 20 * i, 52, 16, 9, role, label=nm)
arrow(ax, (12, 51), (12, 40), 'fixe')
text(ax, 17, 45.5, 'on élimine x₃ et x₄ (Seidenberg)', 'varie', 's', ha='left')
box(ax, 4, 30, 16, 9, 'fixe', label=r'$x_1$'); box(ax, 24, 30, 16, 9, 'varie', label=r'$x_2$')
text(ax, 44, 34.5, 'condition sur x₁ et x₂', 'encre', 's', ha='left')
arrow(ax, (12, 29), (12, 17), 'fixe')
text(ax, 17, 23.5, 'on élimine x₂ ; Sturm décide', 'varie', 's', ha='left')
box(ax, 4, 8, 16, 9, 'sujet', label=r'$x_1$')
text(ax, 24, 12.5, 'condition sur x₁ seule', 'encre', 's', ha='left')
save(fig, '70-177')
