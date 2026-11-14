import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
w, u = 7, 5
X = lambda i: 44 + 12 * i
rows = [(54, 'sujet', r'$f=x^2+x$ : degré 2', [0, 1, 1, 0]),
        (38, 'autre', r'$g=x^3$ : degré 3', [0, 0, 0, 1]),
        (22, 'resultat', r'$f+g$ : degré 3', [0, 1, 1, 1])]
for yb, role, lab, co in rows:
    line(ax, [(38, yb), (83, yb)], 'fixe')
    text(ax, 2, yb + 4, lab, role, 's', ha='left')
    for i, a in enumerate(co):
        if a == 0:
            line(ax, [(X(i) - w / 2, yb), (X(i) + w / 2, yb)], 'fixe', lw=1.2)
        else:
            ax.add_patch(Rectangle((X(i) - w / 2, yb), w, a * u, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
for i in range(4):
    text(ax, X(i), 14, str(i), 'fixe', 's')
text(ax, 2, 14, 'position :', 'fixe', 's', ha='left')
text(ax, 20, 5, r'$\max(2,3)=3$', 'resultat', 'm')
save(fig, '54-130')
