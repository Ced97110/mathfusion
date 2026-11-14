import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, 'coordonnées dans la base :', 'fixe', 's')
xs = [3, 25, 47, 69]; w = 16
vals = ['(1, 0)', '(2, 1)', '(5, 5)', '(0, 5)']
roles = ['sujet', 'autre', 'autre', 'resultat']
words = ['nouvelle', 'ancienne', 'ancienne', 'nouvelle']
for x, v, r, wd in zip(xs, vals, roles, words):
    box(ax, x, 30, w, 11, r, label=v, size='s', weight='bold')
    text(ax, x + w / 2, 47, wd, r, 's')
for i, lab in enumerate([r'$P$', r'$A$', r'$P^{-1}$']):
    x0 = xs[i] + w + 0.6; x1 = xs[i + 1] - 0.6
    arrow(ax, (x0, 35.5), (x1, 35.5), 'varie', lw=1.4)
    text(ax, (x0 + x1) / 2, 40.5 + 3.5, lab, 'varie', 's', weight='bold')
text(ax, 44, 20, r'$P^{-1}AP$', 'encre', 'l', weight='bold')
text(ax, 44, 12, 'se lit de droite à gauche', 'fixe', 's')
save(fig, '58-270')
