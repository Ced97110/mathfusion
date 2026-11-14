import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
maps = [(1, 2), (2, 1), (1, 1), (2, 2)]
labs = ['rien', 'échange', 'tout sur 1', 'tout sur 2']
for i, (m, l) in enumerate(zip(maps, labs)):
    cx = 11 + i * 22
    box(ax, cx - 10, 24, 20, 32, 'sujet', fill=False)
    ys = {1: 46, 2: 32}
    for n in (1, 2):
        disc(ax, cx - 6, ys[n], 2.4, 'fixe', label=str(n), size='s'); disc(ax, cx + 6, ys[n], 2.4, 'fixe', label=str(n), size='s')
        arrow(ax, (cx - 3.4, ys[n]), (cx + 3.4, ys[m[n - 1]]), 'varie', lw=0.8)
    text(ax, cx, 19, l, 'sujet', 's')
text(ax, 44, 8, r'$|M(\{1,2\})|=4=2\times2$', 'resultat', 'm')
save(fig, '44-090')
