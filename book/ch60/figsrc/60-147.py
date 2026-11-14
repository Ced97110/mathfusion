import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'multiplier par $\lambda$  =  appliquer $T$', 'varie', 'l', weight='bold')
bw, bh, y = 22, 12, 28
xs = [4, 33, 62]
labs = ['(1, 0)', '(0, 1)', '(1, 0)']
roles = ['sujet', 'varie', 'sujet']
for x, l, r in zip(xs, labs, roles):
    box(ax, x, y, bw, bh, r, label=l, size='m')
for x in xs[:2]:
    arrow(ax, (x + bw + 0.4, y + bh / 2), (x + bw + 6.6, y + bh / 2), 'varie')
    text(ax, x + bw + 3.5, y + bh / 2 + 4.5, r'$\times\,\lambda$', 'varie', 's')
text(ax, 44, 20, 'deux échanges se compensent', 'fixe', 's')
text(ax, 44, 9, r'$(\lambda^2 - 1)\,x = (0, 0)$', 'resultat', 'm', weight='bold')
save(fig, '60-147')
