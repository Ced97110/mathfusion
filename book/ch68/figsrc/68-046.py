import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)

def bits(ax, x, y, s, roles, cw, ch=7.0, size='l'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

x, y = '10101', '11010'
diff = [i for i in range(5) if x[i] != y[i]]
assert len(diff) == 4
cw = 10.0
x0 = 28
text(ax, 44, 56, 'positions où les mots diffèrent', 'encre', 'm', weight='bold')
text(ax, 18, 43.5, r'$x$', 'sujet', 'l', weight='bold')
text(ax, 18, 22.5, r'$y$', 'autre', 'l', weight='bold')
bits(ax, x0, 40, x, ['varie' if i in diff else 'sujet' for i in range(5)], cw)
bits(ax, x0, 19, y, ['varie' if i in diff else 'autre' for i in range(5)], cw)
for i in range(5):
    cx = x0 + i * cw + cw / 2
    if i in diff:
        arrow(ax, (cx, 39), (cx, 27.5), 'varie', both=True)
    else:
        line(ax, [(cx, 39), (cx, 27.5)], 'fixe', dash=True)
brace(ax, x0 + cw, x0 + 5 * cw, 19, 'varie', label=r'$d(x, y) = 4$', size='m')
text(ax, x0 + cw / 2, 33, '=', 'fixe', 'm')
save(fig, '68-046')
