import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
f = numberline(ax, 6, 76, 14, 0, 35, 5, every=2, arrow_right=False)
y = 14
for v, r in ((25, 'sujet'), (16, 'resultat'), (34, 'autre')):
    disc(ax, f(v), y, 1.5, r)
    text(ax, f(v), 6.5, str(v), r, 'm', weight='bold')
arrow(ax, (f(25), y + 2.5), (f(16) + 0.5, y + 2.5), 'varie', curve=0.5)
arrow(ax, (f(25), y + 2.5), (f(34) - 0.5, y + 2.5), 'varie', curve=-0.5)
text(ax, (f(25) + f(16)) / 2, 26, '− 9 : on retire', 'varie', 's')
text(ax, f(34) - 2, 24, '+ 9', 'varie', 's')
text(ax, 28, 38, '25 − 9 = 16', 'resultat', 'l', weight='bold')
text(ax, 68, 38, '25 + 9 = 34', 'autre', 'l', weight='bold')
save(fig, '18-049')
