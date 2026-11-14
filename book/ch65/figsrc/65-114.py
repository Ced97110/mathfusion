import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cxs = (24, 48, 72)
for c, r in zip(cxs, (r'$y_1=-3$', r'$y_2=1$', r'$y_3=2$')):
    box(ax, c - 11, 62, 22, 9, 'fixe', label=r, size='s')
text(ax, 5, 46.5, r'$z_1$', 'sujet', 'm')
text(ax, 5, 26.5, r'$z_2$', 'autre', 'm')
r1 = (r'$\times 1$', r'$\times w$', r'$\times w^2$')
r2 = (r'$\times 1$', r'$\times w^2$', r'$\times w$')
for k, (c, a, b) in enumerate(zip(cxs, r1, r2)):
    box(ax, c - 11, 42, 22, 9, 'sujet' if k == 0 else 'varie', label=a, size='s')
    box(ax, c - 11, 22, 22, 9, 'autre' if k == 0 else 'varie', label=b, size='s')
arrow(ax, (cxs[1], 42), (cxs[2], 31.5), 'varie')
arrow(ax, (cxs[2], 42), (cxs[1], 31.5), 'varie')
text(ax, cxs[0], 36.5, r'$w\leftrightarrow w^2$', 'varie', 's')
box(ax, 3, 4, 40, 10, 'sujet', label=r'$z_1=-5-w$')
box(ax, 45, 4, 40, 10, 'autre', label=r'$z_2=-4+w$')
save(fig, '65-114')
