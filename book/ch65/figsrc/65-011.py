import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
panels = [(r'$\sigma$', {0: 1, 1: 2, 2: 0}, 'varie'),
          (r'$\sigma^2$', {0: 2, 1: 0, 2: 1}, 'varie'),
          (r'$\sigma^3=1$', {0: 0, 1: 1, 2: 2}, 'resultat')]
for p, (title, m, role) in enumerate(panels):
    cx = 19 + 26 * p
    text(ax, cx + 6, 50, title, role, 'l')
    for i in range(3):
        disc(ax, cx + 6 * i, 36, 2.5, 'sujet', label=f'$r_{i + 1}$', size='s')
        disc(ax, cx + 6 * i, 10, 2.5, 'fixe')
    for i, j in m.items():
        arrow(ax, (cx + 6 * i, 33.4), (cx + 6 * j, 12.6), role, lw=0.9)
text(ax, 2, 36, 'avant', 'sujet', 's', ha='left')
text(ax, 2, 10, 'après', 'fixe', 's', ha='left')
save(fig, '65-011')
