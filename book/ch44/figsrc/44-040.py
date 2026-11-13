import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X = [14, 34, 54, 74]
for i, x in enumerate(X): disc(ax, x, 40, 4.5, 'resultat' if i == 3 else 'sujet' if i == 0 else 'fixe', label=str(i + 1), size='l')
for i, g in enumerate([r'$\alpha$', r'$\beta$', r'$\gamma$']):
    arrow(ax, (X[i] + 5, 40), (X[i + 1] - 5, 40), 'varie'); text(ax, (X[i] + X[i + 1]) / 2, 44.5, g, 'varie', 'm')
brace(ax, X[1], X[3], 50, 'autre', r'$(\gamma \circ \beta) \circ \alpha$', down=False)
brace(ax, X[0], X[2], 31, 'sujet', r'$\gamma \circ (\beta \circ \alpha)$', down=True)
text(ax, 44, 10, 'dans les deux cas, 1 arrive en 4', 'resultat', 'm')
save(fig, '44-040')
