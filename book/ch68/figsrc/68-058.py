import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)

def bits(ax, x, y, s, roles, cw, ch=7.0, size='l'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

a, b = '000', '111'
assert sum(p != q for p, q in zip(a, b)) == 3
cw = 10.0
text(ax, 44, 57, r'code $C = \{000,\ 111\}$', 'sujet', 'l', weight='bold')
bits(ax, 4, 34, a, ['varie'] * 3, cw)
bits(ax, 54, 34, b, ['varie'] * 3, cw)
arrow(ax, (36, 37.5), (52, 37.5), 'varie', both=True)
text(ax, 44, 44, 'une seule paire', 'fixe', 's')
brace(ax, 4, 84, 34, 'varie', label=r'$d = 3$ : les 3 positions diffèrent', size='m')
text(ax, 44, 8, 'plusieurs paires : on garde la plus petite', 'sujet', 'm', weight='bold')
save(fig, '68-058')
