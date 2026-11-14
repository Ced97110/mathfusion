import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# un sac par case : n cases, n sacs de base
rows = [(r'$\mathbb{R}^2$' + '\n2 cases', ['(1, 0)', '(0, 1)'], 'dim = 2'),
        (r'$\mathbb{R}^3$' + '\n3 cases', ['(1, 0, 0)', '(0, 1, 0)', '(0, 0, 1)'], 'dim = 3'),
        (r'$\mathbb{R}^n$' + '\n$n$ cases', [r'$e_1$', '…', r'$e_n$'], r'dim = $n$')]
y = 48
for lab, sacs, dim in rows:
    text(ax, 11, y + 7, lab, 'sujet', 's')
    for i, s in enumerate(sacs):
        box(ax, 22 + i * 14.8, y + 1, 13.6, 12, 'sujet' if s != '…' else 'fixe', label=s, size='s', r=0.6, fill=(s != '…'))
    arrow(ax, (22 + (len(sacs) - 1) * 14.8 + 14.1, y + 7), (70, y + 7), 'fixe', lw=0.6)
    box(ax, 71, y + 2, 15, 10, 'resultat', label=dim, size='s', weight='bold')
    y -= 22
save(fig, '58-184')
