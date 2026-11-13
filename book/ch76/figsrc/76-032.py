import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, r'$n = 2$ : $2^2 = 4$ produits', 'sujet', 'm', weight='bold')
cw, ch, gx, gy = 13, 11, 14, 28
heads = ['1', r'$i$']
for c in range(2):
    text(ax, gx + c * cw + cw / 2, gy + 2 * ch + 4, heads[c], 'sujet', 'm'); text(ax, gx - 4, gy + (1 - c) * ch + ch / 2, heads[c], 'sujet', 'm')
vals = [['1', r'$i$'], [r'$i$', '?']]
for r in range(2):
    for c in range(2):
        miss = (r, c) == (1, 1)
        box(ax, gx + c * cw, gy + (1 - r) * ch, cw, ch, 'limite' if miss else 'fixe', label=vals[r][c], dash=miss)
text(ax, gx + cw, gy - 4, r'$i \times i$ inconnu', 'limite', 's')
text(ax, 62, 55, r'$(2+3i)(1+4i)$', 'encre', 's')
box(ax, 46, 36, 40, 13, 'autre', label=r'$i\times i=-1$ : $-10+11i$', size='s')
box(ax, 46, 17, 40, 13, 'varie', label=r'$i\times i=1$ : $14+11i$', size='s')
text(ax, 66, 10, 'deux résultats', 'limite', 's')
save(fig, '76-032')
