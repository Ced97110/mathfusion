import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 80, 'deux nombres de produit 20', 'fixe', 's')
rows = [('1 et 20 : 1 divise 20', r'$\mathbb{Z}/20$', True),
        ('2 et 10 : 2 divise 10', r'$\mathbb{Z}/2\oplus\mathbb{Z}/10$', True),
        ('4 et 5 : 4 ne divise pas 5', '', False),
        ('5 et 4 : 5 ne divise pas 4', '', False),
        ('10 et 2 : 10 ne divise pas 2', '', False)]
for k, (a, b, ok) in enumerate(rows):
    y = 66 - k * 13
    box(ax, 2, y, 54, 9, 'resultat' if ok else 'limite', label=a, size='s')
    if ok:
        arrow(ax, (57, y + 4.5), (62, y + 4.5), 'varie')
        box(ax, 63, y, 23, 9, 'resultat', label=b, size='s')
text(ax, 44, 9, 'deux candidats seulement', 'resultat', 's', weight='bold')
save(fig, '59-146')
