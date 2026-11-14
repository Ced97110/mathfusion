import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# zone des fractions : on y reste avec les quatre opérations
box(ax, 2, 22, 58, 30, 'sujet', fill=False, dash=True)
text(ax, 31, 47, 'on reste dans ℚ', 'sujet', 's')
box(ax, 4, 28, 18, 10, 'fixe', label='3 et 1', size='s')
box(ax, 28, 28, 30, 10, 'fixe', label='3 × 3 − 4 × 1 = 5', size='s')
arrow(ax, (22.5, 33), (27.5, 33), 'fixe')
text(ax, 31, 24.5, '5 : encore dans ℚ', 'fixe', 's')
# la racine : seul geste qui sort de ℚ
box(ax, 66, 28, 18, 10, 'varie', label='√5', size='m')
arrow(ax, (58.5, 33), (65.5, 33), 'varie')
text(ax, 75, 43, 'sort de ℚ', 'varie', 's')
# résultat : encore des opérations
box(ax, 24, 4, 40, 10, 'resultat', label='(3 ± √5) / 2', size='m')
arrow(ax, (75, 27.5), (64.5, 11), 'resultat', curve=-0.2)
text(ax, 80, 17, '+ 3, ÷ 2', 'resultat', 's')
save(fig, '64-001')
