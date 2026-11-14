import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
w, u = 7, 2
X = lambda i: 44 + 12 * i
for yb in (44, 22):
    line(ax, [(37, yb), (83, yb)], 'fixe')
    for i in range(4):
        line(ax, [(X(i) - w / 2, yb), (X(i) + w / 2, yb)], 'fixe', lw=1.2)
ax.add_patch(Rectangle((X(0) - w / 2, 44), w, 5 * u, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, zorder=2))
text(ax, 4, 52, 'constant 5', 'fixe', 'm', ha='left')
text(ax, 4, 44, r'degré $0$', 'fixe', 'm', ha='left')
text(ax, 4, 30, 'polynôme nul', 'sujet', 'm', ha='left', weight='bold')
text(ax, 4, 22, r'degré $-\infty$', 'sujet', 'm', ha='left', weight='bold')
text(ax, 60, 30, 'aucune barre non nulle', 'sujet', 's')
for i in range(4):
    text(ax, X(i), 12, str(i), 'fixe', 's')
text(ax, 4, 12, 'position :', 'fixe', 's', ha='left')
save(fig, '54-126')
