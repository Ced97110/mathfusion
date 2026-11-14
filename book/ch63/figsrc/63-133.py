import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'$\sigma\in G$, $\tau\in H=G(E/K)$, $\alpha\in K$', 'encre', 's')
w, gap = 14, 9.33
xs = [2 + i * (w + gap) for i in range(4)]
labs = [r'$\alpha$', '$\\sigma(\\alpha)$', '$\\tau\\sigma(\\alpha)$\n$=\\sigma(\\alpha)$', '$\\sigma^{-1}\\tau\\sigma(\\alpha)$\n$=\\alpha$']
roles = ['sujet', 'autre', 'autre', 'resultat']
for x, l, r in zip(xs, labs, roles):
    box(ax, x, 26, w, 12, role=r, label=l, size='s')
arr = [(r'$\sigma$', 'varie'), (r'$\tau$', 'fixe'), (r'$\sigma^{-1}$', 'varie')]
for i, (l, r) in enumerate(arr):
    arrow(ax, (xs[i] + w + 0.8, 32), (xs[i + 1] - 0.8, 32), r)
    text(ax, xs[i] + w + gap / 2, 36.5, l, r, 's')
text(ax, xs[1] + 7, 20, '∈ K (K normale)', 'autre', 's')
text(ax, xs[2] + 7, 14.5, 'τ fixe K', 'fixe', 's')
text(ax, 44, 5, r'$\sigma^{-1}\tau\sigma$ fixe $K$, donc $\in H$', 'resultat', 'm', weight='bold')
save(fig, '63-133')
