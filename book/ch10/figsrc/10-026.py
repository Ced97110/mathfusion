import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, '≈ : les nombres changent', 'varie', 's')
for x, a, b in [(12, '53,82', '54'), (58, '41,6', '42')]:
    text(ax, x, 49, a, 'fixe', 'l'); text(ax, x + 12, 49, '≈', 'varie', 'xl', weight='bold'); text(ax, x + 22, 49, b, 'sujet', 'l')
text(ax, 44, 33, '= : après, le calcul est exact', 'resultat', 's')
text(ax, 20, 24, r'$54 + 42$', 'sujet', 'l'); text(ax, 40, 24, '=', 'resultat', 'xl', weight='bold'); text(ax, 52, 24, '96', 'resultat', 'l')
text(ax, 22, 8, 'valeur exacte : 95,42', 'fixe', 's'); text(ax, 66, 8, 'écart : 0,58', 'varie', 's')
save(fig, '10-026')
