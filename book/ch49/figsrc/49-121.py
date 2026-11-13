import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r'4 classes de $H=\{1, s\}$', 'sujet', 's')
names = [r'$H$', r'$rH$', r'$r^2H$', r'$r^3H$']
xs = [3 + i * 22 for i in range(4)]
for x, n in zip(xs, names):
    box(ax, x, 22, 17, 22, 'sujet')
    disc(ax, x + 5, 37, 2.2, 'sujet'); disc(ax, x + 12, 37, 2.2, 'sujet')
    text(ax, x + 8.5, 28, n, 'sujet', 's')
for i in range(3):
    arrow(ax, (xs[i] + 17.5, 33), (xs[i + 1] - 0.5, 33), 'varie')
arrow(ax, (xs[3] + 8.5, 21), (xs[0] + 8.5, 21), 'varie', curve=-0.35)
text(ax, 44, 7, r'$r\times$ envoie chaque classe', 'varie', 's')
text(ax, 44, 1.5, 'sur la suivante', 'varie', 's') if False else None
save(fig, '49-121')
