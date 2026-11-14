import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
X0, Y0, sx, sy = 14, 12, 15.0, 1.4
f = numberline(ax, X0, X0 + 4 * sx, Y0, 0, 4, arrow_right=False)
h = lambda t: 20 * t - 5 * t * t
line(ax, [(f(t), Y0 + sy * h(t)) for t in [4 * i / 60 for i in range(61)]], 'sujet', lw=1.3)
for t in range(5):
    r = 'resultat' if t == 2 else 'sujet'
    ax.plot([f(t)], [Y0 + sy * h(t)], 'o', color=COL[r], ms=3.5, zorder=4)
    text(ax, f(t), Y0 + sy * h(t) + 4.5, f'{h(t):g}', r, 'm')
text(ax, f(2) + 14, Y0 + sy * 20 + 4.5, 'sommet', 'resultat', 's')
text(ax, 20, 50, 'hauteur (m)', 'fixe', 's')
text(ax, f(4), Y0 - 9.5, 'temps (s)', 'fixe', 's')
save(fig, '23-103')
