import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
data = [(r'$7$', r'$x$', 'x'), (r'$2$', r'$y$', 'y'), (r'$-8$', r'$z$', 'z')]
for i, (c, l, n) in enumerate(data):
    cx = 15 + i * 29
    box(ax, cx - 12, 26, 12, 11, 'sujet', label=c); box(ax, cx + 1, 26, 11, 11, 'autre', label=l)
    text(ax, cx, 19, f'coefficient de ${n}$', 'sujet', 's')
    arrow(ax, (cx - 6, 25), (cx + 6.5, 25), 'sujet', curve=0.0)
    if i < 2: text(ax, cx + 14.5, 31.5, '+', 'varie', 'l')
text(ax, 44, 45, 'le nombre relié à sa lettre', 'fixe', 's')
save(fig, '15-030')
