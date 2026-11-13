import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# les 9 listes de 2 cases, chaque case prise parmi 0, 1, 2 (horloge à trois heures)
c = 15.0
x0, y0 = 26, 16
for i in range(3):          # i : valeur de la 1re case (ligne)
    for j in range(3):      # j : valeur de la 2e case (colonne)
        box(ax, x0 + c * j, y0 + c * (2 - i), c, c, 'resultat', label=f'({i}, {j})', size='m')
brace(ax, x0, x0 + 3 * c, y0 + 3 * c + 1, 'varie', label='2e case : 3 valeurs', down=False)
text(ax, 11, y0 + 1.5 * c + 5, '1re case :', 'sujet', 's')
text(ax, 11, y0 + 1.5 * c, '3 valeurs', 'sujet', 's')
line(ax, [(21.5, y0), (21.5, y0 + 3 * c)], 'sujet', lw=0.9)
text(ax, x0 + 1.5 * c, y0 - 5, r'$3 \times 3 = 9$ listes', 'resultat', 'l', weight='bold')
save(fig, '58-338')
