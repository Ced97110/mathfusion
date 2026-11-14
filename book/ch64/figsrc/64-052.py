import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 22
f = numberline(ax, 5, 83, y, -27, 36, step=1, labels=False, arrow_right=False, tick=0.9)
for v in range(-27, 37, 9):
    disc(ax, f(v), y, 1.7, 'sujet')
    text(ax, f(v), y - 5, str(v).replace('-', '−'), 'sujet', 's')
arrow(ax, (f(0), y + 2), (f(9), y + 2), 'varie', curve=-0.6)
text(ax, f(4.5), y + 9, r'$9\times1$', 'varie', 's')
arrow(ax, (f(0), y + 2), (f(18), y + 2), 'varie', curve=-0.4)
text(ax, f(13), y + 10.5, r'$9\times2$', 'varie', 's')
arrow(ax, (f(0), y + 2), (f(-9), y + 2), 'varie', curve=0.6)
text(ax, f(-4.5), y + 9, r'$9\times(-1)$', 'varie', 's')
text(ax, 44, 48, r'$9\mathbb{Z}$ : multiples de 9', 'sujet', 'm', weight='bold')
text(ax, 44, 6, r'traits : tous les entiers de $\mathbb{Z}$', 'fixe', 's')
save(fig, '64-052')
