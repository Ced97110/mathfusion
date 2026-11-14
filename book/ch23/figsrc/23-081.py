import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(62)
box(ax, 14, 50, 60, 10, 'sujet', label=r'$x=-b\,/\,(2a)$', size='l')
f = numberline(ax, 50, 78, 10, -3, 2, arrow_right=False)
rows = [('b = −2, a = 1 : 2 / 2', 1, 38), ('b = 4, a = 1 : −4 / 2', -2, 29), ('b = −4, a = 2 : 4 / 4', 1, 20)]
for s, v, y in rows:
    text(ax, 2, y, s, 'encre', 's', ha='left')
    disc(ax, f(v), y, 1.2, 'varie')
    line(ax, [(f(v), y - 1.2), (f(v), 10)], 'fixe', dash=True)
text(ax, f(1) + 5, 38, '1', 'varie', 's')
text(ax, f(-2) - 4, 29, '−2', 'varie', 's')
text(ax, f(1) + 5, 20, '1', 'varie', 's')
text(ax, 44, 45, 'même règle, résultat différent', 'fixe', 's')
save(fig, '23-081')
