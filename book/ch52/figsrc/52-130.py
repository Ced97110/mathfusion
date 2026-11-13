import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'idéaux $(k)$ de $\mathbb{Z}$', 'encre', 'm')
cfg = {0: 'sujet', 1: 'fixe', 2: 'resultat', 3: 'resultat', 4: 'limite', 5: 'resultat', 6: 'limite'}
for k, r in cfg.items():
    x = 5 + k * 11.5
    box(ax, x, 40, 10, 12, r, label=f'({k})', size='m')
rows = [('sujet', 'premier, pas maximal : (0)'), ('resultat', 'premier et maximal : (p), p premier'),
        ('limite', 'ni premier ni maximal : (4), (6)'), ('fixe', 'tout l’anneau : (1), exclu')]
for i, (r, s) in enumerate(rows):
    y = 28 - i * 7
    box(ax, 6, y - 2, 4, 4, r)
    text(ax, 13, y, s, r, 's', ha='left')
save(fig, '52-130')
