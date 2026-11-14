import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [3, 33, 63]; w = 22; y = 38; h = 15
labs = [r'$G$' + '\n6 éléments', r'$G^{(1)}$' + '\n3 éléments', r'$G^{(2)}=\{e\}$' + '\n1 élément']
roles = ['sujet', 'sujet', 'resultat']
for x, l, r in zip(xs, labs, roles):
    box(ax, x, y, w, h, r, label=l, size='s')
for i in range(2):
    arrow(ax, (xs[i] + w + 0.4, y + h / 2), (xs[i + 1] - 0.4, y + h / 2), 'varie')
    text(ax, (xs[i] + w + xs[i + 1]) / 2, y + h + 3, 'dérivé', 'varie', 's')
text(ax, 66, 31, 'on s’arrête : résoluble', 'resultat', 's', weight='bold')
box(ax, 3, 4, 82, 16, 'limite', fill=False, dash=True,
    label=r'si $G^{(k+1)}=G^{(k)}$ sans être $\{e\}$' + '\nla suite ne change plus : non résoluble', size='s')
save(fig, '64-059')
