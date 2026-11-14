import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 14, 51, 'racines', 'fixe', 's')
text(ax, 44, 51, 'facteurs', 'fixe', 's')
text(ax, 76, 51, 'produit', 'fixe', 's')
rows = [(38, r'$i$', r'$x-i$'), (16, r'$-i$', r'$x+i$')]
for y, r, fct in rows:
    disc(ax, 14, y, 5, 'sujet', label=r)
    box(ax, 34, y - 6, 20, 12, 'varie', label=fct)
    arrow(ax, (19, y), (34, y), 'sujet')
    arrow(ax, (54, y), (66, 27 + (6 if y > 27 else -6) * 0.6), 'varie')
box(ax, 66, 20, 20, 14, 'resultat', label=r'$x^2+1$')
text(ax, 76, 15, 'degré 2', 'resultat', 's')
text(ax, 44, 4, 'un facteur par racine, une fois', 'sujet', 's')
save(fig, '66-039')
