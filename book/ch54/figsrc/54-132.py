import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
w, u = 7, 3
X = lambda i: 46 + 14 * i
b1, b2 = 56, 26
text(ax, 2, 61, r'$2x$ : degré 1', 'sujet', 'm', ha='left')
for yb in (b1, b2):
    line(ax, [(41, yb), (84, yb)], 'fixe')
    for i in range(3):
        line(ax, [(X(i) - w / 2, yb), (X(i) + w / 2, yb)], 'fixe', lw=1.2)
ax.add_patch(Rectangle((X(1) - w / 2, b1), w, 2 * u, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
text(ax, X(1), b1 + 2 * u + 3, '2', 'sujet', 's')
ax.add_patch(Rectangle((X(2) - w / 2, b2), w, 4 * u, ec=COL['limite'], fc='none', lw=0.9, ls='--', zorder=2))
text(ax, X(2), b2 + 4 * u + 3, '4', 'limite', 's')
text(ax, 68, b2 + 4 * u + 9, 'prévu : degré 2', 'limite', 's')
text(ax, 2, 38, r'$(2x)(2x)=4x^2$', 'sujet', 'm', ha='left')
text(ax, 2, 30, r'dans ℤ/4 : $4=0$', 'varie', 'm', ha='left')
text(ax, 2, 22, r'réel : degré $-\infty$', 'sujet', 'm', ha='left', weight='bold')
for i in range(3):
    text(ax, X(i), 15, str(i), 'fixe', 's')
text(ax, 2, 15, 'position :', 'fixe', 's', ha='left')
save(fig, '54-132')
