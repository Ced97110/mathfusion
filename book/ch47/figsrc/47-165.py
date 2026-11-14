import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'table de $S_3/A_3$ : produit des classes', 'encre', 'm')
hd = [('paire', 'sujet'), ('impaire', 'varie')]
x0, y0, cw, ch = 26, 48, 28, 13
text(ax, 12, y0 + 0, r'$\times$', 'fixe', 'l')
for j, (l, r) in enumerate(hd):
    box(ax, x0 + j * (cw + 2), y0 - 6.5, cw, ch, r, label=l, size='s')
    box(ax, 4 - 0 + 0, y0 - 6.5 - (j + 1) * (ch + 2), 20, ch, r, label=l, size='s')
res = [['paire', 'impaire'], ['impaire', 'paire']]
rol = {'paire': 'sujet', 'impaire': 'varie'}
for i in range(2):
    for j in range(2):
        v = res[i][j]
        box(ax, x0 + j * (cw + 2), y0 - 6.5 - (i + 1) * (ch + 2), cw, ch, 'resultat', label=v, size='s')
text(ax, 44, 3, r'signature : paire $+1$, impaire $-1$', 'fixe', 's')
save(fig, '47-165')
