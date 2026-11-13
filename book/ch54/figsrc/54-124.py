import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
y0, u, w = 32, 5, 9
coef = [2, -1, 0, 5]
roles = ['autre', 'fixe', 'fixe', 'sujet']
X = lambda i: 16 + 18 * i
line(ax, [(5, y0), (83, y0)], 'fixe')
for i, a in enumerate(coef):
    if a == 0:
        line(ax, [(X(i) - w / 2, y0), (X(i) + w / 2, y0)], 'fixe', lw=1.2)
    else:
        h = a * u
        ax.add_patch(Rectangle((X(i) - w / 2, min(y0, y0 + h)), w, abs(h), ec=COL[roles[i]], fc=FILL[roles[i]], lw=0.8, zorder=2))
    text(ax, X(i), 17, str(i), 'fixe', 's')
text(ax, X(1), y0 - u - 3, r'$-1$', 'fixe', 's')
text(ax, X(0), y0 + 2 * u + 4, 'constant : 2', 'autre', 's')
text(ax, X(3), y0 + 5 * u + 4, 'dominant : 5', 'sujet', 's', weight='bold')
text(ax, 5, 24, 'position :', 'fixe', 's', ha='left')
arrow(ax, (X(3), 9), (X(3), 14), 'fixe')
text(ax, X(3), 5, 'degré = position 3', 'fixe', 's')
save(fig, '54-124')
