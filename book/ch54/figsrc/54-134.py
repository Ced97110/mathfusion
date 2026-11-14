import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
w, u = 7, 3
text(ax, 44, 65, r'dans ℤ/6 : $2\times3=6=0$', 'varie', 'm')
bx = 72
rows = [(46, r'$(2x)(x)=2x^2$', 'degré 2 : la règle marche', 'resultat', True),
        (14, r'$(2x)(3x)=6x^2=0$', r'degré $-\infty$, et non 2', 'limite', False)]
for yb, expr, verdict, role, bar in rows:
    line(ax, [(52, yb), (83, yb)], 'fixe')
    for xx in (58, 66, 74):
        line(ax, [(xx - w / 2, yb), (xx + w / 2, yb)], 'fixe', lw=1.2)
    text(ax, 2, yb + 10, expr, 'sujet', 'm', ha='left')
    text(ax, 2, yb + 3, verdict, role, 's', ha='left')
    if bar:
        ax.add_patch(Rectangle((74 - w / 2, yb), w, 2 * u, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
        text(ax, 74, yb + 2 * u + 3, '2', role, 's')
for xx, i in ((58, 0), (66, 1), (74, 2)):
    text(ax, xx, 5, str(i), 'fixe', 's')
save(fig, '54-134')
