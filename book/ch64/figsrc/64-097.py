import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(50, r'$\mathbb{Z}/2$', 2, 'une racine carrée'), (32, r'$\mathbb{Z}/3$', 3, 'une racine cubique'), (12, r'$V$', 4, 'deux racines carrées')]
for y, nm, n, res in rows:
    h = 12 if n < 4 else 14
    box(ax, 3, y - h / 2, 28, h, 'sujet')
    text(ax, 10, y, nm, 'sujet', 'm')
    xs = [18 + k * 4.2 for k in range(n)] if n < 4 else [17 + k * 3.6 + (1.4 if k >= 2 else 0) for k in range(4)]
    for x in xs: disc(ax, x, y, 1.2, 'sujet')
    if n == 4:
        for a, b in ((0, 1), (2, 3)):
            box(ax, xs[a] - 2, y - 2.6, xs[b] - xs[a] + 4, 5.2, 'varie', fill=False, dash=True, lw=0.7, r=1.0)
        text(ax, 17, y - 5.2, r'$4=2\times2$', 'varie', 's', ha='left')
    arrow(ax, (31, y), (45, y), 'varie')
    box(ax, 45, y - 6, 40, 12, 'resultat', label=res, size='s')
save(fig, '64-097')
