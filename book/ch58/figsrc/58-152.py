import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# colonnes : alpha * (3,1) + beta * (1,2) = (0,0), lues ligne par ligne
box(ax, 6, 76, 76, 12, 'sujet', label=r'$\alpha\times(3,\,1)\ +\ \beta\times(1,\,2)\ =\ (0,\,0)$')
# deux lignes lues
box(ax, 6, 56, 36, 9, 'fixe', label=r'$3\alpha+\beta=0$')
box(ax, 46, 56, 36, 9, 'fixe', label=r'$\alpha+2\beta=0$')
text(ax, 24, 68, '1ʳᵉ case', 'fixe', 's')
text(ax, 64, 68, '2ᵉ case', 'fixe', 's')
# calcul pas à pas
rows = [(r'$\beta=-3\alpha$', 'varie', 'tiré de la 1ʳᵉ'),
        (r'$\alpha-6\alpha=-5\alpha=0$', 'varie', 'dans la 2ᵉ'),
        (r'$\alpha=0$ puis $\beta=0$', 'resultat', 'donc')]
y = 44
for lab, role, note in rows:
    box(ax, 30, y - 4, 52, 8, role, label=lab)
    text(ax, 4, y, note, 'fixe', 's', ha='left')
    y -= 13
    if y > 10: arrow(ax, (56, y + 13 - 4), (56, y + 4), 'varie')
box(ax, 6, 3, 76, 7, 'resultat', label='seule la combinaison triviale', weight='bold')
save(fig, '58-152')
