import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for y, unit, a, b in [(38, 'en mètres', '3 m', '5 m'), (8, 'en centimètres', '300 cm', '500 cm')]:
    text(ax, 4, y + 16, unit, 'fixe', 's', ha='left')
    box(ax, 4, y + 7, 18, 7, 'sujet', label=a, size='s', r=0.3)
    box(ax, 4, y - 1, 30, 7, 'varie', label=b, size='s', r=0.3)
text(ax, 66, 43, '3 ÷ 5 = 0,6', 'resultat', 's'); text(ax, 66, 13, '300 ÷ 500 = 0,6', 'resultat', 's')
text(ax, 66, 28, 'même rapport', 'encre', 's')
save(fig, '09-013')
