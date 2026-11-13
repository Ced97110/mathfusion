import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [10, 30, 58, 78]
for x in xs: disc(ax, x, 58, 1.6, 'sujet' if x < 70 else 'resultat')
for (a, b), lab in zip(zip(xs, xs[1:]), [r'$\eta^{-1}$', r'$\tau_{u,c}$', r'$\eta$']):
    arrow(ax, (a + 2.5, 58), (b - 2.5, 58), 'varie'); text(ax, (a + b) / 2, 63, lab, 'varie', 's')
text(ax, 10, 51, r'$x=(3,1)$', 'sujet', 's'); text(ax, 78, 51, '(3, 4)', 'resultat', 's')
arrow(ax, (10, 55), (78, 55), 'autre', curve=0.22)
text(ax, 44, 42, r'$\tau_{\eta u,c}$', 'autre', 's')
text(ax, 44, 32, 'même point', 'resultat', 'm')
arrow(ax, (10, 8), (30, 8), 'sujet', lw=1.3); text(ax, 20, 3.5, r'$u$', 'sujet', 's')
arrow(ax, (38, 8), (52, 8), 'fixe'); text(ax, 45, 12, r'$\eta$', 'fixe', 's')
arrow(ax, (60, 4), (60, 18), 'autre', lw=1.3); text(ax, 66, 11, r'$\eta u$', 'autre', 's')
save(fig, '75-078')
