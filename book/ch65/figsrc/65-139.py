import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
conds = ['1. irréductible', '2. deux racines non réelles', '3. degré 5, premier']
for i, c in enumerate(conds):
    y = 70 - i * 15
    box(ax, 4, y, 80, 11, 'sujet', label='✓  ' + c, size='s')
    arrow(ax, (44, y), (44, y - 4), 'varie')
box(ax, 4, 14, 80, 11, 'resultat', label=r'groupe de $x^5-4x+2$ : $S_5$')
arrow(ax, (44, 14), (44, 9), 'varie')
text(ax, 44, 4, 'non résoluble : pas de radicaux', 'limite', 's')
text(ax, 44, 84, 'trois conditions réunies', 'sujet', 's')
save(fig, '65-139')
