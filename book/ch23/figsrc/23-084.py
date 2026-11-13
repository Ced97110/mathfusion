import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(80)
f = numberline(ax, 14, 70, 60, -1, 3, arrow_right=False)
d = 2
disc(ax, f(1 - d), 60, 1.3, 'autre'); disc(ax, f(1 + d), 60, 1.3, 'sujet'); disc(ax, f(1), 60, 1.0, 'fixe')
arrow(ax, (f(1) - 1.5, 66), (f(1 - d) + 0.5, 66), 'varie'); arrow(ax, (f(1) + 1.5, 66), (f(1 + d) - 0.5, 66), 'varie')
text(ax, (f(1) + f(1 - d)) / 2, 69, 'd', 'varie', 's'); text(ax, (f(1) + f(1 + d)) / 2, 69, 'd', 'varie', 's')
text(ax, f(1 - d), 73, '1 − d', 'autre', 's'); text(ax, f(1 + d), 73, '1 + d', 'sujet', 's')
text(ax, 44, 77, r'$y=(x-1)^2-4$', 'encre', 's')
box(ax, 2, 28, 41, 16, 'autre', label='x = 1 − d\n(−d)² − 4 = d² − 4', size='s')
box(ax, 45, 28, 41, 16, 'sujet', label='x = 1 + d\nd² − 4', size='s')
arrow(ax, (22, 28), (38, 17), 'fixe'); arrow(ax, (66, 28), (50, 17), 'fixe')
box(ax, 14, 4, 60, 12, 'resultat', label='même hauteur : d² − 4', size='s')
save(fig, '23-084')
