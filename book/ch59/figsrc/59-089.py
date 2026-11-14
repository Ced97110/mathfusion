import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def mat(vs, rs, x, y, c=10.0, g=1.0, size='m'):
    n = len(vs)
    for r, row in enumerate(vs):
        for k, v in enumerate(row):
            box(ax, x + k * (c + g), y + (n - 1 - r) * (c + g), c, c, rs[r][k], label=v, size=size)
mat([['6', '0'], ['0', '4']], [['sujet', 'fixe'], ['fixe', 'sujet']], 3, 36)
box(ax, 30, 50, 24, 11, 'autre', label=r'$\Delta_1=2$', size='s')
box(ax, 30, 33, 24, 11, 'autre', label=r'$\Delta_2=24$', size='s')
arrow(ax, (25, 48), (29.5, 54), 'autre')
arrow(ax, (25, 43), (29.5, 40), 'autre')
box(ax, 58, 50, 28, 11, 'resultat', label=r'$d_1=\Delta_1=2$', size='s')
box(ax, 58, 28, 28, 16, 'resultat', label='$d_2=\\Delta_2/\\Delta_1$\n$=24/2=12$', size='s')
arrow(ax, (54.5, 55.5), (57.5, 55.5), 'resultat')
arrow(ax, (54.5, 38.5), (57.5, 38.5), 'resultat')
arrow(ax, (54, 51), (58, 43), 'resultat')
text(ax, 72, 21, r'et non $6$ et $4$', 'limite', 's')
text(ax, 14.5, 62, r'diag$(6,\,4)$', 'sujet', 's')
save(fig, '59-089')
