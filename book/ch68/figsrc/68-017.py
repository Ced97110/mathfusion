import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
xs = [10, 30, 52, 76]
roles = ['sujet', 'sujet', 'varie', 'varie']
for x, w, r in zip(xs, ['000', '001', '011', '111'], roles):
    disc(ax, x, 28, 5.2, r, label=w, size='s')
for a, b in [(0, 1), (1, 2), (2, 3)]:
    line(ax, [(xs[a] + 5.2, 28), (xs[b] - 5.2, 28)], 'fixe')
line(ax, [(41, 8), (41, 43)], 'fixe', dash=True)
text(ax, 41, 47, 'aucun mot dans les deux boules', 'encre', 's')
brace(ax, 10, 52, 35, 'sujet', label='2 arêtes de 000', down=False)
brace(ax, 52, 76, 21, 'varie', label='1 arête de 111', down=True)
text(ax, 44, 5, 'mot reçu 011 : une seule couleur, orange', 'varie', 's')
save(fig, '68-017')
