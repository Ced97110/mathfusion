import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 76, r'$(a + b)(a + b)(a + b)(a + b)$', 'fixe', 's')
cols = [27.8, 36.6, 45.4, 54.2]
for r, y in enumerate((62, 54, 46, 38)):
    bcol = 3 - r
    for c, x in enumerate(cols):
        box(ax, x, y, 6, 6, 'varie' if c == bcol else 'autre')
box(ax, 10, 24, 4, 4, 'autre', r=0.5); text(ax, 17, 26, r'$a$', 'encre', 's')
box(ax, 24, 24, 4, 4, 'varie', r=0.5); text(ax, 31, 26, r'$b$', 'encre', 's')
text(ax, 44, 12, r'$a \times a \times a \times b = a^{3}b$', 'encre', 's')
line(ax, [(60.5, 68), (62, 68), (62, 38), (60.5, 38)], 'varie', lw=0.9)
text(ax, 74, 63, '4 fois le même', 'varie', 's')
arrow(ax, (63, 53), (69.5, 53), 'varie')
text(ax, 72, 53, '4', 'sujet', 'l')
text(ax, 79, 53, r'$a^{3}b$', 'encre', 'l')
text(ax, 72, 45, 'coefficient', 'sujet', 's')
text(ax, 74, 38, 'placé devant', 'sujet', 's')
save(fig, '01-167')
