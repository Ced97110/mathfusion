import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cols = [('point vert', 'resultat', 'cos x = 1', 'sec x = 1', '1 = 1'), ('point vert', 'resultat', 'cos x = −1', 'sec x = −1', '−1 = −1'),
        ('contre-exemple', 'limite', 'cos x = 0,5', 'sec x = 2', '0,5 ≠ 2')]
for i, (h, r, a, b, s) in enumerate(cols):
    x0 = 3 + i * 28.5; xc = x0 + 13
    text(ax, xc, 62, h, r, 's')
    box(ax, x0, 42, 26, 11, 'autre', label=a, size='s'); box(ax, x0, 10, 26, 11, 'sujet', label=b, size='s')
    arrow(ax, (xc - 9, 41), (xc - 9, 22), 'varie')
    text(ax, xc + 4, 31.5, s, r, 'm', weight='bold')
save(fig, '30-079')
