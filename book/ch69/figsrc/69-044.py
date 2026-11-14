import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
items = ['ordonné', '(i) racines carrées', '(ii) impair : une racine']
for k, t in enumerate(items):
    y = 50 - 14 * k
    box(ax, 2, y, 36, 10, 'fixe', label=t, size='s')
    arrow(ax, (39, y + 5), (47, 36), 'varie')
box(ax, 48, 26, 38, 20, 'sujet', label=r'$R$ réel clos', size='l')
text(ax, 67, 14, r'$\mathbb{R}$ : les trois', 'resultat', 's')
text(ax, 67, 6, r'$\mathbb{Q}$ : (i) manque', 'limite', 's')
save(fig, '69-044')
