import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(74)
box(ax, 9, 64, 70, 8, 'sujet', label=r'$x^2+x-156=0$', size='s')
box(ax, 9, 52, 70, 8, 'sujet', label=r'$D=1+624=625=25^2$', size='s')
box(ax, 9, 40, 70, 8, 'resultat', label=r'$x=(-1\pm25)/2$ : 12 et $-13$', size='s')
arrow(ax, (44, 64), (44, 60.5), 'fixe'); arrow(ax, (44, 52), (44, 48.5), 'fixe')
f = numberline(ax, 8, 80, 22, -14, 14, arrow_right=False, labels=False)
text(ax, f(0), 18.5, '0', 'fixe', 's')
for v, r in ((12, 'sujet'), (13, 'sujet'), (-13, 'autre'), (-12, 'autre')): disc(ax, f(v), 22, 1.1, r)
text(ax, f(12.5), 28, '12 : 12 et 13', 'sujet', 's'); text(ax, f(-12.5)+4, 28, '−13 : −13 et −12', 'autre', 's')
text(ax, f(12.5) - 2, 12, 'produit 156', 'sujet', 's'); text(ax, f(-12.5) + 2, 12, 'produit 156', 'autre', 's')
save(fig, '23-092')
