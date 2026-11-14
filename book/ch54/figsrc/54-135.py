import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
w, u = 6, 3
X = lambda i: 10 + 10 * i
rows = [(72, 'sujet', r'$p=3+3x^3$', {0: 3, 3: 3}),
        (46, 'autre', r'$q=4+4x^2+4x^4$', {0: 4, 2: 4, 4: 4}),
        (20, 'resultat', r'$pq$ : coefficients tous nuls', {})]
for yb, role, lab, co in rows:
    line(ax, [(5, yb), (84, yb)], 'fixe')
    text(ax, 2, yb + (16 if yb > 20 else 8), lab, role, 'm', ha='left')
    for i in range(8):
        a = co.get(i, 0)
        if a == 0:
            line(ax, [(X(i) - w / 2, yb), (X(i) + w / 2, yb)], 'fixe', lw=1.2)
        else:
            ax.add_patch(Rectangle((X(i) - w / 2, yb), w, a * u, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
for i in range(8):
    text(ax, X(i), 12, str(i), 'fixe', 's')
text(ax, 44, 4, r'chaque rang : $3\times4=12=0$ dans ℤ/12', 'varie', 's')
save(fig, '54-135')
