import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$(a+I)(b+I)=ab+I$', 'sujet', 'l')
steps = (('prendre un élément', r'3 dans $\bar{3}$, 2 dans $\bar{2}$', 'varie'),
         (r'multiplier dans $\mathbb{Z}$', r'3 $\times$ 2 = 6', 'fixe'),
         ('reprendre la classe', r'6 = 1 $\times$ 4 + 2 : $\bar{2}$', 'resultat'))
for k, (t, d, r) in enumerate(steps):
    y = 50 - k * 22
    box(ax, 4, y, 80, 16, r, label=None)
    text(ax, 44, y + 11, t, r, 's', weight='bold')
    text(ax, 44, y + 4.5, d, 'encre', 'm')
    if k < 2: arrow(ax, (44, y - 0.5), (44, y - 5.5), 'varie')
save(fig, '52-071')
