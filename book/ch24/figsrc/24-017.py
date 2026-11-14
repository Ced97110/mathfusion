import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
# expression a x + b y
bx = [(6, 'a', 'sujet'), (17, 'x', 'fixe'), (36, 'b', 'autre'), (47, 'y', 'fixe')]
for x, s, r in bx:
    box(ax, x, 50, 9, 11, r, label=r'$%s$' % s, size='l')
text(ax, 29.5, 55.5, '+', 'encre', 'l')
text(ax, 22, 46.5, r'$a$ multiplie $x$', 'sujet', 's')
text(ax, 52, 46.5, r'$b$ multiplie $y$', 'autre', 's')
# headers
text(ax, 50, 36, 'cafés', 'sujet', 's')
text(ax, 76, 36, 'croissants', 'autre', 's')
for day, a, b, y in (('Lundi', 1, 1, 24), ('Mardi', 2, 1, 8)):
    text(ax, 2, y, day, 'encre', 'm', ha='left')
    text(ax, 26, y, r'$a = %d$' % a, 'sujet', 'm')
    for i in range(a): disc(ax, 40 + i * 8, y, 3, 'sujet')
    text(ax, 62, y, r'$b = %d$' % b, 'autre', 'm')
    for i in range(b): disc(ax, 74, y, 3, 'autre')
save(fig, '24-017')
