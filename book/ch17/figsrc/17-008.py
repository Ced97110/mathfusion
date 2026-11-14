import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 8, 71, 22, 0, 7, arrow_right=True)
text(ax, 84, 28, r'$d$', 'fixe', 's')
line(ax, [(f(0), 22), (f(6), 22)], 'resultat', lw=2.4)
for k in range(1, 60):
    ax.add_patch(Circle((f(6 * k / 60), 22), 0.5, ec='none', fc=COL['resultat'], zorder=3))
for v in (2.5, 4, 6):
    disc(ax, f(v), 22, 1.9, 'resultat')
    text(ax, f(v), 31, str(v).replace('.', ','), 'resultat', 's')
text(ax, 44, 48, 'toutes ces distances sont justes', 'resultat', 's')
text(ax, f(6) + 12, 38, '… sans fin', 'fixe', 's')
save(fig, '17-008')
