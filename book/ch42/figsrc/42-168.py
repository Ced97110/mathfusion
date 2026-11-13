import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
lc = [12, 24, 36]; lr = {'a': 22, 'b': 34}
rc = {'a': 64, 'b': 76}; rr = [16, 28, 40]
for x, n in zip(lc, '123'): text(ax, x, 44, n, 'sujet', 's')
for n, y in lr.items(): text(ax, 5, y, rf'${n}$', 'autre', 's')
for n, x in rc.items(): text(ax, x, 50, rf'${n}$', 'autre', 's')
for n, y in zip('123', rr): text(ax, 56, y, n, 'sujet', 's')
for x in lc:
    for y in lr.values():
        hit = (x == 24 and y == 34); disc(ax, x, y, 2.8 if hit else 2.1, 'varie' if hit else 'sujet')
for x in rc.values():
    for y in rr:
        hit = (x == 76 and y == 28); disc(ax, x, y, 2.8 if hit else 2.1, 'varie' if hit else 'autre')
text(ax, 24, 58, r'$S\times T$', 'sujet', 'm', weight='bold'); text(ax, 70, 58, r'$T\times S$', 'autre', 'm', weight='bold')
text(ax, 24, 8, r'$(2,\,b)$', 'varie', 'm'); text(ax, 70, 8, r'$(b,\,2)$', 'varie', 'm')
for dy in (-1.6, 1.6): line(ax, [(43.5, 28 + dy), (50.5, 28 + dy)], 'limite', lw=1.3)
line(ax, [(45, 24.5), (49, 31.5)], 'limite', lw=1.3)
save(fig, '42-168')
