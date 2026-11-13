import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 26, 49, 28, 16, 'sujet', fill=False, dash=True)
text(ax, 40, 68, r'même classe $rH$', 'sujet', 's')
box(ax, 28, 51, 11, 9, 'sujet', label=r'$rs$', size='s')
box(ax, 41, 51, 11, 9, 'sujet', label=r'$r$', size='s')
names = [r'$H$', r'$rH$', r'$r^2H$', r'$r^3H$']
cx = []
for i in range(4):
    x0 = 2.25 + i * 21.5; cx.append(x0 + 9.5)
    box(ax, x0, 14, 19, 9, 'varie' if i in (0, 2) else 'fixe', label=names[i])
arrow(ax, (33.5, 50), (cx[0], 24), 'varie')
arrow(ax, (46.5, 50), (cx[2], 24), 'varie')
text(ax, 17, 40, r'$\times r$', 'varie', 's')
text(ax, 60, 40, r'$\times r$', 'varie', 's')
text(ax, cx[0], 10, r'$s$', 'encre', 'm')
text(ax, cx[2], 10, r'$r^2$', 'encre', 'm')
text(ax, 44, 3.5, 'deux classes différentes', 'limite', 's')
save(fig, '47-179')
