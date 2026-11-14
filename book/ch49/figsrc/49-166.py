import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 44, 86, 'un trait orange = une classe', 'varie', 's')
top = ['$e$', '$r$', '$r^2$', '$r^3$']; bot = ['$s$', '$rs$', '$r^2s$', '$r^3s$']
for i in range(4):
    x = 14 + i * 20
    line(ax, [(x, 57.5), (x, 34.5)], 'varie', lw=2.4)
    disc(ax, x, 62, 4.6, 'sujet', label=top[i], size='s'); disc(ax, x, 30, 4.6, 'sujet', label=bot[i], size='s')
    arrow(ax, (x, 24), (x, 15), 'varie'); disc(ax, x, 10, 4.4, 'resultat', label='ABCD'[i], size='s')
save(fig, '49-166')
