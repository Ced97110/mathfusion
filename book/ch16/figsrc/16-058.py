import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
data = ((52, '3', '7'), (32, '5', '12'), (12, '8', '20'))
for y, a, b in data:
    box(ax, 2, y, 28, 9, 'fixe', label=r'$x+%s=%s$' % (a, b))
    text(ax, 16, y - 4, r'$a=%s$, $b=%s$' % (a, b), 'autre', 's')
    arrow(ax, (31, y + 4.5), (53, 31 + (y - 32) * 0.25), 'varie')
box(ax, 54, 24, 32, 14, 'sujet', label=r'$x+a=b$', size='l')
text(ax, 70, 18, r'$a$, $b$ : nombres connus', 'sujet', 's')
text(ax, 70, 44, 'une seule écriture', 'sujet', 's')
save(fig, '16-058')
