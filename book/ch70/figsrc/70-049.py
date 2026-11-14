import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
line(ax, [(44, 20), (44, 62)], 'fixe', lw=0.6, dash=True)
text(ax, 22, 66, r'racines $\pm\sqrt{2}$ et $1$', 'sujet', 's')
box(ax, 2, 34, 40, 20, 'sujet', label='$(\\sqrt{2}-1)(-\\sqrt{2}-1)$\n$=-1$', size='s')
text(ax, 66, 66, 'tableau : sans racines', 'autre', 's')
rows = [['1', '0', '−2'], ['1', '−1', '0'], ['0', '1', '−1']]
cw, ch, x0, ytop = 12, 8, 48, 60
for i, row in enumerate(rows):
    for j, s in enumerate(row):
        box(ax, x0 + j * cw + 0.4, ytop - (i + 1) * ch + 0.4, cw - 0.8, ch - 0.8, 'autre', label=s, size='s', r=0.4)
text(ax, 66, ytop - 3 * ch - 4, r'déterminant $=-1$', 'autre', 's')
box(ax, 14, 6, 60, 10, 'resultat', label=r'même nombre : $-1$', size='m')
save(fig, '70-049')
