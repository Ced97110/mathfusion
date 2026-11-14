import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def times(x, y):
    for sg in (1, -1): line(ax, [(x - 1.5, y - 1.5 * sg), (x + 1.5, y + 1.5 * sg)], 'fixe', lw=1.1)
def equals(x, y):
    for d in (-1, 1): line(ax, [(x - 1.8, y + d), (x + 1.8, y + d)], 'fixe', lw=1.1)
xs = [10, 28, 46, 64, 80]
box(ax, 2, 62, 24, 12, 'varie', label='orange', size='m'); times(31, 68)
box(ax, 36, 62, 22, 12, 'resultat', label='vert', size='m'); equals(63, 68)
box(ax, 68, 62, 18, 12, 'resultat', label='vert', size='m')
for i, (a, b) in enumerate([(1, 2), (5, 6), (-3, 10)]):
    y = 46 - 16 * i
    p = a * b
    disc(ax, 14, y, 4.6, 'varie', label=str(a).replace('-', '−'), size='m'); times(31, y)
    disc(ax, 47, y, 4.6, 'resultat', label=str(b), size='m'); equals(63, y)
    disc(ax, 77, y, 4.6, 'resultat', label=str(p).replace('-', '−'), size='m')
save(fig, '52-031')
