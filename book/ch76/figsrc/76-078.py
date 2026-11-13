import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cells = [(28, 40, '2'), (44, 40, '1'), (28, 27, '1'), (44, 27, '3')]
for x, y, lab in cells: box(ax, x, y, 16, 13, 'sujet')
arrow(ax, (33, 48), (47, 31), 'resultat', lw=1.2)
arrow(ax, (55, 48), (41, 31), 'varie', lw=1.2)
for (x, y, lab), nm in zip(cells, 'abcd'):
    t = text(ax, x + 8, y + 6.5, rf'${nm}={lab}$', 'sujet', 's')
    t.set_bbox(dict(fc=FILL['sujet'], ec='none', pad=0.6))
text(ax, 22, 18, r'$ad=2\times3=6$', 'resultat', 's'); text(ax, 66, 18, r'$bc=1\times1=1$', 'varie', 's')
box(ax, 18, 3, 52, 9.5, 'resultat', label=r'$\det A=6-1=5$', size='m')
save(fig, '76-078')
