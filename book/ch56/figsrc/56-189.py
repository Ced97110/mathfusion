import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
rows = [(52, r'$6=$', ['2', '3'], [r'$-1$', r'$-1$'], r'$\mathbb{Z}$ : unités $1$ et $-1$'),
        (22, r'$5=$', [r'$2+i$', r'$2-i$'], [r'$i$', r'$-i$'], r'$\mathbb{Z}[i]$ : $1$, $-1$, $i$, $-i$')]
for y, lead, fac, uni, cap in rows:
    text(ax, 8, y + 5, lead, 'encre', 'l')
    for k, s in enumerate(fac):
        box(ax, 15 + k * 21, y, 18, 10, 'sujet', label=s)
    for k, s in enumerate(uni):
        box(ax, 57 + k * 15, y, 13, 10, 'fixe', label=s)
    brace(ax, 57, 85, y - 1, 'fixe', label='unités', depth=1.6)
    text(ax, 44, y + 15, cap, 'fixe', 's')
save(fig, '56-189')
