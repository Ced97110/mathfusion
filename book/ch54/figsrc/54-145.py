import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
w, u, yb = 9, 10, 14
X = lambda i: 16 + 20 * i
deg = [3, 2, 1, 0]
names = ['départ', 'ligne 1', 'ligne 2', 'ligne 3']
text(ax, 44, 58, 'le degré du reste baisse à chaque ligne', 'varie', 's')
line(ax, [(5, yb), (84, yb)], 'fixe')
line(ax, [(5, yb + u), (84, yb + u)], 'autre', dash=True)
text(ax, 76, yb + u + 4, 'diviseur : degré 1', 'autre', 's')
for i, d in enumerate(deg):
    role = 'resultat' if i == 3 else 'sujet'
    if d == 0:
        line(ax, [(X(i) - w / 2, yb), (X(i) + w / 2, yb)], role, lw=1.6)
    else:
        ax.add_patch(Rectangle((X(i) - w / 2, yb), w, d * u, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, X(i), yb + d * u + 3, str(d), role, 'm')
    text(ax, X(i), 8, names[i], 'fixe', 's')
for i in range(3):
    arrow(ax, (X(i) + 5, yb + deg[i] * u + 1), (X(i + 1) - 5, yb + deg[i + 1] * u + 5), 'varie')
text(ax, 70, 40,r'$0<1$ : on s’arrête', 'resultat', 's')
save(fig, '54-145')
