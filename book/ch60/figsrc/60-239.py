import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
rows = [('4, 27, 5', '540'), ('2, 2, 27, 5', '2, 270'), ('4, 9, 3, 5', '3, 180'),
        ('2, 2, 9, 3, 5', '6, 90'), ('4, 3, 3, 3, 5', '3, 3, 60'), ('2, 2, 3, 3, 3, 5', '3, 6, 30')]
text(ax, 24, 92, 'diviseurs élémentaires', 'autre', 'm', weight='bold')
text(ax, 68, 92, 'facteurs invariants', 'sujet', 'm', weight='bold')
for i, (e, d) in enumerate(rows):
    y = 76 - 12 * i
    hi = (e == '4, 3, 3, 3, 5')
    box(ax, 3, y, 42, 9, 'varie' if hi else 'autre', label=e)
    box(ax, 55, y, 30, 9, 'varie' if hi else 'sujet', label=d)
    arrow(ax, (46, y + 4.5), (54, y + 4.5), 'fixe', both=True)
text(ax, 44, 8, 'chaque ligne : produit 540', 'resultat', 'm')
save(fig, '60-239')
