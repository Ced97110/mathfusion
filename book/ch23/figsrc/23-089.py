import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(64)
box(ax, 2, 46, 36, 11, 'sujet', label=r'$x(x+4)=30$', size='s')
box(ax, 2, 28, 36, 11, 'sujet', label=r'$x^2+4x-30=0$', size='s')
box(ax, 2, 8, 36, 14, 'resultat', label=r'$D=136$' + '\n' + r'$x=-2+\sqrt{34}$', size='s')
arrow(ax, (20, 46), (20, 39.5), 'fixe'); arrow(ax, (20, 28), (20, 22.5), 'fixe')
x0, u, hh = 50, 4.6, 3.83 * 4.6
poly(ax, [(x0, 10), (x0 + 7.83 * u, 10), (x0 + 7.83 * u, 10 + hh), (x0, 10 + hh)], 'sujet')
brace(ax, x0, x0 + 7.83 * u, 10 + hh + 2, 'fixe', label='7,83 = 3,83 + 4', down=False)
text(ax, x0 - 2, 10 + hh / 2, '3,83', 'sujet', 's', ha='right')
text(ax, x0 + 7.83 * u / 2, 10 + hh / 2, 'aire ≈ 29,99', 'sujet', 's')
text(ax, x0 + 7.83 * u / 2, 4.5, 'proche de 30, pas égal', 'fixe', 's')
save(fig, '23-089')
