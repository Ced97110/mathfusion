import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$x_i \rightarrow x_{\pi(i)}$', 'varie', 'xl')
pi = {1: 2, 2: 1, 3: 3}
ys = {1: 54, 2: 38, 3: 22}
for i in (1, 2, 3):
    role = 'varie' if pi[i] != i else 'fixe'
    disc(ax, 14, ys[i], 4.6, 'sujet', label=rf'$x_{i}$')
    disc(ax, 46, ys[pi[i]], 4.6, 'autre', label=rf'$x_{pi[i]}$')
for i in (1, 2, 3):
    role = 'varie' if pi[i] != i else 'fixe'
    arrow(ax, (19, ys[i]), (41, ys[pi[i]]), role)
    text(ax, 68, ys[i], rf'$\pi({i})={pi[i]}$', 'encre', 'm')
text(ax, 14, 11, 'avant', 'sujet', 's')
text(ax, 46, 11, 'après', 'autre', 's')
save(fig, '55-061')
