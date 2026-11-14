import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
xs = [3 + i * 17.5 for i in range(5)]; w = 12; h = 11
rows = [(50, 'sujet', [r'$\mathbb{Z}$', r'$9\mathbb{Z}$', r'$45\mathbb{Z}$', r'$180\mathbb{Z}$', r'$\{0\}$'], r'$\mathbb{Z}$ est abélien'),
        (26, 'autre', [r'$\mathbb{Z}/24$', r'$\langle2\rangle$', r'$\langle6\rangle$', r'$\langle12\rangle$', r'$\{0\}$'], r'$\mathbb{Z}/24$ abélien ; $\langle2\rangle$ : multiples de 2')]
for y, role, labs, cap in rows:
    for x, l in zip(xs, labs):
        box(ax, x, y, w, h, role, label=l, size='s')
    for i in range(4):
        arrow(ax, (xs[i] + w + 0.3, y + h / 2), (xs[i + 1] - 0.3, y + h / 2), 'fixe')
    text(ax, 44, y + h + 3.5, cap, role, 's')
box(ax, 8, 2, 72, 11, 'resultat', fill=False, dash=True, label='abélien : tout terme est normal dans G', size='s')
save(fig, '64-038')
