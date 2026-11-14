import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [4, 32, 60]
cols = [(r'$p=2$', [('2', 1), ('1 + 1', 0)]),
        (r'$p=3$', [('3', 0), ('2 + 1', 1), ('1 + 1 + 1', 0)]),
        (r'$p=5$', [('1', 1)])]
for x, (h, items) in zip(xs, cols):
    text(ax, x + 12, 62, h, 'sujet', 'm', weight='bold')
    for k, (t, chosen) in enumerate(items):
        box(ax, x, 47 - 10 * k, 24, 8, 'varie' if chosen else 'fixe', label=t)
pieces = [r'$\mathbb{Z}/4$', r'$\mathbb{Z}/9\oplus\mathbb{Z}/3$', r'$\mathbb{Z}/5$']
for x, p in zip(xs, pieces):
    text(ax, x + 12, 14, p, 'varie', 'm', weight='bold')
for x in (30, 58):
    text(ax, x, 14, r'$\oplus$', 'encre', 'l')
save(fig, '60-231')
