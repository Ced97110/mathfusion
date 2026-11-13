import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
y0, u, w = 42, 5, 7
coef = [2, -1, 0, 5, 0, 0]
last = 3
X = lambda i: 12 + 12 * i
line(ax, [(5, y0), (83, y0)], 'fixe')
for i, a in enumerate(coef):
    role = 'sujet' if i == last else 'fixe'
    if a == 0:
        line(ax, [(X(i) - w / 2, y0), (X(i) + w / 2, y0)], 'fixe', lw=1.2)
    else:
        h = a * u
        ax.add_patch(Rectangle((X(i) - w / 2, min(y0, y0 + h)), w, abs(h), ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, X(i), 29, str(i), 'fixe', 's')
text(ax, X(0), y0 + 2 * u + 3, '2', 'fixe', 's')
text(ax, X(1), y0 - u - 3, r'$-1$', 'fixe', 's')
text(ax, X(3), y0 + 5 * u + 3, '5', 'sujet', 's')
text(ax, X(3), y0 + 5 * u + 9, 'dernière barre non nulle', 'sujet', 's')
text(ax, 5, 24, 'position :', 'fixe', 's', ha='left')
arrow(ax, (X(3), 15), (X(3), 25.5), 'sujet')
text(ax, X(3), 11, r'degré $=3$', 'sujet', 'm', weight='bold')
save(fig, '54-122')
