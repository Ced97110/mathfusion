import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
for x, role, lab in [(4, 'varie', r'$x^5$'), (34, 'varie', r'$x^3$'), (64, 'resultat', r'$x$')]:
    box(ax, x, 58, 20, 12, role, label=lab, size='l')
arrow(ax, (25, 64), (33, 64), 'fixe'); arrow(ax, (55, 64), (63, 64), 'fixe')
text(ax, 29, 52, 'retire\n' + r'$x^2(x^3-x)$', 'varie', 's')
text(ax, 59, 52, 'retire\n' + r'$(x^3-x)$', 'varie', 's')
f = numberline(ax, 8, 62, 30, 0, 5, arrow_right=False)
for v, role in [(5, 'varie'), (3, 'varie'), (1, 'resultat')]:
    ax.add_patch(Circle((f(v), 30), 1.4, ec=COL[role], fc=COL[role], zorder=4))
arrow(ax, (f(5), 32), (f(3), 32), 'varie', curve=0.5)
arrow(ax, (f(3), 32), (f(1), 32), 'varie', curve=0.5)
brace(ax, f(0), f(2), 22, 'resultat', label=r'exposants $< q = 3$')
text(ax, 44, 8, r'les exposants descendent sous $q$', 'encre', 's')
save(fig, '55-058')
