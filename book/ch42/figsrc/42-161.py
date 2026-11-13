import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
cols = [30 + 16 * i for i in range(3)]
rows = {'a': 32, 'b': 16}
for x in cols: line(ax, [(x, 10), (x, 38)], 'fixe', lw=0.6)
for y in rows.values(): line(ax, [(22, y), (70, y)], 'fixe', lw=0.6)
for x, n in zip(cols, '123'): text(ax, x, 44, n, 'sujet', 'm')
for n, y in rows.items(): text(ax, 17, y, rf'${n}$', 'sujet', 'm')
text(ax, 6, 44, r'$S$', 'sujet', 'l', weight='bold'); text(ax, 6, 24, r'$T$', 'sujet', 'l', weight='bold')
line(ax, [(cols[1], 40), (cols[1], rows['b'])], 'varie', dash=True)
line(ax, [(22, rows['b']), (cols[1], rows['b'])], 'varie', dash=True)
for x in cols:
    for y in rows.values():
        hit = (x == cols[1] and y == rows['b'])
        disc(ax, x, y, 2.8 if hit else 2.2, 'varie' if hit else 'sujet')
text(ax, cols[1], 7, r'$(2,\,b)$', 'varie', 'm')
save(fig, '42-161')
