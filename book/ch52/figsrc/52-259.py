import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'$903\,070=9\,122\times99-8$', 'sujet', 'm')
text(ax, 44, 47, 'chaque ajout de 903 070 retire 8', 'varie', 's')
cx = [12, 33, 54, 75]; vals = [79, 71, 63, 55]
for i, (c, v) in enumerate(zip(cx, vals)):
    box(ax, c - 6.5, 20, 13, 10, 'resultat' if i == 3 else 'fixe', label=str(v))
    text(ax, c, 15, f'{i} ajout' + ('s' if i > 1 else ''), 'fixe', 's')
    if i < 3:
        arrow(ax, (c + 7, 25), (cx[i + 1] - 7, 25), 'varie')
        text(ax, c + 10.5, 29.5, r'$-8$', 'varie', 's')
text(ax, 75, 35, 'reste voulu', 'resultat', 's')
text(ax, 12, 35, 'reste de départ', 'fixe', 's')
save(fig, '52-259')
