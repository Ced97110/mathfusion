import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'somme $x_i + y_i$ d’une position $i$', 'encre', 'm', weight='bold')
text(ax, 55, 47, r'$y_i = 0$', 'autre', 'm', weight='bold')
text(ax, 77, 47, r'$y_i = 1$', 'autre', 'm', weight='bold')
for r, a in enumerate((0, 1)):
    ya = 31 - r * 13
    text(ax, 24, ya + 5, r'$x_i = %d$' % a, 'sujet', 'm', weight='bold')
    for c, b in enumerate((0, 1)):
        same = a == b
        box(ax, 44 + c * 22, ya, 21, 10, 'fixe' if same else 'varie', label='%d + %d = %d' % (a, b, (a + b) % 2),
            size='m', weight='normal' if same else 'bold')
        assert ((a + b) % 2 == 1) == (a != b)
box(ax, 4, 5, 7, 6, 'fixe')
text(ax, 13, 8, 'bits égaux : somme 0', 'fixe', 's', ha='left')
box(ax, 46, 5, 7, 6, 'varie')
text(ax, 55, 8, 'bits différents : 1', 'varie', 's', ha='left')
save(fig, '68-051')
