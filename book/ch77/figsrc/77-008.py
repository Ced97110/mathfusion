import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'même geste : $x\mapsto$ élément $\times\,x$', 'varie', 's')
rows = [(34, 'autre', 'groupe', r'$g$', r'$x\mapsto gx$', 'permutation', 'une ligne du tableau'),
        (12, 'sujet', 'algèbre', r'$a$', r'$x\mapsto ax$', 'matrice', 'un tableau de nombres')]
for y, role, nom, el, geste, res, sous in rows:
    box(ax, 2, y, 22, 10, role, label=f'{el} ({nom})', size='s')
    arrow(ax, (24, y + 5), (36, y + 5), 'varie'); text(ax, 30, y + 9, geste, 'varie', 's')
    box(ax, 38, y, 24, 10, role, label=res, size='s')
    text(ax, 50, y - 3, sous, role, 's')
save(fig, '77-008')
