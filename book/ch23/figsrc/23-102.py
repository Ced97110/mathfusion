import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X0, Y0, u = 24, 34, 4.2
arrow(ax, (X0 - 19, Y0), (X0 + 19, Y0), 'fixe', lw=0.9)
n = 60
line(ax, [(X0 + u * x, Y0 + u * (x * x - 4)) for x in [-3 + 6 * i / n for i in range(n + 1)]], 'sujet', lw=1.3)
line(ax, [(X0 - 2 * u, Y0), (X0 + 2 * u, Y0)], 'resultat', lw=2.4)
for x in (-2, 2):
    ax.plot([X0 + u * x], [Y0], 'o', color=COL['encre'], ms=3.5, zorder=4)
    text(ax, X0 + u * x + (-4 if x < 0 else 4), Y0 - 3.8, f'{x}'.replace('-', '−'), 'resultat', 's')
text(ax, X0, Y0 - 7, r'$y<0$', 'resultat', 's')
text(ax, X0 - 14.5, Y0 + 3.5, r'$y>0$', 'fixe', 's')
text(ax, X0 + 14.5, Y0 + 3.5, r'$y>0$', 'fixe', 's')
text(ax, X0, 60, r'$y=x^2-4$', 'sujet', 'm')
# zoom near -2
box(ax, 48, 24, 38, 38, 'fixe', False, None, dash=True)
Z = 43
text(ax, 67, 58, 'zoom près de −2', 'fixe', 's')
arrow(ax, (50, Z), (84, Z), 'fixe', lw=0.9)
line(ax, [(54, Z + 8), (82, Z - 8)], 'sujet', lw=1.3)
for xx, v, lab, vl, up in [(60, 4.57, '−2,1', '0,41', True), (76, -4.57, '−1,9', '−0,39', False)]:
    ax.plot([xx], [Z + v], 'o', color=COL['varie'], ms=3.5, zorder=4)
    text(ax, xx, Z + v + (4.5 if up else -4.5), vl, 'varie', 's')
    text(ax, xx, Z - 3.5 if up else Z + 3.5, lab, 'fixe', 's')
ax.plot([68], [Z], 'o', color=COL['resultat'], ms=4, zorder=4)
text(ax, 68, Z - 3.5, '−2', 'resultat', 's')
text(ax, 68, 30, 'le signe change', 'varie', 's')
save(fig, '23-102')
