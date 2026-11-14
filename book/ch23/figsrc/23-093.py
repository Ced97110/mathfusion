import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(64)
box(ax, 2, 49, 32, 10, 'sujet', label='D = 625', size='m')
f = numberline(ax, 42, 76, 54, 24, 26, arrow_right=False)
disc(ax, f(25), 54, 1.4, 'resultat'); text(ax, f(25), 60, 'racine : 25', 'resultat', 's')
box(ax, 2, 32, 84, 8, 'resultat', label=r'25 entier : $(x-12)(x+13)$', size='s')
box(ax, 2, 17, 32, 10, 'autre', label='D = 136', size='m')
g = numberline(ax, 42, 76, 22, 11, 12, arrow_right=False)
disc(ax, g(136 ** 0.5), 22, 1.4, 'autre'); text(ax, g(136 ** 0.5), 28, r'$\sqrt{136}$', 'autre', 's')
box(ax, 2, 2, 84, 8, 'fixe', label='pas entier : pas de couple', size='s')
save(fig, '23-093')
