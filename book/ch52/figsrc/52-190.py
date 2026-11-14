import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, r'$a = 3$ : reste par $m = 4$', 'sujet', 'm')
for i in range(4):
    box(ax, 19 + i * 12.5, 34, 11.5, 11, 'sujet' if i == 3 else 'fixe', label=str(i))
text(ax, 44, 26, r'$b = 4$ : reste par $n = 5$', 'autre', 'm')
for i in range(5):
    box(ax, 12 + i * 12.5, 8, 11.5, 11, 'autre' if i == 4 else 'fixe', label=str(i))
save(fig, '52-190')
