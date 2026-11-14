import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
text(ax, 22, 74, 'tableau : 4 essais', 'sujet', 'm'); text(ax, 66, 74, 'calcul : 5 lignes', 'autre', 'm')
for i in range(4):
    box(ax, 16, 62 - i * 10, 12, 7, 'sujet', label=str(i + 1))
for i in range(5):
    box(ax, 60, 62 - i * 10, 12, 7, 'autre', label=str(i + 1))
box(ax, 30, 6, 28, 9, 'resultat', label=r'$C=a$', weight='bold')
arrow(ax, (22, 31), (36, 16.5), 'varie'); arrow(ax, (66, 21), (52, 16.5), 'varie')
line(ax, [(22, 23), (22, 19)], 'varie') if False else None
save(fig, '80-460')
