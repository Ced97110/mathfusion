import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 38, 54, 'inversibles', 'sujet', 's'); text(ax, 76, 54, 'déterminant 1', 'resultat', 's')
for y, lab, a, d, b in [(40, 'q = 3, n = 2', 48, 2, 24), (26, 'q = 5, n = 2', 480, 4, 120), (12, 'q = 2, n = 3', 168, 1, 168)]:
    text(ax, 2, y, lab, 'encre', 's', ha='left')
    box(ax, 32, y - 5, 14, 10, 'sujet', label=str(a))
    arrow(ax, (47, y), (55, y), 'varie')
    text(ax, 56, y, f'÷ {d}', 'varie', 's', ha='left')
    arrow(ax, (64, y), (68, y), 'varie')
    box(ax, 69, y - 5, 17, 10, 'resultat', label=str(b))
save(fig, '75-115')
