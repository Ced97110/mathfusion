import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
w, u = 7, 8
text(ax, 44, 55, r'$D[x]$ : qui est inversible ?', 'encre', 'm')
text(ax, 23, 45, r'$x$ : degré 1', 'sujet', 'm')
text(ax, 65, 45, 'constante : degré 0', 'fixe', 'm')
for x0, role, bp in ((10, 'sujet', 1), (52, 'fixe', 0)):
    yb = 28
    line(ax, [(x0 - 6, yb), (x0 + 36, yb)], 'fixe')
    for i in range(3):
        xx = x0 + 12 * i
        if i == bp:
            ax.add_patch(Rectangle((xx - w / 2, yb), w, u, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
        else:
            line(ax, [(xx - w / 2, yb), (xx + w / 2, yb)], 'fixe', lw=1.2)
        text(ax, xx, 21, str(i), 'fixe', 's')
text(ax, 23, 10, 'jamais inversible', 'limite', 'm')
text(ax, 65, 10, 'peut l’être', 'resultat', 'm')
save(fig, '54-140')
