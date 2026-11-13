import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 2, 81, r'Départ : trois fois $a/b$', 'sujet', 'm', ha='left')
for i, x in enumerate((10, 35, 60)):
    box(ax, x, 62, 18, 14, 'sujet', label=r'$\frac{a}{b}$', size='l')
    if i < 2: text(ax, x + 22, 69, r'$\times$', 'sujet', 'l')
arrow(ax, (44, 61), (44, 51), 'varie')
text(ax, 48, 56, 'hauts ensemble, bas ensemble', 'varie', 's', ha='left')
box(ax, 14, 36, 60, 14, 'varie', label=r'$\frac{a\times a\times a}{b\times b\times b}$', size='m')
arrow(ax, (44, 35), (44, 26), 'resultat')
text(ax, 2, 16, 'Arrivée', 'resultat', 'm', ha='left')
box(ax, 29, 6, 30, 18, 'resultat', label=r'$\frac{a^3}{b^3}$', size='l')
save(fig, '14-049')
