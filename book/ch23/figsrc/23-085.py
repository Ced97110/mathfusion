import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(60)
text(ax, 44, 54, r'$x=1\ \pm\ 2$', 'encre', 'l')
f = numberline(ax, 10, 70, 28, -2, 4, arrow_right=False, labels=False)
disc(ax, f(1), 28, 1.4, 'sujet'); disc(ax, f(-1), 28, 1.4, 'resultat'); disc(ax, f(3), 28, 1.4, 'resultat')
text(ax, f(1), 22.5, 'milieu 1', 'sujet', 's')
arrow(ax, (f(1) - 1.5, 37), (f(-1) + 0.5, 37), 'varie'); arrow(ax, (f(1) + 1.5, 37), (f(3) - 0.5, 37), 'varie')
text(ax, (f(1) + f(-1)) / 2, 41, '− 2', 'varie', 's'); text(ax, (f(1) + f(3)) / 2, 41, '+ 2', 'varie', 's')
box(ax, 3, 4, 38, 10, 'resultat', label='x = 1 − 2 = −1', size='s')
box(ax, 47, 4, 38, 10, 'resultat', label='x = 1 + 2 = 3', size='s')
arrow(ax, (f(-1), 26), (22, 14.5), 'fixe', lw=0.8); arrow(ax, (f(3), 26), (66, 14.5), 'fixe', lw=0.8)
save(fig, '23-085')
