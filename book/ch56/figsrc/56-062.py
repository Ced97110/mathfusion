import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
names = {(0, 0): '$1$', (1, 0): '$x$', (0, 1): '$y$', (2, 0): '$x^2$', (1, 1): '$xy$', (0, 2): '$y^2$',
         (3, 0): '$x^3$', (2, 1): '$x^2y$', (1, 2): '$xy^2$', (0, 3): '$y^3$'}
step = 14.0; ox, oy = 11.0, 14.0
for (m, n), lab in names.items():
    even = (m + n) % 2 == 0
    disc(ax, ox + m * step, oy + n * step, 5.2, 'sujet' if even else 'fixe', fill=even, label=lab, size='s')
text(ax, ox + 1.5 * step, 3.5, "exposant de $x$", 'fixe', 's')
text(ax, 3, oy + 1.5 * step, "exposant de $y$", 'fixe', 's', rot=90)
disc(ax, 40, 58, 2.2, 'sujet')
text(ax, 44, 58, 'degré pair : dans $R$', 'sujet', 's', ha='left')
disc(ax, 40, 50, 2.2, 'fixe', fill=False)
text(ax, 44, 50, 'impair : hors de $R$', 'fixe', 's', ha='left')
save(fig, '56-062')
