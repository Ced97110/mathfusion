import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, '312, 297, 305, 288', 'sujet', 'm')
rows = [('1 repérer', 'proches de 300', 'varie'), ('2 remplacer', 'chacun → 300', 'varie'),
        ('3 additionner', '4 × 300 = 1 200', 'varie'), ('4 calculer', 'somme exacte : 1 202', 'sujet'),
        ('5 mesurer', '1 200 − 1 202 = −2', 'resultat')]
for i, (v, c, r) in enumerate(rows):
    y = 60 - 12 * i
    box(ax, 3, y, 26, 9, r, label=v)
    box(ax, 33, y, 52, 9, r, label=c, fill=False)
    if i: arrow(ax, (16, y + 12), (16, y + 9), 'fixe')
save(fig, '10-079')
