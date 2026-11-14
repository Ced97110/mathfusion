import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'trois pas de $\sigma$', 'encre', 'm')
xs = [30, 46, 62, 78]
r = 3.5
def row(y, letters, roles):
    for x, s, ro in zip(xs, letters, roles):
        disc(ax, x, y, r, ro, label=s, size='s')
    for i in range(3):
        arrow(ax, (xs[i] + r + 0.5, y), (xs[i + 1] - r - 0.5, y), 'varie')
y1, y2 = 52, 26
text(ax, 2, y1, '3-cycle', 'encre', 's', ha='left')
row(y1, [r'$a$', r'$b$', r'$c$', r'$a$'], ['sujet', 'fixe', 'fixe', 'resultat'])
text(ax, 54, y1 - 10, r'$\sigma^3$ = identité', 'resultat', 'm')
text(ax, 2, y2, 'échange', 'encre', 's', ha='left')
row(y2, [r'$d$', r'$e$', r'$d$', r'$e$'], ['sujet', 'fixe', 'fixe', 'varie'])
text(ax, 54, y2 - 10, r'$\sigma^3$ = échange', 'varie', 'm')
save(fig, '67-217')
