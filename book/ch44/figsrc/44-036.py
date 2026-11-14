import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
X = [12, 44, 76]
def lane(y, vals, first, second, title):
    text(ax, 44, y + 11, title, 'sujet', 'm')
    for x, v, r in zip(X, vals, ['sujet', 'fixe', 'resultat']): disc(ax, x, y, 5, r, label=str(v), size='l')
    for (a, b), g in zip([(X[0], X[1]), (X[1], X[2])], [first, second]):
        role = 'varie' if g == r'$\alpha$' else 'autre'
        arrow(ax, (a + 5.5, y), (b - 5.5, y), role); text(ax, (a + b) / 2, y + 4.5, g, role, 'l')
lane(50, [1, 4, 1], r'$\alpha$', r'$\beta$', r'$\beta \circ \alpha$ : $\alpha$ d’abord')
lane(20, [1, 2, 3], r'$\beta$', r'$\alpha$', r'$\alpha \circ \beta$ : $\beta$ d’abord')
text(ax, 76, 35, r'$\neq$', 'limite', 'l')
save(fig, '44-036')
