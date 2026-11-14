import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, 'plan (dimension 2)', 'resultat', 'm', weight='bold')
bw, bh, g = 16, 10, 8
x0 = 44 - (3 * bw + 2 * g) / 2
y = 50
for k, l in enumerate(['(1, 0)', '(0, 1)', '(1, 0)']):
    x = x0 + k * (bw + g)
    box(ax, x, y, bw, bh, 'resultat', label=l, size='s')
    if k < 2:
        arrow(ax, (x + bw + 0.4, y + bh / 2), (x + bw + g - 0.4, y + bh / 2), 'varie')
text(ax, 44, 44, 'la suite revient : torsion', 'resultat', 's')
text(ax, 44, 32, 'polynômes (dimension infinie)', 'limite', 'm', weight='bold')
labs = ['1', r'$\lambda$', r'$\lambda^2$', r'$\lambda^3$', '…']
bw2, g2 = 11, 6
x1 = 44 - (5 * bw2 + 4 * g2) / 2
y2 = 14
for k, l in enumerate(labs):
    x = x1 + k * (bw2 + g2)
    box(ax, x, y2, bw2, bh, 'limite', label=l, size='s')
    if k < 4:
        arrow(ax, (x + bw2 + 0.3, y2 + bh / 2), (x + bw2 + g2 - 0.3, y2 + bh / 2), 'varie')
text(ax, 44, 8, 'jamais liés : pas de torsion', 'limite', 's')
text(ax, 44, 2.5, r'chaque flèche : $\times\,\lambda$', 'fixe', 's')
save(fig, '60-148')
