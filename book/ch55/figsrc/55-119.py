import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# Z/3Z : x^3 and x. Left: polynomials (coefficient lists), right: functions (values).
text(ax, 21, 68, 'polynômes', 'sujet', 'l', weight='bold')
text(ax, 66, 68, 'fonctions', 'autre', 'l', weight='bold')
line(ax, [(44, 6), (44, 64)], 'fixe', dash=True)
YT, YB = 40, 24
text(ax, 3, YT + 4, r'$x^3$', 'sujet', 'm', ha='left')
text(ax, 3, YB + 4, r'$x$', 'sujet', 'm', ha='left')
cw, st = 6, 7
def strip(y, coefs):
    for i, c in enumerate(coefs):
        box(ax, 12 + i * st, y, cw, 8, 'sujet' if c else 'fixe', label=str(c), size='m')
strip(YT, [0, 0, 0, 1])
strip(YB, [0, 1, 0, 0])
for i, d in enumerate(('1', r'$x$', r'$x^2$', r'$x^3$')):
    text(ax, 12 + i * st + cw / 2, YT + 11.5, d, 'fixe', 's')
box(ax, 8, 4, 30, 9, 'limite', label='listes ≠ : non', size='m')
# right: values at x = 0, 1, 2
text(ax, 50, YT + 11.5, r'$x=$', 'fixe', 's')
for j, v in enumerate((0, 1, 2)):
    text(ax, 58 + j * 9 + 4, YT + 11.5, str(v), 'fixe', 's')
    box(ax, 58 + j * 9, YT, 8, 8, 'autre', label=str((v ** 3) % 3), size='m')
    box(ax, 58 + j * 9, YB, 8, 8, 'autre', label=str(v), size='m')
text(ax, 50, YT + 4, r'$x^3$', 'autre', 'm')
text(ax, 50, YB + 4, r'$x$', 'autre', 'm')
box(ax, 50, 4, 34, 9, 'resultat', label='valeurs = : oui', size='m')
save(fig, '55-119')
