import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 2, 84, 62, 'fixe')
text(ax, 6, 59, 'End($R$, +)', 'fixe', 'm', ha='left')
box(ax, 8, 6, 72, 46, 'sujet')
text(ax, 14, 46, '$R_L$', 'sujet', 'l', ha='left')
text(ax, 30, 46, 'multiplications à gauche', 'sujet', 's', ha='left')
for i, lab in enumerate(['doubler', 'tripler', '× 5', '…']):
    box(ax, 14 + 16 * i, 28, 14, 10, 'sujet', label=lab, size='s')
arrow(ax, (38.5, 27.5), (38.5, 21.5), 'varie')
text(ax, 40, 18, '$a_L$ : une seule règle', 'varie', 's')
text(ax, 44, 11, 'dans ℤ : une règle par entier', 'sujet', 's')
save(fig, '57-118')
