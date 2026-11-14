import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(66)
f = numberline(ax, 12, 76, 40, -2, 4, arrow_right=False)
g = lambda y: 40 + 2.6 * y
curve(ax, lambda x: (x - 1) ** 2 - 4, -1.8, 3.8, f, g, 'sujet')
line(ax, [(f(1), 12), (f(1), 58)], 'varie', lw=1.3, dash=True)
text(ax, f(1) + 2, 60, 'axe x = 1', 'varie', 'm', ha='left')
for a, b, h in ((0, 2, -3), (-1, 3, 0)):
    for x in (a, b): disc(ax, f(x), g(h), 1.1, 'sujet')
    arrow(ax, (f(a) + 1.5, g(h)), (f(b) - 1.5, g(h)), 'fixe', lw=0.8, both=True)
text(ax, f(0) - 3, g(-3), 'même hauteur', 'fixe', 's', ha='right')
text(ax, f(1) + 2.5, g(-4) - 3.5, 'sommet', 'sujet', 's', ha='left')
disc(ax, f(1), g(-4), 1.2, 'varie')
save(fig, '23-083')
