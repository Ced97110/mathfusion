import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
w, u = 7, 2.5
X = lambda i: 34 + 12 * i
rows = [(86, 'sujet', r'$f=2+3x$ : degré 1', [2, 3, 0, 0]),
        (62, 'autre', r'$g=1+4x^2$ : degré 2', [1, 0, 4, 0]),
        (10, 'resultat', r'$fg$ : degré 3', [2, 3, 8, 12])]
for yb, role, lab, co in rows:
    line(ax, [(28, yb), (83, yb)], 'fixe')
    text(ax, 2, yb + 5, lab, role, 's', ha='left')
    for i, a in enumerate(co):
        r = role
        if yb == 10 and i < 3:
            r = 'fixe'
        if a == 0:
            line(ax, [(X(i) - w / 2, yb), (X(i) + w / 2, yb)], 'fixe', lw=1.2)
        else:
            ax.add_patch(Rectangle((X(i) - w / 2, yb), w, a * u, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))
text(ax, X(1), 86 + 3 * u + 3, '3', 'sujet', 's')
text(ax, X(2), 62 + 4 * u + 3, '4', 'autre', 's')
text(ax, X(3), 10 + 12 * u + 3, '12', 'resultat', 's')
text(ax, X(3) - 2, 56, r'rangs $1+2=3$', 'resultat', 's')
arrow(ax, (X(3), 52), (X(3), 10 + 12 * u + 8), 'resultat')
text(ax, 2, 46, r'seul couple de rangs', 'resultat', 's', ha='left')
text(ax, 2, 41, r'qui s’ajoutent en 3 :', 'resultat', 's', ha='left')
text(ax, 2, 36, r'$3\times4=12$', 'resultat', 'm', ha='left')
for i in range(4):
    text(ax, X(i), 3.5, str(i), 'fixe', 's')
save(fig, '54-133')
