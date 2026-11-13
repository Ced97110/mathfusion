import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
steps = [(2, 24, r'$4a=2a+8$'), (32, 22, r'$2a=8$'), (60, 26, r'$a=4$')]
for i, (x, wd, s) in enumerate(steps):
    box(ax, x, 42, wd, 11, 'sujet' if i == 2 else 'fixe', label=s)
arrow(ax, (26.5, 47.5), (31.5, 47.5), 'varie'); arrow(ax, (54.5, 47.5), (59.5, 47.5), 'varie')
text(ax, 73, 58, 'candidat', 'sujet', 's')
arrow(ax, (73, 41), (73, 22), 'varie')
box(ax, 20, 8, 66, 13, 'limite', label=r'$a-4=4-4=0$ : interdit')
text(ax, 25, 30, 'on remplace', 'fixe', 's', ha='center')
save(fig, '21-129')
