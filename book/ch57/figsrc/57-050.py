import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
rows = [(36, '4', 'tripler', '12', 'ne rien changer', 'varie', 'fixe'),
        (14, '4', 'ne rien changer', '4', 'tripler', 'fixe', 'varie')]
for y, a, l1, b, l2, r1, r2 in rows:
    box(ax, 2, y, 12, 10, 'sujet', label=a)
    box(ax, 38, y, 12, 10, 'fixe', label=b)
    box(ax, 74, y, 12, 10, 'resultat', label='12')
    arrow(ax, (14.5, y + 5), (37.5, y + 5), r1)
    arrow(ax, (50.5, y + 5), (73.5, y + 5), r2)
    text(ax, 26, y + 9, l1, r1, 's')
    text(ax, 62, y + 9, l2, r2, 's')
text(ax, 44, 4, 'même résultat que « tripler »', 'resultat', 's')
save(fig, '57-050')
