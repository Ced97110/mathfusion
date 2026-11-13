import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
d = 7.6; x0 = (W - 8 * d) / 2 + d / 2; y = 34
box(ax, x0 - d / 2 - 1, y - 6, 4 * d + 2, 12, 'sujet')
box(ax, x0 + 4 * d - d / 2 + 1, y - 6, 4 * d - 2, 12, 'fixe')
for i in range(8): disc(ax, x0 + i * d, y, 2.4, 'sujet' if i < 4 else 'fixe')
brace(ax, x0 - d / 2, x0 + 7.5 * d, y + 8, 'sujet', r'$|G|$ = 8', down=False, depth=2.4)
text(ax, x0 + 1.5 * d, y - 11, r'$C(y)$ : 4 éléments', 'sujet', 's')
text(ax, x0 + 5.5 * d, y - 11, '4 éléments', 'fixe', 's')
text(ax, W / 2, 14, r'indice $[G:C(y)] = 8 \div 4 = 2$', 'resultat', 'm', weight='bold')
text(ax, W / 2, 6, '2 > 1 et 2 divise 8', 'resultat', 'm')
save(fig, '49-184')
