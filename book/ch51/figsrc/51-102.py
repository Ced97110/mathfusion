import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, x1, y0, S = 8, 76, 24, 40.0   # [0,1] -> 68 mm ; 1 unité de valeur = 40 mm
X = lambda t: x0 + t * (x1 - x0)
Y = lambda v: y0 + v * S
line(ax, [(X(0), Y(0)), (X(1), Y(0))], 'fixe', lw=0.9)
for t, lab in [(0, '0'), (0.25, r'$\frac{1}{4}$'), (0.5, r'$\frac{1}{2}$'), (0.75, r'$\frac{3}{4}$'), (1, '1')]:
    line(ax, [(X(t), Y(0) - 1), (X(t), Y(0) + 1)], 'fixe'); text(ax, X(t), Y(0) - 4.5, lab, 'fixe', 's')
line(ax, [(X(0), Y(0.5)), (X(0.5), Y(0))], 'sujet', lw=1.6)
line(ax, [(X(0.5), Y(0)), (X(1), Y(0.5))], 'autre', lw=1.6)
line(ax, [(X(0.5), Y(0.0) + 0.0), (X(1), Y(0))], 'sujet', lw=1.6)
line(ax, [(X(0), Y(0)), (X(0.5), Y(0))], 'autre', lw=1.6)
text(ax, X(0.06), Y(0.5) + 4, r'$f$', 'sujet', 'm'); text(ax, X(0.94), Y(0.5) + 4, r'$g$', 'autre', 'm')
for t, v, role in [(0.25, 0.25, 'sujet'), (0.75, 0.25, 'autre')]:
    ax.plot([X(t)], [Y(v)], 'o', color=COL[role], ms=3.5, zorder=6)
text(ax, X(0.25) + 4, Y(0.25) + 5, r'$f=\frac{1}{4}$', 'sujet', 's')
text(ax, X(0.75) - 4, Y(0.25) + 5, r'$g=\frac{1}{4}$', 'autre', 's')
text(ax, X(0.25), Y(0) - 1.2 + 6.0 - 6.0 + 7, r'$g=0$', 'autre', 's') if False else None
text(ax, 44, 10, r'$f \times g = 0$ en chaque point', 'resultat', 's')
box(ax, 10, 1.5, 68, 0.1, 'resultat', fill=False) if False else None
line(ax, [(X(0), 15.5), (X(1), 15.5)], 'resultat', lw=2.0)
save(fig, '51-102')
