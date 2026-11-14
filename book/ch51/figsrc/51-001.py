import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [('entiers', '2×(3+4) = 2×7 = 14', '2×3+2×4 = 6+8 = 14'),
        ('polynômes', 'x×(x+2)', 'x×x + x×2'),
        ('cadran 4 h', '3×(2+3) = 3×1 = 3', '3×2+3×3 = 2+1 = 3')]
text(ax, 36, 55, "somme d'abord", 'sujet', 's')
text(ax, 73, 55, "chaque terme d'abord", 'varie', 's')
for i, (nom, g, d) in enumerate(rows):
    y = 38 - 16 * i
    text(ax, 2, y + 5.5, nom, 'encre', 's', ha='left', weight='bold')
    box(ax, 21, y, 30, 11, 'sujet', label=g, size='s')
    box(ax, 59, y, 27, 11, 'varie', label=d, size='s')
    text(ax, 55, y + 5.5, '=', 'resultat', 'l', weight='bold')
save(fig, '51-001')
