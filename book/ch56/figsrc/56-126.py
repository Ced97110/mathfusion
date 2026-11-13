import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y = 44
parts = [(6, 'sujet', r'$\mathbb{Z}$', 'les entiers'), (32, 'varie', r'$[\ \ ]$', 'on ajoute un nombre'),
         (58, 'autre', r'$i$', r'$i^2=-1$')]
for x, role, sym, mean in parts:
    box(ax, x, y, 24, 14, role, label=sym, size='xl')
    arrow(ax, (x + 12, y), (x + 12, y - 8), role)
    text(ax, x + 12, y - 12, mean, role, 's')
box(ax, 8, 6, 72, 11, 'resultat', label=r'tous les $m+ni$, $m$ et $n$ entiers', size='m')
text(ax, 44, y + 20, r'$\mathbb{Z}[i]$ se lit « grand Z crochet i »', 'encre', 's')
save(fig, '56-126')
