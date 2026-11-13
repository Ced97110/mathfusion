import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for i in range(2):
    for j in range(2): box(ax, 22 + i * 17, 14 + j * 17, 15, 15, 'resultat', label=str(2 * j + i + 1), size='m')
brace(ax, 22, 54, 12, 'varie', label=r'étage 1 : degré 2', size='s')
line(ax, [(57, 14), (59, 14), (59, 46), (57, 46)], 'varie')
text(ax, 62, 30, 'étage 2', 'varie', 's', ha='left'); text(ax, 62, 25, 'degré 2', 'varie', 's', ha='left')
text(ax, 44, 51, r'$2 \times 2 = 4$ briques', 'resultat', 'm')
save(fig, '61-123')
