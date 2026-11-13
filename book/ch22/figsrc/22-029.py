import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 16
f = numberline(ax, 8, 76, y, -5, 5, 1, labels=False)
ax.add_patch(Rectangle((f(0), y + 0.5), f(5) - f(0), 7, fc=FILL['resultat'], ec='none', zorder=1))
text(ax, (f(0) + f(5)) / 2 + 2, y + 4, 'positives', 'resultat', 's')
disc(ax, f(4), y, 1.6, 'resultat'); disc(ax, f(-4), y, 1.6, 'fixe')
text(ax, f(0), y - 3.4, '0', 'fixe', 's'); text(ax, f(4), y - 3.4, '4', 'resultat', 's'); text(ax, f(-4), y - 3.4, '−4', 'fixe', 's')
box(ax, 44, 38, 30, 10, 'sujet', label=r'$\sqrt{16} = 4$', size='m')
arrow(ax, (f(4), 38), (f(4), y + 3), 'varie')
text(ax, 20, 36, r'pas $\sqrt{16}$', 'fixe', 's')
arrow(ax, (20, 33), (f(-4), y + 3), 'fixe')
save(fig, '22-029')
