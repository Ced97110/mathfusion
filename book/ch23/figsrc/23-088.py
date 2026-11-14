import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(70)
f = numberline(ax, 6, 74, 12, -3, 4)
g = lambda y: 36 + 4.5 * y
curve(ax, lambda x: x * x, -1.9, 1.9, f, g, 'fixe')
curve(ax, lambda x: (x - 1) ** 2 - 4, -0.9, 2.9, f, g, 'sujet')
disc(ax, f(0), g(0), 1.2, 'fixe'); disc(ax, f(1), g(-4), 1.3, 'resultat')
arrow(ax, (f(0) + 1.5, g(0)), (f(1) - 1, g(0)), 'varie')
arrow(ax, (f(1), g(0) - 1.5), (f(1), g(-4) + 2), 'varie')
text(ax, f(0.5), g(0) - 3.2, 'droite : 1', 'varie', 's')
text(ax, f(1) - 1.5, g(-2), 'bas : 4', 'varie', 's', ha='right')
text(ax, f(0), g(0) + 3, '(0 ; 0)', 'fixe', 's')
text(ax, f(1) + 2.5, g(-4) - 3, '(1 ; −4)', 'resultat', 's', ha='left')
text(ax, 20, 64, r'départ : $y=x^2$', 'fixe', 's')
text(ax, 62, 64, r'$y=(x-1)^2-4$', 'sujet', 's')
save(fig, '23-088')
