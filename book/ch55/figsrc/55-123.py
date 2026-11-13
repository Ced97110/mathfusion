import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# same polynomial x^2 - 5x + 6, roots 2 and 3, two numberings
box(ax, 14, 60, 60, 9, 'fixe', label=r'mêmes coefficients : $x^2-5x+6$', size='s')
text(ax, 20, 53, 'numérotation', 'fixe', 's')
text(ax, 52, 53, r'$r_1+r_2$', 'resultat', 's')
text(ax, 75, 53, r'$r_1-r_2$', 'varie', 's')
rows = [(r'$r_1=2,\ r_2=3$', 2, 3), (r'$r_1=3,\ r_2=2$', 3, 2)]
y = 38
for lab, a, b in rows:
    box(ax, 3, y, 34, 9, 'sujet', label=lab, size='s')
    box(ax, 42, y, 20, 9, 'resultat', label=str(a + b), size='m')
    box(ax, 65, y, 20, 9, 'varie', label=str(a - b).replace('-', '−'), size='m')
    y -= 14
text(ax, 52, 19, 'même valeur', 'resultat', 's')
text(ax, 75, 19, 'deux valeurs', 'varie', 's')
text(ax, 44, 8, r'$r_1-r_2$ ne vient pas des coefficients', 'encre', 's')
save(fig, '55-123')
