import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(64)
f = numberline(ax, 14, 74, 18, -1, 3, arrow_right=False)
g = lambda y: 44 + 4 * y
curve(ax, lambda x: (x - 1) ** 2 - 4, -1, 3, f, g, 'sujet')
line(ax, [(f(-1), g(-4)), (f(3), g(-4))], 'resultat', dash=True)
line(ax, [(f(1), g(-4)), (f(1), 18)], 'resultat', dash=True)
for x in (0, 1, 2):
    disc(ax, f(x), g((x - 1) ** 2 - 4), 1.1, 'resultat' if x == 1 else 'sujet')
text(ax, f(0) - 4.5, g(-3) + 0.5, '−3', 'sujet', 's')
text(ax, f(2) + 4.5, g(-3) + 0.5, '−3', 'sujet', 's')
text(ax, f(1) + 3, g(-4) - 3, 'minimum : −4', 'resultat', 's', ha='left')
text(ax, 24, 58, r'$y=(x-1)^2-4$', 'sujet', 'm')
box(ax, 50, 53, 36, 9, 'varie', label='un carré est ≥ 0', size='s')
arrow(ax, (68, 53), (f(1) + 6, g(-4) + 3), 'varie', curve=-0.25)
save(fig, '23-080')
