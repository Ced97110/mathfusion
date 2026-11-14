import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 57, r'exposants de $(a^2)^3$', 'sujet', 'm')
for i in range(3):
    box(ax, 8 + i*16, 38, 10, 10, 'sujet', label='2')
    if i < 2: text(ax, 21 + i*16, 43, '+', 'encre', 'l')
text(ax, 60, 43, '= 6', 'resultat', 'l', ha='left', weight='bold')
arrow(ax, (29, 36), (29, 22), 'varie')
text(ax, 34, 29, 'addition répétée', 'varie', 's', ha='left')
box(ax, 12, 8, 34, 12, 'resultat', label=r'$3 \times 2 = 6$', size='l')
save(fig, '14-044')
