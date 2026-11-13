import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(36)
y = 24
f = numberline(ax, 6, 70, y, -4, 4, labels=False)
line(ax, [(f(0), y), (f(3), y)], 'sujet', lw=2.2)
line(ax, [(f(-3), y), (f(0), y)], 'autre', lw=2.2)
disc(ax, f(3), y, 1.6, 'sujet'); disc(ax, f(-3), y, 1.6, 'autre'); disc(ax, f(0), y, 1.3, 'fixe')
text(ax, f(0), y + 5, '0', 'fixe', 's')
text(ax, f(3), y + 5, r'$P$', 'sujet', 'm'); text(ax, f(-3), y + 5, r'$Q$', 'autre', 'm')
brace(ax, f(0), f(3), y - 3.5, 'sujet', '3 pas')
brace(ax, f(-3), f(0), y - 3.5, 'autre', '3 pas')
text(ax, f(1.5), 6, r'$|3| = 3$', 'sujet', 'l'); text(ax, f(-1.5), 6, r'$|-3| = 3$', 'autre', 'l')
save(fig, '13-017')
