import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(44, r'$x + 3 = 8$', r'$x = 5$', 'retour'), (24, r'$x \times 3 = 12$', r'$x = 4$', 'retour'), (4, r'$x^2 = 25$', r'$x = 5$ ou $x = -5$', 'retour')]
for y, q, a, l in rows:
    box(ax, 3, y, 30, 12, 'sujet', label=q)
    box(ax, 50, y, 35, 12, 'resultat', label=a)
    arrow(ax, (34, y + 6), (49, y + 6), 'varie')
    text(ax, 41.5, y + 9.5, l, 'varie', 's')
save(fig, '80-483')
