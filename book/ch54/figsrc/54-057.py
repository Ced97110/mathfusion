import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, 'seul obstacle : un produit nul', 'varie', 's')
rows = [(52, r'$\mathbb{Z}$', 'sujet', r'$\mathbb{Q}$', 'resultat', 'resultat'),
        (34, r'$\mathbb{Z}[x]$', 'sujet', 'quotients de polynômes', 'resultat', 'resultat'),
        (16, r'$\mathbb{Z}/6$', 'fixe', 'aucun corps', 'limite', 'limite')]
for y, a, ra, b, rb, rar in rows:
    box(ax, 2, y, 22, 12, ra, label=a, size='m')
    arrow(ax, (24, y + 6), (42, y + 6), rar)
    box(ax, 42, y, 44, 12, rb, label=b, size='s', dash=(rb == 'limite'))
text(ax, 33, 8, r'$2\times3=0$ : refusé', 'limite', 's')
save(fig, '54-057')
