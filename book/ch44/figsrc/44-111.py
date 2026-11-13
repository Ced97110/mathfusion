import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 73, r'$U(\mathbb{Z})$ avec $\times$', 'sujet', 'm')
box(ax, 22, 50, 44, 16, 'sujet', dash=True)
disc(ax, 34, 58, 4.5, 'sujet', label='$1$', size='s')
disc(ax, 54, 58, 4.5, 'sujet', label='$-1$', size='s')
arrow(ax, (54, 63), (34, 63), 'varie', curve=0.4)
text(ax, 44, 46, r'$(-1)(-1) = 1$', 'varie', 's')
rows = ['le neutre $1$ est dans $U$', 'le produit reste dans $U$', 'l’inverse de $-1$ reste dans $U$']
for i, r in enumerate(rows):
    box(ax, 6, 28 - i * 11 + 0, 76, 9, 'resultat')
    text(ax, 44, 32.5 - i * 11, '✓ ' + r, 'resultat', 's')
text(ax, 44, 4, 'test du sous-groupe : un groupe', 'resultat', 's') if False else None
save(fig, '44-111')
