import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(62)
box(ax, 10, 51, 68, 9, 'sujet', label='équation : deux solutions', size='m')
f = numberline(ax, 6, 80, 32, -9, 5, arrow_right=False, labels=False)
text(ax, f(0), 28.5, '0', 'fixe', 's')
arrow(ax, (30, 51), (f(-7.83), 38), 'fixe', lw=0.8); arrow(ax, (58, 51), (f(3.83), 38), 'resultat', lw=0.8)
disc(ax, f(-7.83), 32, 1.4, 'fixe', fill=False); disc(ax, f(3.83), 32, 1.4, 'resultat')
text(ax, f(-7.83), 36, '−7,83', 'fixe', 's'); text(ax, f(3.83), 36, '3,83', 'resultat', 's')
brace(ax, f(-9), f(0) - 1, 25, 'fixe', label='pas une largeur', down=True)
brace(ax, f(0) + 1, f(5), 25, 'resultat', label='largeur possible', down=True)
box(ax, 2, 4, 40, 8, 'fixe', label='−7,83 : écartée', size='s')
box(ax, 46, 4, 40, 8, 'resultat', label='3,83 : gardée', size='s')
save(fig, '23-091')
