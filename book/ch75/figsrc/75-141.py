import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'le produit $uv$ reste le même', 'fixe', 's')
cells = [[r'$(u,\,v)$', r'$(2u,\,2v)$'], [r'$(v,\,u)$', r'$(2v,\,2u)$']]
text(ax, 41, 53, r'$a=1$', 'varie', 's'); text(ax, 67, 53, r'$a=2$', 'varie', 's')
for r, (nom, role) in enumerate([('sans échange', 'sujet'), ('avec échange', 'autre')]):
    y = 33 - 15 * r
    text(ax, 15, y + 6, nom, role, 's')
    for k in range(2):
        box(ax, 29 + 26 * k, y, 24, 12, role, label=cells[r][k], size='s')
text(ax, 44, 8, r'$2(q-1)=2\times2=4$', 'resultat', 'l', weight='bold')
save(fig, '75-141')
