import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 34, 84, 27, 'fixe', fill=False, lw=0.8)
text(ax, 44, 56.5, 'dans R : x²y² s’écrit', 'fixe', 's')
bw, bh = 7.0, 9.0
groups = [(6, 15, 'autre', [r'$x^2$'], [r'$x$', r'$x$']),
          (23, 15, 'autre', [r'$y^2$'], [r'$y$', r'$y$']),
          (48, 15, 'sujet', [r'$xy$'], [r'$x$', r'$y$']),
          (65, 15, 'sujet', [r'$xy$'], [r'$x$', r'$y$'])]
for x0, w, role, top, bricks in groups:
    box(ax, x0, 37, w, 11, role, label=top[0], size='m')
    for i, b in enumerate(bricks):
        box(ax, x0 + i * (bw + 1), 12, bw, bh, 'fixe', label=b, size='s', dash=True)
    arrow(ax, (x0 + w / 2, 36.5), (x0 + w / 2, 22), 'fixe')
brace(ax, 6, 80, 11, 'fixe', label='hors de R : degré total 1', down=True)
save(fig, '56-066')
