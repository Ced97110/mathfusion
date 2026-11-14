import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy = 12, 12
X = lambda x: ox + 30 * x
Yv = lambda y: oy + 4.2 * y
arrow(ax, (ox - 2, oy), (X(2.2), oy), 'fixe', lw=0.6)
line(ax, [(ox, oy - 2), (ox, 68)], 'varie', lw=1.3, dash=True)
text(ax, ox, 6, r'$x=0$', 'varie', 's')
xs = [0.1 + i * 0.01 for i in range(191)]
line(ax, [(X(x), Yv(1 / x)) for x in xs], 'sujet', lw=1.4)
for (x, lab, dx, dy) in [(1, r'$(1\ ;\ 1)$', 2, 3.5), (0.1, r'$(0{,}1\ ;\ 10)$', 3, 0)]:
    disc(ax, X(x), Yv(1 / x), 1.2, 'sujet')
    text(ax, X(x) + dx, Yv(1 / x) + dy, lab, 'sujet', 's', ha='left')
arrow(ax, (ox + 1.2, 58), (ox + 1.2, 67), 'varie', lw=1.0)
text(ax, ox + 5, 65, r'$(0{,}01\ ;\ 100)$', 'sujet', 's', ha='left')
text(ax, X(1.4), Yv(3.6), r'$y=1/x$', 'sujet', 's')
text(ax, 62, 40, 'la courbe\nne touche jamais\n$x=0$', 'varie', 's')
save(fig, '70-125')
