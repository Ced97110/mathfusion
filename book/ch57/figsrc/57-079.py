import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 17, 70, 'objet', 'fixe', 's')
text(ax, 44, 70, r'$x\mapsto 3x$', 'varie', 'm')
text(ax, 71, 70, 'image', 'fixe', 's')
rows = [(52, 'x = (2 ; 1)', '(6 ; 3)'), (36, 'y = (1 ; 4)', '(3 ; 12)'), (16, 'x + y = (3 ; 5)', '(9 ; 15)')]
for y, l, r in rows:
    box(ax, 2, y, 30, 9, 'sujet', label=l, size='s')
    arrow(ax, (34, y + 4.5), (54, y + 4.5), 'varie')
    box(ax, 56, y, 30, 9, 'resultat', label=r, size='s')
for xc in (17, 71):
    text(ax, xc, 48, '+', 'fixe', 'l')
    text(ax, xc, 30.5, '=', 'fixe', 'l')
text(ax, 44, 6, 'la règle respecte la somme', 'resultat', 'm')
save(fig, '57-079')
