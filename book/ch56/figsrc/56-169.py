import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'on part d’un ensemble\net on ajoute un élément', 'encre', 'm')
rows = [(40, r'$\mathbb{Z}$', r'$+\,x$', r'$\mathbb{Z}[x]$', 'fixe'),
        (24, r'$\mathbb{Z}$', r'$+\,i$', r'$\mathbb{Z}[i]$', 'fixe'),
        (6, r'rng $R$', '+ neutre $1$', 'anneau, neutre\n' + r'$(1,0)$', 'sujet')]
for y, a, mid, b, role in rows:
    h = 12 if role == 'sujet' else 10
    box(ax, 2, y, 24, h, role, label=a, size='s')
    arrow(ax, (27, y + h / 2), (51, y + h / 2), 'varie')
    text(ax, 39, y + h / 2 + 3.2, mid, 'varie', 's')
    box(ax, 52, y, 34, h, role if role != 'fixe' else 'fixe', label=b, size='s')
save(fig, '56-169')
