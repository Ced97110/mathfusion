import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 11, 14, r'$1+H$', 'varie', 'm'); text(ax, 11, 52, r'$2+H$', 'autre', 'm')
for i in range(4):
    x = 30 + i * 15
    four = (i == 1)
    box(ax, x - 6, 8, 12, 12, 'resultat' if four else 'varie', label=str(3 * i + 1), size='l', lw=1.6 if four else 0.8)
    box(ax, x - 6, 46, 12, 12, 'autre', label=str(3 * i + 2), size='l')
x = 45
arrow(ax, (x, 21), (x, 31), 'resultat')
line(ax, [(x - 3, 33), (x + 3, 39)], 'limite', lw=1.4); line(ax, [(x - 3, 39), (x + 3, 33)], 'limite', lw=1.4)
text(ax, 62, 38, '4 absent de', 'limite', 's', ha='left'); text(ax, 62, 33, r'$2+H$', 'limite', 's', ha='left')
save(fig, '47-013')
