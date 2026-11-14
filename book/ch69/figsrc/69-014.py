import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
rows = [('−7', '49', 'autre', 'négatif'), ('−2', '4', 'autre', 'négatif'), ('1,5', '2,25', 'sujet', 'positif'), ('10', '100', 'sujet', 'positif')]
text(ax, 19, 54, 'départ', 'encre', 'm')
text(ax, 69, 54, 'carré', 'encre', 'm')
for i, (a, c, role, sg) in enumerate(rows):
    y = 40 - 12 * i
    box(ax, 4, y, 30, 8, role, label=f'{a}  ({sg})')
    arrow(ax, (34, y + 4), (54, y + 4), 'varie')
    box(ax, 54, y, 30, 8, 'resultat', label=f'{c}  (positif)')
save(fig, '69-014')
