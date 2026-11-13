import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 11, 53, r'$Le_1$', 'sujet', 'm'); text(ax, 52, 53, r'$Le_2$', 'autre', 'm')
text(ax, 37, 46, r'$1\,e_1$', 'autre', 's'); text(ax, 67, 46, r'$3\,e_2$', 'autre', 's')
text(ax, 11, 38, r'$2\,e_1$', 'sujet', 's'); text(ax, 11, 25, r'$1\,e_2$', 'sujet', 's')
cells = [(22, 33, r'$e_1\wedge e_1=0$', 'limite'), (52, 33, r'$6\,e_{12}$', 'sujet'),
         (22, 20, r'$-1\,e_{12}$', 'varie'), (52, 20, r'$e_2\wedge e_2=0$', 'limite')]
for x, y, lab, role in cells: box(ax, x, y, 30, 12, role, label=lab, size='s')
arrow(ax, (52, 19), (52, 12.5), 'resultat', lw=1.0)
box(ax, 22, 2, 60, 9.5, 'resultat', label=r'$6-1=5$', size='m')
save(fig, '76-077')
