import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
X = [3, 25, 47, 69]; g = ['1', '3', '6', '10']; f = ['1', '2', '3', '4']
for i in range(4):
    gr = 'varie' if i >= 2 else 'sujet'
    box(ax, X[i], 32, 17, 12, gr, label=rf"$g({i})={g[i]}$", size='s')
    box(ax, X[i], 8, 17, 12, 'resultat' if i == 3 else 'sujet', label=rf"$f({i})={f[i]}$", size='s')
    if i < 3: arrow(ax, (X[i] + 17, 38), (X[i + 1], 38), 'fixe')
arrow(ax, (X[3] + 8.5, 32), (X[3] + 8.5, 20), 'varie')
text(ax, X[3] + 5, 26, r"$10-6=4$", 'varie', 's', ha='right')
save(fig, '80-417')
