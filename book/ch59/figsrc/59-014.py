import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 64, r'entiers $\mathbb{Z}$', 'sujet', 'm')
text(ax, 66, 64, r'polynômes $F[x]$', 'autre', 'm')
line(ax, [(44, 8), (44, 68)], 'fixe', dash=True)
text(ax, 22, 54, r'$17=3\times5+2$', 'sujet', 's')
text(ax, 66, 54, r'$A=Q\,B+R$', 'autre', 's')
# barres de taille
for (cx, role, hb, hr, lb, lr) in [(22, 'sujet', 20, 8, '5', '2'), (66, 'autre', 20, 11, r'deg $B$', r'deg $R$')]:
    box(ax, cx - 14, 18, 11, hb, role, label=None)
    box(ax, cx + 3, 18, 11, hr, role, label=None)
    text(ax, cx - 8.5, 13, lb, role, 's'); text(ax, cx + 8.5, 13, lr, role, 's')
text(ax, 22, 42, 'valeur absolue', 'fixe', 's')
text(ax, 66, 42, 'degré', 'fixe', 's')
text(ax, 44, 4, 'le reste est plus petit que le diviseur', 'encre', 's')
save(fig, '59-014')
