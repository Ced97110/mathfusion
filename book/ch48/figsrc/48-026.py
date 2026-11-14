import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [3 + i * 17 for i in range(3)]
for x in xs:
    box(ax, x, 48, 13, 10, 'sujet', label='5'); box(ax, x, 14, 13, 10, 'autre', label='1')
    arrow(ax, (x + 6.5, 47), (x + 6.5, 25), 'varie'); text(ax, x + 9, 36, r'$f$', 'varie', 's', ha='left')
text(ax, xs[1] + 6.5, 63, r'$a^k$ : 3 facteurs égaux', 'sujet', 's')
text(ax, 72, 53, '= 15', 'sujet'); text(ax, 72, 19, '= 3', 'autre')
text(ax, xs[1] + 6.5, 4, r'$f(a)^k$ : 3 facteurs égaux', 'autre', 's')
for i in range(2):
    text(ax, xs[i] + 15, 53, '+', 'sujet'); text(ax, xs[i] + 15, 19, '+', 'autre')
save(fig, '48-026')
