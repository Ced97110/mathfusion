import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# écriture la plus abrégée
text(ax, 36, 66, '2 + 3 × 4²', 'encre', 'l', weight='bold')
text(ax, 72, 66, 'le plus abrégé', 'fixe', 's')
# 1. déplier 4² : 4 groupes de 4, soit 16 (échelle 1,6 mm par unité)
text(ax, 44, 58, '1. déplier 4² : 4 × 4 = 16', 'varie', 's')
for k in range(4):
    box(ax, 31.2 + 6.4 * k, 48, 6.4, 4, 'varie', r=0.2)
# 2. déplier 3 × 16 après le 2
text(ax, 44, 42, '2. 3 × 16 = 16 + 16 + 16', 'varie', 's')
box(ax, 4, 30, 3.2, 6, 'sujet', r=0.2)
text(ax, 5.6, 33, '2', 'encre', 's')
for x0 in (7.2, 32.8, 58.4):
    box(ax, x0, 30, 25.6, 6, 'varie', r=0.2)
for xc in (20, 45.6, 71.2):
    text(ax, xc, 33, '16', 'encre', 's')
# 3. additionner en dernier
text(ax, 44, 24, '3. additionner : 2 + 48', 'encre', 's')
box(ax, 4, 12, 80, 6, 'resultat', label='50', size='m', weight='bold', r=0.2)
text(ax, 44, 6, 'le moins abrégé : des +', 'fixe', 's')
save(fig, '04-063')
