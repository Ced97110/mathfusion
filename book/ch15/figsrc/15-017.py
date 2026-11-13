import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$x = 1 \cdot x$', 'sujet', 'l')
box(ax, 34, 38, 20, 9, 'sujet', label=r'$x$')
text(ax, 32, 42.5, 'un cahier :', 'fixe', 's', ha='right')
text(ax, 56, 42.5, 'une fois $x$', 'sujet', 's', ha='left')
xs = [8, 25, 42]
for x in xs: box(ax, x, 14, 14, 9, 'sujet', label=r'$x$')
text(ax, 62, 18.5, '+', 'varie', 'l')
box(ax, 68, 14, 14, 9, 'varie', label=r'$x$')
text(ax, 25, 28, r'$3x$', 'sujet', 'm'); text(ax, 75, 28, r'$1 \cdot x$', 'varie', 'm')
brace(ax, 8, 82, 12, 'resultat', r'$3x + 1 \cdot x = 4x$')
save(fig, '15-017')
