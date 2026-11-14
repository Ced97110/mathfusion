import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, k = 44, 36, 27
X = lambda x: cx + k * x; Y = lambda y: cy + k * y
text(ax, 44, 77, r'$\sin 3\theta = 3\sin\theta - 4\sin^3\theta$', 'sujet', 'm')
ax.add_patch(Rectangle((X(-1.25), Y(-1)), X(1.25) - X(-1.25), Y(1) - Y(-1), fc=FILL['resultat'], ec='none', zorder=0.5))
line(ax, [(X(-1.25), cy), (X(1.25), cy)], 'fixe', lw=0.7); line(ax, [(cx, Y(-1.2)), (cx, Y(1.2))], 'fixe', lw=0.7)
for yy in (1, -1): line(ax, [(X(-1.25), Y(yy)), (X(1.25), Y(yy))], 'resultat', dash=True, lw=0.8)
xs = [i / 100 for i in range(-100, 101)]
line(ax, [(X(x), Y(3 * x - 4 * x ** 3)) for x in xs], 'sujet', lw=1.3)
for px, py in ((0.5, 1), (1, -1)): ax.add_patch(Circle((X(px), Y(py)), 1.4, fc=COL['resultat'], ec='none', zorder=4))
text(ax, X(0.5) + 3, Y(1) + 3.5, r'$\theta=30°$ : $0{,}5\to 1$', 'resultat', 's', ha='left')
text(ax, X(1) - 2, Y(-1) - 4, r'$\theta=90°$ : $1\to -1$', 'resultat', 's', ha='right')
text(ax, X(-1.25) + 1, Y(1) + 3, r'$1$', 'resultat', 's', ha='left'); text(ax, X(-1.25) + 1, Y(-1) - 3, r'$-1$', 'resultat', 's', ha='left')
text(ax, X(-0.95), Y(0.6), r'$3x-4x^3$', 'sujet', 's')
text(ax, X(1.2), cy + 3, r'$x=\sin\theta$', 'fixe', 's', ha='right')
text(ax, 18, Y(1) + 3.5, r'reste dans $[-1,\ 1]$', 'resultat', 's', ha='left')
save(fig, '34-139')
