import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
y = 14
f = numberline(ax, 8, 64, y, 0, 4)
cols = [('ch. 1', '0, 1, 2, 3', 'sujet'), ('ch. 6', '1/2', 'varie'), ('ch. 8', '0,75', 'resultat'), ('ch. 11', r'$\pi$', 'autre')]
for i, (n, ex, r) in enumerate(cols):
    box(ax, 4 + 21 * i, 40, 19, 14, r, label=None)
    text(ax, 4 + 21 * i + 9.5, 49.5, n, r, 's', weight='bold')
    text(ax, 4 + 21 * i + 9.5, 44, ex, r, 's')
for v in (0, 1, 2, 3):
    disc(ax, f(v), y, 0.95, 'sujet')
disc(ax, f(0.5), y, 0.95, 'varie'); text(ax, f(0.5), y + 5, r'$1/2$', 'varie', 's')
disc(ax, f(0.75), y, 0.95, 'resultat'); text(ax, f(0.75), y + 10, '0,75', 'resultat', 's')
line(ax, [(f(0.75), y + 1.8), (f(0.75), y + 8)], 'resultat', lw=0.6)
disc(ax, f(math.pi), y, 0.95, 'autre'); text(ax, f(math.pi), y + 5, r'$\pi$', 'autre', 'm')
text(ax, 44, 30, 'tous sur la même droite', 'encre', 's')
save(fig, '12-006')
