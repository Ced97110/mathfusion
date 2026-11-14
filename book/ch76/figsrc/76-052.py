import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'$(u+v)\wedge(u+v)=0$', 'sujet', 'm')
text(ax, 31, 68, r'$u$', 'encre', 's'); text(ax, 63, 68, r'$v$', 'encre', 's')
text(ax, 8, 55, r'$u$', 'encre', 's'); text(ax, 8, 37, r'$v$', 'encre', 's')
cells = [(0, 0, r'$u\wedge u=0$', 'fixe'), (1, 0, r'$u\wedge v=5$', 'varie'),
         (0, 1, r'$v\wedge u=-5$', 'varie'), (1, 1, r'$v\wedge v=0$', 'fixe')]
for c, r, lab, role in cells:
    box(ax, 15 + c * 32, 49 - r * 18, 30, 14, role, label=lab, size='s')
arrow(ax, (47, 30), (47, 21), 'varie')
text(ax, 47, 25.5, '', 'encre', 's') if False else None
text(ax, 47, 16, r'$5+(-5)=0$', 'varie', 'm')
box(ax, 14, 2, 66, 9, 'resultat', label=r'$v\wedge u=-\,u\wedge v$')
save(fig, '76-052')
