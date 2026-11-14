import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 78, 'Horloge à 4 heures', 'encre', 'm')
for i in range(4):
    box(ax, 6 + i * 20, 58, 16, 11, 'fixe', label=str(i), dash=(i >= 2), fill=(i < 2))
arrow(ax, (14, 58), (14, 36), 'fixe')
arrow(ax, (34, 58), (34, 36), 'fixe')
text(ax, 38, 47, 'on garde 0 et 1', 'fixe', 's', ha='left')
els = ['0', '1', r'$\alpha$', r'$\alpha+1$']
for i in range(4):
    box(ax, 6 + i * 20, 25, 16, 11, 'fixe' if i < 2 else 'varie', label=els[i])
brace(ax, 46, 82, 25, 'varie', label='deux éléments nouveaux')
text(ax, 44, 8, 'Corps à quatre éléments', 'sujet', 'm')
save(fig, '67-008')
