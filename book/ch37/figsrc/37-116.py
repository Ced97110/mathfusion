import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 62, 52, r'$\Delta \div$ reste', 'varie', 's')
rows = [('c = 60', 15, 66.14, 'c', 'varie'), ('b = 50', 25, 39.69, 'b', 'sujet'), ('a = 40', 35, 28.35, 'a', 'sujet')]
k = 0.7
for i, (side, rest, r, n, role) in enumerate(rows):
    y = 38 - i * 14
    text(ax, 3, y + 4.5, side.replace('=', ' = '), 'fixe', 's', ha='left')
    text(ax, 26, y + 4.5, rf'$s-{n}={rest}$', 'fixe', 's', ha='left')
    box(ax, 44, y, r * k * 0.9, 9, role, label=rf'$r_{n}$ = ' + f'{r:.2f}'.replace('.', ','), size='s')
text(ax, 44, 3, 'plus grand côté → plus petit reste → plus grand rayon', 'varie', 's')
save(fig, '37-116')
