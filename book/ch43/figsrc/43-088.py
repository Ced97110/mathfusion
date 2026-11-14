import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cols = [(0, [3, 6]), (1, [1, 4]), (2, [2, 5]), (5, [])]; xs = [14, 36, 58, 78]
text(ax, 44, 67, r'fibres de $f$ au-dessus de chaque $c$', 'sujet', 'm', weight='bold')
line(ax, [(3, 14), (85, 14)], 'fixe', lw=0.9)
for (c, els), x in zip(cols, xs):
    if els:
        box(ax, x - 8, 22, 16, 34, 'sujet')
        for k, n in enumerate(els): disc(ax, x, 48 - k * 14, 3.4, 'sujet', label=str(n))
        arrow(ax, (x, 21), (x, 15.5), 'fixe', lw=0.7)
    else:
        box(ax, x - 8, 22, 16, 34, 'limite', fill=False, dash=True)
        text(ax, x, 39, 'vide', 'limite', 's')
    disc(ax, x, 10, 3.2, 'limite' if not els else 'fixe', label=str(c))
text(ax, 44, 1.8, r'$c$ dans $T$', 'fixe', 's')
save(fig, '43-088')
