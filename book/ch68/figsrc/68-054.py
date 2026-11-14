import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)

def bits(ax, x, y, s, roles, cw, ch=7.0, size='l'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

x, y = '10101', '11010'
diff = [i for i in range(5) if x[i] != y[i]]
assert len(diff) == 4
cw = 8.0
x0 = 14
text(ax, 7, 47.5, r'$x$', 'sujet', 'l', weight='bold')
text(ax, 7, 21.5, r'$y$', 'autre', 'l', weight='bold')
bits(ax, x0, 44, x, ['varie' if i in diff else 'sujet' for i in range(5)], cw)
bits(ax, x0, 18, y, ['varie' if i in diff else 'autre' for i in range(5)], cw)
for i in diff:
    cx = x0 + i * cw + cw / 2
    arrow(ax, (cx, 43), (cx, 26), 'varie', both=True)
text(ax, 70, 44, r'$d(x, y) = 4$', 'varie', 'l', weight='bold')
text(ax, 70, 34, '=', 'fixe', 'l')
text(ax, 70, 24, r'$d(y, x) = 4$', 'varie', 'l', weight='bold')
text(ax, 44, 8, 'mêmes positions dans les deux sens', 'varie', 'm')
save(fig, '68-054')
