import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
rows = [('sujet', 'f', ['1', '0', r'$x^2-4$']),
        ('autre', 'g', ['1', r'$2-x^2$', '0']),
        ('autre', 'g', ['0', '1', r'$2-x^2$'])]
xs = [16, 41, 66]
for i, (role, name, cells) in enumerate(rows):
    y = 44 - 17 * i
    text(ax, 8, y + 7, name, role, 'l')
    for x, c in zip(xs, cells):
        box(ax, x, y, 21, 14, 'fixe' if c == '0' else role, label=c, size='s' if len(c) > 2 else 'm')
text(ax, 44, 4, '1 ligne $f$ + 2 lignes $g$', 'encre', 's')
save(fig, '70-102')
