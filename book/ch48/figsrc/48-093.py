import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
pairs = [('0', '6', r'$K$'), ('2', '8', r'$2K$'), ('4', '10', r'$4K$')]
for i, (a, b, n) in enumerate(pairs):
    x = 4 + i * 28; role = 'sujet' if i == 0 else 'autre'
    box(ax, x, 22, 24, 12, role)
    disc(ax, x + 6.5, 28, 4, role, label=a, size='s')
    disc(ax, x + 17.5, 28, 4, role, label=b, size='s')
    text(ax, x + 12, 17, n, role, 's')
brace(ax, 4, 80, 38, 'fixe', r'$H$ : 6 éléments', down=False)
brace(ax, 4, 80, 12, 'autre', r'$H/K$ : 3 paquets', down=True)
text(ax, 44, 52, r'$K=\{0,\ 6\}$', 'sujet', 's') if False else None
save(fig, '48-093')
