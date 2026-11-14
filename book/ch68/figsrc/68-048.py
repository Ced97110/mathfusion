import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)

def bits(ax, x, y, s, roles, cw, ch=7.0, size='l'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

x = '10101'
zero = '00000'
cw = 10.0
x0 = 28
diff = [i for i in range(5) if x[i] != zero[i]]
assert diff == [i for i in range(5) if x[i] == '1'] and len(diff) == 3
text(ax, 44, 62, r'$w(x) = d(x, 0)$', 'sujet', 'l', weight='bold')
text(ax, 17, 47.5, r'$x$', 'sujet', 'l', weight='bold')
text(ax, 15, 26.5, r'mot nul', 'fixe', 's')
bits(ax, x0, 44, x, ['varie' if c == '1' else 'sujet' for c in x], cw)
bits(ax, x0, 23, zero, 'fixe', cw)
for i in range(5):
    cx = x0 + i * cw + cw / 2
    if i in diff:
        arrow(ax, (cx, 43), (cx, 31.5), 'varie', both=True)
    else:
        line(ax, [(cx, 43), (cx, 31.5)], 'fixe', dash=True)
text(ax, 44, 10, r'3 uns = 3 positions différentes', 'varie', 'm', weight='bold')
save(fig, '68-048')
