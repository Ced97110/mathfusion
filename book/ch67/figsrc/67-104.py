import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [16, 44, 72]
for x, m in zip(xs, ('1', '2', '4')): disc(ax, x, 60, 6, 'varie', label=r'$m=$' + m, size='s')
text(ax, 30, 48, 'diviseurs de 4', 'varie', 's')
fs = [r'$\mathbb{F}_{2^1}$', r'$\mathbb{F}_{2^2}$', r'$\mathbb{F}_{2^4}$']
cs = ['2 éléments', '4 éléments', '16 éléments']
for x, f, c in zip(xs, fs, cs):
    arrow(ax, (x, 53.5), (x, 36), 'varie')
    box(ax, x - 12, 22, 24, 12, 'sujet', label=f, size='m')
    text(ax, x, 15, c, 'sujet', 's')
for a, b in ((0, 1), (1, 2)): arrow(ax, (xs[a] + 13, 28), (xs[b] - 13, 28), 'fixe')
text(ax, 44, 4, 'un seul sous-corps par diviseur', 'resultat', 's')
save(fig, '67-104')
