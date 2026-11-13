import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(66)
f = numberline(ax, 20, 68, 8, -2, 2, arrow_right=False)
g = lambda h: 8 + 0.6 * h
line(ax, [(f(0), 8), (f(0), 49)], 'fixe')
curve(ax, lambda t: 64 - 16 * t * t, -2, 0, f, g, 'fixe', dash=True)
curve(ax, lambda t: 64 - 16 * t * t, 0, 2, f, g, 'sujet')
disc(ax, f(0), g(64), 1.3, 'resultat'); disc(ax, f(1), g(48), 1.1, 'sujet'); disc(ax, f(2), g(0), 1.1, 'sujet')
disc(ax, f(-1), g(48), 1.1, 'fixe')
text(ax, f(0) + 3, g(64) + 4, 'sommet : 64', 'resultat', 's', ha='left')
text(ax, f(1) + 3.5, g(48) + 1, '48', 'sujet', 's'); text(ax, f(-1) - 3.5, g(48) + 1, '48', 'fixe', 's')
text(ax, f(2) - 2, g(0) + 4, 'sol : 0', 'sujet', 's', ha='right')
text(ax, 44, 61, r'$h=64-16t^2$', 'sujet', 'm')
text(ax, 44, 56, r'$a=-16<0$', 'varie', 's')
text(ax, 80, 12, 't', 'fixe', 's'); text(ax, f(0) - 4, 3, 'avant le lâcher : sans sens', 'fixe', 's', ha='right') if False else None
text(ax, f(-1.1), 22, 'temps négatif', 'fixe', 's')
save(fig, '23-087')
