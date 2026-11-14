import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 10
for i in range(4): box(ax, 30 + i * u, 10, u, u, 'varie')
for j in range(3): box(ax, 70, 20 + j * u, u, u, 'sujet')
line(ax, [(30, 20), (70, 50)], 'fixe', lw=1.3)
text(ax, 13, 46, '3', 'sujet', 'xl'); line(ax, [(8, 40.5), (18, 40.5)], 'encre', lw=1.2); text(ax, 13, 35, '4', 'varie', 'xl')
text(ax, 13, 58, r'$\frac{3}{4}$ dit', 'encre', 'm')
text(ax, 50, 5, 'avancée 4 (4 cases)', 'varie', 's'); text(ax, 62, 58, 'montée 3 (3 cases)', 'sujet', 's')
save(fig, '19-094')
