import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 17, 66, 16, 9, 'sujet', label=r'$E$')
box(ax, 17, 8, 16, 9, 'sujet', label=r'$\mathbb{Q}$')
mids = [(2, r'$\mathbb{Q}(r)$', False), (18, r'$\mathbb{Q}(j)$', False), (34, '?', True)]
for x, lab, dash in mids:
    box(ax, x, 38, 14, 9, 'varie' if not dash else 'fixe', label=lab, dash=dash)
    line(ax, [(25, 17), (x + 7, 38)], 'fixe')
    line(ax, [(x + 7, 47), (25, 66)], 'fixe')
qs = [(58, 'combien\nde corps ?'), (34, 'comment les\ntrouver ?'), (10, 'lesquels sont des corps\nde décomposition ?')]
for y, lab in qs:
    box(ax, 52, y, 34, 16, 'autre', label=lab, size='s')
save(fig, '63-006')
