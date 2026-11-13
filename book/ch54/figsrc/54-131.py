import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
w, u = 7, 8
X = lambda i: 52 + 14 * i
rows = [(56, 'sujet', r'$f=x^2+x$ : degré 2', [0, 1, 1]),
        (36, 'autre', r'$g=-x^2$ : degré 2', [0, 0, -1]),
        (14, 'resultat', r'$f+g=x$ : degré 1', [0, 1, 0])]
ax.add_patch(Rectangle((X(2) - 6, 8), 12, 60, ec=COL['varie'], fc='none', lw=0.9, ls='--', zorder=1))
text(ax, X(2), 71, "s'annulent", 'varie', 's')
for yb, role, lab, co in rows:
    line(ax, [(46, yb), (83, yb)], 'fixe')
    text(ax, 2, yb + 4, lab, role, 's', ha='left')
    for i, a in enumerate(co):
        if a == 0:
            line(ax, [(X(i) - w / 2, yb), (X(i) + w / 2, yb)], 'fixe', lw=1.2)
        else:
            ax.add_patch(Rectangle((X(i) - w / 2, min(yb, yb + a * u)), w, abs(a * u), ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
for i in range(3):
    text(ax, X(i), 3.5, str(i), 'fixe', 's')
text(ax, 2, 3.5, 'position :', 'fixe', 's', ha='left')
save(fig, '54-131')
