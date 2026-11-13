import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 22, 42, 14, 11, 'varie', label=r'$-$', size='xl')
box(ax, 52, 42, 14, 11, 'sujet', label='5', size='xl')
text(ax, 29, 37, 'côté : gauche', 'varie', 's'); text(ax, 59, 37, 'distance : 5 pas', 'sujet', 's')
text(ax, 44, 56, r'$-5$ est un nombre', 'encre', 'm')
y = 14
f = numberline(ax, 8, 70, y, -5, 2, every=5, arrow_right=False)
line(ax, [(f(-5), y), (f(0), y)], 'sujet', lw=2.2)
disc(ax, f(-5), y, 1.8, 'sujet'); disc(ax, f(0), y, 1.3, 'fixe')
brace(ax, f(-5), f(0), y + 3, 'sujet', '5 pas', down=False)
save(fig, '13-026')
