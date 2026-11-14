import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'$x \cdot y$ : bit à bit, puis somme', 'encre', 'm', weight='bold')
cw, x0 = 9, 28
x, y = '1100', '1010'
p = ''.join(str(int(a) * int(b)) for a, b in zip(x, y))
rows = [(40, x, r'$x$', 'sujet'), (31, y, r'$y$', 'autre'), (20, p, 'produit', 'resultat')]
for yy, s, lab, role in rows:
    text(ax, 3, yy + 3, lab, role, 'm', ha='left')
    for i, c in enumerate(s):
        box(ax, x0 + i * cw, yy, cw - 0.8, 6.2, role if c == '1' else 'fixe', label=c, size='m', r=0.4)
text(ax, 44, 11, '1 + 0 + 0 + 0 = 1', 'resultat', 'l', weight='bold')
text(ax, 44, 3.5, r'$h \cdot c = 0$ : test d’un mot $c$ du code', 'fixe', 's')
save(fig, '68-215')
