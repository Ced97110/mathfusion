import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 16
f = numberline(ax, 8, 76, y, -5, 5, 1, labels=False)
ax.add_patch(Rectangle((f(-5), y + 0.5), f(0) - f(-5), 7, fc=FILL['varie'], ec='none', zorder=1))
text(ax, (f(-5) + f(0)) / 2 - 2, y + 4, 'négatives', 'varie', 's')
disc(ax, f(4), y, 1.6, 'sujet'); disc(ax, f(-4), y, 1.6, 'varie')
text(ax, f(0), y - 3.4, '0', 'fixe', 's')
text(ax, f(4), y - 6, r'$\sqrt{16} = 4$', 'sujet', 's')
text(ax, f(-4), y - 6, r'$-\sqrt{16} = -4$', 'varie', 's')
arrow(ax, (f(4), y + 3), (f(-4), y + 3), 'varie', curve=0.45)
text(ax, f(0), y + 21, 'signe − : opposé', 'varie', 's')
save(fig, '22-030')
