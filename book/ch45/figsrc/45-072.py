import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
E = [r'$x^\prime y^\prime$', r'$\eta(x)\eta(y)$', r'$\eta(xy)$', r'$\eta(yx)$', r'$\eta(y)\eta(x)$', r'$y^\prime x^\prime$']
R = ['surjectivité', 'η conserve le produit', 'G commutatif', 'η conserve le produit', 'surjectivité']
for k in range(6):
    y = 94 - k * 17.5
    box(ax, 4, y, 30, 9, 'sujet' if k == 0 else 'resultat' if k == 5 else 'fixe', label=E[k])
    if k < 5:
        key = k in (0, 4)
        arrow(ax, (19, y - 0.5), (19, y - 8), 'varie' if key else 'fixe', lw=1.4 if key else 0.9)
        text(ax, 40, y - 4.2, R[k], 'varie' if key else 'fixe', 's', ha='left')
save(fig, '45-072')
