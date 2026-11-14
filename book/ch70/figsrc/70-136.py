import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
cols = [(3, r'$x=1{,}5$', [r'$x-2=-0{,}5$', r'$x-1=0{,}5$', r'$x-3=-1{,}5$'], r'produit $p=0{,}375$', 'resultat',
         'deux hauteurs', r'$y^2=0{,}375$'),
        (45, r'$x=0{,}5$', [r'$x-2=-1{,}5$', r'$x-1=-0{,}5$', r'$x-3=-2{,}5$'], r'produit $p=-1{,}875$', 'fixe',
         'aucune hauteur', r'$y^2=-1{,}875$')]
for (x0, title, facs, prod, prole, res, eq) in cols:
    text(ax, x0 + 20, 90, title, 'encre', 'm')
    for j, fl in enumerate(facs):
        box(ax, x0, 70 - 12 * j, 40, 9, 'sujet', label=fl, size='s')
    arrow(ax, (x0 + 20, 46), (x0 + 20, 31.5), 'varie', lw=1.0)
    box(ax, x0, 21, 40, 9, prole, label=prod, size='s')
    arrow(ax, (x0 + 20, 21), (x0 + 20, 17), 'varie', lw=1.0)
    text(ax, x0 + 20, 12, eq, prole if prole == 'resultat' else 'fixe', 's')
    text(ax, x0 + 20, 6, res, prole if prole == 'resultat' else 'fixe', 's')
for s in (-1, 1):
    disc(ax, 8, 9 + s * 3, 1.2, 'resultat')
save(fig, '70-136')
