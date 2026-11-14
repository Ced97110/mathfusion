import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, 'Programme de correction', 'encre', 'm')
text(ax, 44, 72, 'il divise un mot par un autre', 'varie', 's')
for i, w in enumerate(['00', '01', '10', '11']):
    box(ax, 8 + i * 20, 50, 16, 12, 'fixe' if i == 0 else 'sujet', label=w, size='l')
text(ax, 16, 45, 'mot nul', 'fixe', 's')
for i, w in enumerate(['01', '10', '11']):
    x = 28 + i * 20
    arrow(ax, (x + 8, 49), (x + 8, 42), 'varie')
    box(ax, x, 30, 16, 11, 'varie', label=r'$\div$ ' + w, size='m')
text(ax, 16, 35, 'pas de division', 'fixe', 's')
arrow(ax, (58, 29), (58, 21), 'varie')
text(ax, 62, 25, 'toujours possible', 'varie', 's', ha='left')
box(ax, 14, 6, 60, 13, 'resultat', label='Il faut un corps', size='m')
save(fig, '67-001')
