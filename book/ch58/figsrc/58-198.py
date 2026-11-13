import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# la case a_ji : ligne j, colonne i ; ici ligne 1, colonne 2
cw, ch = 11, 10
mx, my = 24, 22
vals = [['2', '1'], ['1', '3']]
for j in range(2):
    for i in range(2):
        if (j, i) == (0, 1): role = 'resultat'
        elif j == 0: role = 'varie'
        elif i == 1: role = 'sujet'
        else: role = 'fixe'
        box(ax, mx + i * (cw + 1.5), my + (1 - j) * (ch + 1.5), cw, ch, role, label=vals[j][i], size='m', r=0.5,
            weight='bold' if (j, i) == (0, 1) else 'normal')
text(ax, mx + cw / 2, 54, r'$e_1$', 'fixe', 's')
text(ax, mx + cw * 1.5 + 1.5, 54, r'$e_2$', 'sujet', 's', weight='bold')
text(ax, mx - 4, my + ch + 1.5 + ch / 2, r'$f_1$', 'varie', 's', weight='bold')
text(ax, mx - 4, my + ch / 2, r'$f_2$', 'fixe', 's')
text(ax, mx + cw * 1.5 + 0.75, 59, r'colonne $i = 2$ : image de $e_2$', 'sujet', 's')
text(ax, mx - 1, 15,r'ligne $j = 1$ : lots de type $f_1$', 'varie', 's', ha='left')
text(ax, 72, 38.5, r'$a_{12} = 1$', 'resultat', 'm', weight='bold')
arrow(ax, (63, 38.5), (mx + 2 * cw + 3.5, 38.5), 'resultat', lw=1.0)
save(fig, '58-198')
