import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def dots(x0, y0, cols, rows, sp, role):
    n = 0
    for i in range(rows):
        for j in range(cols):
            disc(ax, x0 + j * sp, y0 - i * sp, 1.6, role); n += 1
    return n
box(ax, 4, 22, 38, 28, 'sujet', fill=False)
assert dots(9.5, 45, 6, 4, 5.4, 'sujet') == 24
box(ax, 52, 22, 32, 28, 'autre', fill=False)
assert dots(58, 45, 4, 3, 7.0, 'autre') == 12
text(ax, 23, 55, r'$G$', 'sujet', 'l', weight='bold')
text(ax, 68, 55, r'$H$', 'autre', 'l', weight='bold')
text(ax, 23, 16, r'$|G|=24$', 'sujet', 'm')
text(ax, 68, 16, r'$|H|=12$', 'autre', 'm')
text(ax, 44, 7, r'$|G|/|H|=24/12=2$', 'resultat', 'm', weight='bold')
text(ax, 44, 62, 'ordre = nombre d’éléments', 'encre', 's')
save(fig, '64-051')
