import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cols = [r'$x^2$', r'$7x$', r'$2$']; rws = [r'$x^2$', r'$4$']
prod = [[r'$x^4$', r'$7x^3$', r'$2x^2$'], [r'$4x^2$', r'$28x$', r'$8$']]
x0, w, h = 26, 20, 14
text(ax, x0 + 1.5 * w, 64, r'second facteur', 'autre', 's')
text(ax, 2, 40, 'premier\nfacteur', 'sujet', 's', ha='left')
for j, c in enumerate(cols): text(ax, x0 + w * (j + .5), 58, c, 'autre', 's')
for i, r in enumerate(rws):
    y = 38 - i * h
    text(ax, x0 - 5, y + h / 2, r, 'sujet', 's')
    for j in range(3):
        sem = (i == 0 and j == 2) or (i == 1 and j == 0)
        box(ax, x0 + w * j, y, w, h, 'varie' if sem else 'fixe', label=prod[i][j], size='m')
text(ax, 44, 20, r'$2x^2+4x^2=6x^2$ : semblables', 'varie', 's')
text(ax, 44, 9, r'$x^4+7x^3+6x^2+28x+8$', 'resultat', 'm', weight='bold')
save(fig, '15-119')
