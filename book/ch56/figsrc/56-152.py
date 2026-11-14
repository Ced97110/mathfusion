import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 55, 61, 'contenu', 'sujet', 'm', weight='bold')
text(ax, 77, 61, 'partie primitive', 'fixe', 's')
rows = [(46, r'$f=2x+4$', '2', r'$x+2$', 'sujet'),
        (30, r'$g=3x+6$', '3', r'$x+2$', 'sujet'),
        (10, r'$fg=6x^2+24x+24$', r'$2\times3=6$', r'$(x+2)^2$', 'resultat')]
for y, lab, cont, prim, role in rows:
    h = 12
    text(ax, 2, y + h / 2 + (3 if y == 10 else 0), lab if y != 10 else r'$fg$', 'encre', 'm', ha='left')
    box(ax, 36, y, 24, h, role, label=cont, size='m')
    text(ax, 64, y + h / 2, r'$\times$', 'fixe', 'm')
    box(ax, 68, y, 18, h, 'fixe', label=prim, size='s')
text(ax, 2, 10 + 2, r'$6x^2+24x+24$', 'encre', 's', ha='left')
assert [6, 24, 24] == [2 * 3 * 1, 2 * 3 * 4, 2 * 3 * 4]
save(fig, '56-152')
