import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
y, h = 24, 9
text(ax, 44, 55, 'diag(1, 6)', 'encre', 'm', weight='bold')
# premier morceau : réduit à 0
box(ax, 8, y, 12, h, 'fixe', fill=False, dash=True, label='0', size='s')
text(ax, 14, y + h + 4, 'Dy₁ = {0}', 'fixe', 's')
text(ax, 14, y - 5, 'd₁ = 1 : 1·y₁ = 0', 'fixe', 's')
# second morceau : 6 éléments
x0, cw = 36, 8.0
for i in range(6):
    box(ax, x0 + i * cw, y, cw, h, 'sujet', r=0.3)
text(ax, x0 + 3 * cw, y + h + 4, 'Dy₂ : 6 éléments', 'sujet', 's')
text(ax, x0 + 3 * cw, y - 5, 'd₂ = 6 : 6·y₂ = 0', 'sujet', 's')
text(ax, 44, 8, '(1) = ℤ : générateur supprimé', 'fixe', 's')
save(fig, '59-106')
