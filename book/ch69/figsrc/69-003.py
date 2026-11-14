import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
y0, s, cx = 14, 30, 44
xs = [-1 + i * 2 / 80 for i in range(81)]
ax.plot([cx + x * s for x in xs], [y0 + (x * x - 0.01) * s for x in xs], color=COL['sujet'], lw=1.2, zorder=3)
arrow(ax, (8, y0), (82, y0), 'fixe', lw=0.9)
for v in (-1, 1):
    line(ax, [(cx + v * s, y0 - 1), (cx + v * s, y0 + 1)], 'fixe')
    line(ax, [(cx + v * s, y0 + 1.5), (cx + v * s, y0 + 0.99 * s - 2)], 'varie', lw=0.6, dash=True)
    disc(ax, cx + v * s, y0 + 0.99 * s, 1.6, 'varie')
text(ax, cx - s, 9.5, '−1', 'fixe', 's')
text(ax, cx + s, 9.5, '1', 'fixe', 's')
text(ax, 3, 49, 'g(−1) = 0,99', 'varie', 's', ha='left')
text(ax, 85, 49, 'g(1) = 0,99', 'varie', 's', ha='right')
for v in (-0.1, 0.1):
    disc(ax, cx + v * s, y0, 1.1, 'resultat')
text(ax, cx - 4, 9.5, '−0,1', 'resultat', 's', ha='right')
text(ax, cx + 4, 9.5, '0,1', 'resultat', 's', ha='left')
text(ax, cx, 26, '2 racines cachées', 'resultat', 's')
arrow(ax, (cx, 23.8), (cx, 17), 'resultat', lw=0.9)
text(ax, cx, 59, r'$g(x)=x^2-0{,}01$', 'sujet', 'm')
save(fig, '69-003')
