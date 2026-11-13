import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$60=2\times2\times3\times5$', 'encre', 'm')
top, bot = ['2','2','3','5'], ['5','3','2','2']
xs = [7 + i * 20 for i in range(4)]
ytop, ybot = 48, 22
for i in range(4):
    j = bot.index(top[i]) if top[i] != '2' else (3 if i == 0 else 2)
    line(ax, [(xs[i] + 7, ytop - 5), (xs[j] + 7, ybot + 5)], 'fixe', lw=0.8)
for i in range(4):
    box(ax, xs[i], ytop - 5, 14, 10, 'sujet', label=top[i])
    box(ax, xs[i], ybot - 5, 14, 10, 'varie', label=bot[i])
text(ax, 44, 58, 'un chemin de 1 à 60', 'sujet', 's')
text(ax, 44, 10, 'un autre chemin de 1 à 60', 'varie', 's')
save(fig, '79-184')
