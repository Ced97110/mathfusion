import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(58)
f = numberline(ax, 14, 74, 12, -3, 3, arrow_right=False)
g = lambda y: 12 + 2.2 * y
curve(ax, lambda x: x * x + 2 * x + 5, -3, 2.3, f, g, 'fixe')
vals = {-2: 5, -1: 4, 0: 5, 1: 8, 2: 13}
for x, y in vals.items():
    disc(ax, f(x), g(y), 1.1, 'sujet')
    if x == -1: text(ax, f(x), g(y) - 3.5, '4', 'sujet', 's')
    elif x < -1: text(ax, f(x) - 3.2, g(y), str(y), 'sujet', 's')
    else: text(ax, f(x) + 3.2, g(y), str(y), 'sujet', 's')
text(ax, 44, 53, r'$D=4-20=-16<0$', 'encre', 'm')
text(ax, 44, 46, 'aucun point sur l\u2019axe', 'sujet', 's')
save(fig, '23-095')
