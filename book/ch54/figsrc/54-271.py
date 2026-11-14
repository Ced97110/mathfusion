import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, 'Dans ℤ/2 (valeurs 0 et 1)', 'fixe', 's')
# columns: coefficients of 1, x, x^2 ; values at 0 and 1
cc = [30, 41, 52]
vc = [68, 79]
for x, l in zip(cc, [r'$1$', r'$x$', r'$x^2$']):
    text(ax, x, 62, l, 'fixe', 's')
for x, l in zip(vc, ['en 0', 'en 1']):
    text(ax, x, 62, l, 'fixe', 's')
rows = [(46, 'sujet', r'$x^2-x$', ['0', '-1', '1']), (28, 'autre', r'$0$', ['0', '0', '0'])]
for y, role, name, coefs in rows:
    text(ax, 9, y + 4, name, role, 'm')
    for x, c in zip(cc, coefs):
        box(ax, x - 4.5, y, 9, 8, role, label=c, size='s')
    for x in vc:
        box(ax, x - 4.5, y, 9, 8, 'resultat', label='0', size='s')
text(ax, 41, 17, r'suites $\neq$', 'limite', 'm', weight='bold')
text(ax, 73.5, 17, 'valeurs =', 'resultat', 'm', weight='bold')
text(ax, 41, 11, 'coefficients', 'fixe', 's')
text(ax, 73.5, 11, 'fonction', 'fixe', 's')
save(fig, '54-271')
