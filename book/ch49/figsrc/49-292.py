import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 74, 'action libre', 'sujet', 'm', weight='bold')
text(ax, 66, 74, 'action triviale', 'autre', 'm', weight='bold')
line(ax, [(44, 4), (44, 78)], 'fixe', dash=True)
text(ax, 22, 66, 'points fixes', 'fixe', 's'); text(ax, 66, 66, 'points fixes', 'fixe', 's')
labsL = ['$e$', '$r$', '$r^2$', '$r^3$']; valsL = ['4', '0', '0', '0']
for i in range(4):
    x = 4 + i * 9.5
    text(ax, x + 4, 59, labsL[i], 'fixe', 's')
    box(ax, x, 49, 8, 7, 'sujet' if i == 0 else 'fixe', label=valsL[i])
for i, (l, v) in enumerate([('$e$', '5'), ('$g$', '5')]):
    x = 55 + i * 12
    text(ax, x + 4, 59, l, 'fixe', 's')
    box(ax, x - 1, 49, 10, 7, 'autre', label=v)
arrow(ax, (22, 46), (22, 40), 'varie'); arrow(ax, (66, 46), (66, 40), 'varie')
text(ax, 22, 36, 'somme : 4', 'encre', 'm'); text(ax, 66, 36, 'somme : 10', 'encre', 'm')
arrow(ax, (22, 32), (22, 26), 'varie'); arrow(ax, (66, 32), (66, 26), 'varie')
text(ax, 22, 22, r'$4 \div 4 = 1$', 'resultat', 'l'); text(ax, 66, 22, r'$10 \div 2 = 5$', 'resultat', 'l')
text(ax, 22, 14, '1 orbite', 'resultat', 's'); text(ax, 66, 14, '5 orbites', 'resultat', 's')
text(ax, 22, 8, r'$k = |S| / |G|$', 'sujet', 's'); text(ax, 66, 8, r'$k = |S|$', 'autre', 's')
save(fig, '49-292')
