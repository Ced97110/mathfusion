import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = lambda a: 8 + a * 62 / 90.0
Y = lambda v: 12 + 7 * v
line(ax, [(8, 12), (84, 12)], 'fixe')
for a in (0, 45, 90):
    line(ax, [(X(a), 11), (X(a), 13)], 'fixe'); text(ax, X(a), 8, f'{a}°', 'fixe', 's')
line(ax, [(X(90), 12), (X(90), 77)], 'sujet', lw=1.2, dash=True)
text(ax, X(90) + 2, 40, 'droite\nà 90°', 'sujet', 's', ha='left')
pts = [(X(a), Y(math.tan(math.radians(a)))) for a in [i * 83.5 / 60 for i in range(61)]]
line(ax, pts, 'varie', lw=1.3)
disc(ax, X(80), Y(math.tan(math.radians(80))), 1.4, 'varie'); text(ax, X(80) - 2, Y(5.67) - 4, '80° : 5,67', 'varie', 's', ha='right')
arrow(ax, (X(83.5) + 0.3, Y(8.9) - 1), (X(83.5) + 2, 74), 'varie')
text(ax, X(88) - 20, 70, '89° : 57,29', 'varie', 's'); text(ax, X(88) - 20, 64, '89,9° : 572,96', 'varie', 's')
text(ax, 22, 36, 'la courbe monte', 'varie', 's')
save(fig, '30-051')
