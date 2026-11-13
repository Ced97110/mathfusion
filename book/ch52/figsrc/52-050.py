import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 6, 76, 14, 0, 24, step=2, arrow_right=False, every=3)
for v in (0, 6, 12, 18, 24):
    disc(ax, f(v), 14, 1.4, 'fixe')
for a in (0, 6, 12):
    arrow(ax, (f(a), 17), (f(a + 6), 17), 'varie', curve=-0.5)
text(ax, f(9), 34, r'$q = 3$ pas de $k = 6$', 'varie', 's')
arrow(ax, (f(18), 17), (f(20), 17), 'limite', curve=-0.5)
disc(ax, f(20), 14, 1.4, 'limite')
text(ax, f(20), 26, r'$r = 2$', 'limite', 's')
text(ax, 44, 50, r'$n = 20 = 3 \times 6 + 2$', 'sujet', 'l')
text(ax, 44, 43, r'$r = 2 < 6$ : impossible', 'limite', 's')
save(fig, '52-050')
