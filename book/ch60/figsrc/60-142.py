import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
cw, ch, ytop = 14, 9, 66
def grid(x0, gset, kx):
    for i in range(4):
        for j in range(2):
            if (i, j) in gset: role = 'sujet'; fill = True
            elif (i, j) == (0, 1): role = 'varie'; fill = True
            else: role = 'fixe'; fill = False
            box(ax, x0 + j * cw, ytop - (i + 1) * ch, cw, ch, role, fill=fill, label=f'({i}, {j})', size='s', r=0.5)
    box(ax, x0 - 0.8, ytop - ch - 0.8, 2 * cw + 1.6, ch + 1.6, 'varie', fill=False, lw=1.6, r=0.5)
    text(ax, kx, ytop - ch / 2, 'K', 'varie', 'm', weight='bold')
grid(8, {(0, 0), (1, 0), (2, 0), (3, 0)}, 4)
grid(52, {(0, 0), (1, 1), (2, 0), (3, 1)}, 48)
line(ax, [(44, 30), (44, 80)], 'fixe', dash=True)
text(ax, 22, 76, 'g = (1, 0)', 'sujet', 'm', weight='bold')
text(ax, 66, 76, 'g = (1, 1)', 'sujet', 'm', weight='bold')
text(ax, 44, 22, r'même $K = \langle (0, 1)\rangle$ (cadre orange)', 'varie', 's')
text(ax, 44, 15, 'deux écritures de G :', 'encre', 's')
text(ax, 44, 9, 'morceaux de 4 et de 2 éléments', 'resultat', 's')
text(ax, 44, 3.5, 'mais pas les mêmes morceaux', 'encre', 's', weight='bold')
save(fig, '60-142')
