import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 4, 73, 'ordre 20 :', 'encre', 's', ha='left')
box(ax, 26, 69, 11, 8, 'varie', label=r'$n_2$'); box(ax, 40, 69, 11, 8, 'varie', label=r'$n_5$')
text(ax, 44, 58, 'chaque étape commence ainsi', 'encre', 's')
for k in range(3):
    y = 40 - 10 * k
    box(ax, 6, y, 12, 7, 'varie', label=r'$n_p$')
    arrow(ax, (19, y + 3.5), (24, y + 3.5), 'fixe')
    for t in range(3): box(ax, 26 + 14 * t, y, 12, 7, 'fixe')
f = numberline(ax, 8, 76, 12, 1960, 2000, step=10)
box(ax, 8, 16, 68, 3, 'sujet', r=0.3)
save(fig, '50-254')
