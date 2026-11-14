import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
w, u = 7, 4
X = lambda i: 52 + 12 * i
rows = [(56, 'sujet', 'constante 2', {0: 2}),
        (36, 'autre', 'constante 3', {0: 3}),
        (14, 'resultat', 'leur produit : nul', {})]
for yb, role, lab, co in rows:
    line(ax, [(46, yb), (84, yb)], 'fixe')
    text(ax, 2, yb + 5, lab, role, 'm', ha='left')
    for i in range(3):
        a = co.get(i, 0)
        if a == 0:
            line(ax, [(X(i) - w / 2, yb), (X(i) + w / 2, yb)], 'fixe', lw=1.2)
        else:
            ax.add_patch(Rectangle((X(i) - w / 2, yb), w, a * u, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
            text(ax, X(i), yb + a * u + 3, str(a), role, 's')
for i in range(3):
    text(ax, X(i), 6, str(i), 'fixe', 's')
text(ax, 2, 6, 'position :', 'fixe', 's', ha='left')
text(ax, 2, 75, r'dans ℤ/6 : $2\times3=0$', 'varie', 'm', ha='left')
save(fig, '54-136')
