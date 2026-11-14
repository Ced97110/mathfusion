import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, 'ℤ est libre : base (1)', 'sujet', 's', weight='bold')
vals = list(range(-3, 5))
xs = [8 + i * 10.3 for i in range(len(vals))]
cl = {0: (30, 'sujet'), 1: (58, 'varie')}
for v, x in zip(vals, xs):
    r = 'sujet' if v % 2 == 0 else 'varie'
    disc(ax, x, 50, 3.6, r, label=f'{v}'.replace('-', '−'), size='s')
    cx, _ = cl[v % 2]
    arrow(ax, (x, 46.2), (cx + (x - cx) * 0.12, 30.5), r, lw=0.5)
disc(ax, 30, 26, 5, 'sujet', label='pairs', size='s')
disc(ax, 58, 26, 5, 'varie', label='impairs', size='s')
text(ax, 44, 14, 'ℤ/2ℤ = les 2 classes', 'encre', 's')
box(ax, 14, 2, 60, 8, 'limite', label='quotient : aucune base', size='s')
save(fig, '58-321')
