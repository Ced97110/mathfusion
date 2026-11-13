import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
for x, s in ((12, 'classes'), (35, 'représentants'), (60, 'produit'), (77, 'classe')):
    text(ax, x, 79, s, 'varie', 's')
box(ax, 2, 28, 20, 20, 'sujet', label=None); text(ax, 12, 38, r'$\bar{3}\cdot\bar{2}$', 'sujet', 'm')
box(ax, 70, 28, 14, 20, 'resultat', label=r'$\bar{2}$', size='l')
for k, (a, p) in enumerate((('3 et 2', '6'), ('7 et 6', '42'), ('−1 et 10', '−10'))):
    y = 62 - k * 24 + 0
    y = (66, 38, 10)[k]
    box(ax, 26, y - 5, 18, 10, 'varie', label=a, size='s')
    text(ax, 60, y, p, 'fixe', 'm')
    arrow(ax, (22.5, 38), (25.5, y), 'varie'); arrow(ax, (44.5, y), (55, y), 'varie'); arrow(ax, (65, y), (69.5, 38), 'varie')
save(fig, '52-076')
