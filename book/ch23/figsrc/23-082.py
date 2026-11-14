import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(68)
f = numberline(ax, 12, 76, 38, -2, 4, arrow_right=False)
g = lambda y: 38 + 2.6 * y
curve(ax, lambda x: (x - 1) ** 2 - 4, -1.8, 3.8, f, g, 'fixe')
disc(ax, f(1), 38, 1.3, 'sujet')
disc(ax, f(-1), 38, 1.3, 'resultat'); disc(ax, f(3), 38, 1.3, 'resultat')
disc(ax, f(1), g(-4), 1.1, 'sujet')
line(ax, [(f(1), 38), (f(1), g(-4))], 'sujet', dash=True)
brace(ax, f(-1), f(1), 42, 'varie', label=r'$\sqrt{D}/2a = 2$', down=False)
brace(ax, f(1), f(3), 42, 'varie', label=r'$\sqrt{D}/2a = 2$', down=False)
text(ax, f(1), 63, r'$x=-b/2a \ \pm \ \sqrt{D}/2a$', 'encre', 'm')
text(ax, f(1), g(-4) - 3.5, r'sommet : $-b/2a = 1$', 'sujet', 's')
text(ax, f(-1) - 2, 31, 'solution', 'resultat', 's', ha='right')
text(ax, f(3) + 2, 31, 'solution', 'resultat', 's', ha='left')
save(fig, '23-082')
