import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 6, 70, 46, 0, 10, step=1, every=2)
for v in range(0, 11, 2): disc(ax, f(v), 46, 2.2, 'resultat')
text(ax, 80, 46, 'sans fin', 'limite', 's')
for y, n, ok in [(26, '7', False), (9, '10', True)]:
    r = 'resultat' if ok else 'limite'
    box(ax, 4, y - 4.5, 12, 9, 'fixe', label=n, size='s'); arrow(ax, (17, y), (27, y), 'fixe')
    box(ax, 28, y - 4.5, 26, 9, 'sujet', label='est pair ?', size='s'); arrow(ax, (55, y), (65, y), r)
    box(ax, 66, y - 4.5, 16, 9, r, label='oui' if ok else 'non', size='s')
save(fig, '42-031')
