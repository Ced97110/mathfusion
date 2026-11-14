import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
bw, st, x0, y = 5, 5.8, 3, 20
labs = {0: r'$\sqrt{2}$', 1: r'$\sqrt{3}$', 2: r'$\sqrt{5}$'}
for i in range(10): box(ax, x0 + i * st, y, bw, 8, 'sujet', label=labs.get(i), size='s', r=0.5)
for j in range(3): box(ax, x0 + (10 + j) * st + 1.5, y, bw, 8, 'limite', fill=False, dash=True, r=0.5)
arrow(ax, (x0 + 12 * st + bw + 3, y + 4), (85, y + 4), 'limite')
brace(ax, x0, x0 + 9 * st + bw, y, 'sujet', '10 réels : liste finie', down=True)
text(ax, 70, y + 12, 'toujours d\'autres', 'limite', 's')
text(ax, 44, 42, r'$[\mathbb{R}:\mathbb{Q}]=\infty$', 'limite', 'xl', weight='bold')
save(fig, '61-048')
