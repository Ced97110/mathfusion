import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0, x1, y = 6, 82, 22
f = numberline(ax, x0, x1, y, 0, 54, step=1, labels=False, role='fixe', arrow_right=False, tick=0.8)
text(ax, f(0), y - 4.5, '0', 'fixe', 's')
text(ax, f(54), y - 4.5, '54', 'fixe', 's')
disc(ax, f(8), y, 1.8, 'fixe')
disc(ax, f(17), y, 1.8, 'sujet')
text(ax, f(8), y + 5, r'$m$ = 8', 'fixe', 'm')
text(ax, f(17) + 7, y + 5, r'$c$ = 17', 'sujet', 'm')
arrow(ax, (f(8) + 1, y + 8), (f(17) - 1, y + 8), 'varie', curve=-0.4)
text(ax, (f(8) + f(17)) / 2, y + 18, 'chiffrer', 'varie', 's')
text(ax, 44, 8, r'$c \equiv m^{e}\ (\mathrm{mod}\ n)$', 'encre', 'm')
save(fig, '53-104')
