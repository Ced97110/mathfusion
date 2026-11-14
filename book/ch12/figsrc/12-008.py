import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
y = 24
f = numberline(ax, 6, 70, y, -3, 4, every=1)
disc(ax, f(0), y, 1.7, 'encre'); text(ax, f(0), y + 5, r'$O$', 'encre', 'm')
disc(ax, f(-2), y, 1.7, 'sujet')
disc(ax, f(0.5), y, 1.7, 'varie'); text(ax, f(0.5), y + 11, r'$1/2$', 'varie', 's')
line(ax, [(f(0.5), y + 2), (f(0.5), y + 9)], 'varie', lw=0.6)
disc(ax, f(math.sqrt(2)), y, 1.7, 'resultat'); text(ax, f(math.sqrt(2)), y + 5, r'$\sqrt{2}$', 'resultat', 'm')
disc(ax, f(math.pi), y, 1.7, 'autre'); text(ax, f(math.pi), y + 5, r'$\pi$', 'autre', 'm')
brace(ax, f(0), f(1), y - 7, 'fixe', label='unité')
text(ax, 76, y + 4, 'sens', 'fixe', 's')
save(fig, '12-008')
