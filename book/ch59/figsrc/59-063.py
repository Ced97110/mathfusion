import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 16, 47, 'nouveau tableau', 'encre', 's')
cells = [[('4', 4, 28), ('6', 14, 28)], [('2', 4, 17), ('−2', 14, 17)]]
for row in cells:
    for v, x, y in row:
        box(ax, x, y, 10, 10, 'sujet', label=v)
line(ax, [(11.5, 30.5), (16.5, 24.5)], 'sujet', lw=1.6)
line(ax, [(16.5, 30.5), (11.5, 24.5)], 'varie', lw=1.6)
text(ax, 86, 36, r'$4\times(-2)=-8$', 'sujet', 'm', ha='right')
text(ax, 86, 27, r'$6\times2=12$', 'varie', 'm', ha='right')
text(ax, 86, 15, r'$-8-12=-20$', 'resultat', 'l', ha='right')
text(ax, 86, 7, 'déterminant', 'resultat', 's', ha='right')
save(fig, '59-063')
