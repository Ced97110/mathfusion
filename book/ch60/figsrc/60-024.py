import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cw, ch, x0, yt = 12, 11, 10, 46
ctr = lambda i, j: (x0 + (j + 0.5) * cw, yt - (i + 0.5) * ch)
for i in range(2):
    for j in range(6):
        if j % 2 == i:
            role, lab, dash, fill = ('limite' if (i, j) == (0, 0) else 'sujet'), f'{j}, {j + 6}', False, True
        else:
            role, lab, dash, fill = 'fixe', None, False, True
        box(ax, x0 + j * cw + 0.3, yt - (i + 1) * ch + 0.3, cw - 0.6, ch - 0.6, role, fill=fill, dash=dash, label=lab, size='s', r=0.6)
for i in range(2): text(ax, x0 - 3.5, ctr(i, 0)[1], str(i), 'fixe', 's')
text(ax, x0 + 3 * cw, yt + 3, 'reste mod 6 (colonne)', 'fixe', 's')
text(ax, 2.5, yt - ch, 'reste mod 2 (ligne)', 'fixe', 's', rot=90)
text(ax, 44, 8, 'rouge : 0 et 6 dans la même case', 'limite', 's')
text(ax, 44, 2.5, 'gris : aucun nombre', 'fixe', 's')
save(fig, '60-024')
