import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 14, 43, 26, 12, 'sujet', label=r'$2^{n}$', size='xl')
text(ax, 65, 49, 'n = nombre de facteurs', 'varie', 's')
cx = [12, 33, 55, 75]; vals = ['2', '4', '8', '16']
for i, x in enumerate(cx):
    n = i + 1
    arrow(ax, (27 + (x - 27) * 0.3, 43), (x, 38), 'fixe')
    text(ax, x, 33.5, f'n = {n}', 'varie', 's')
    for j in range(n): box(ax, x - n * 2.1 + j * 4.2, 22, 3.6, 5.5, 'sujet', r=0.3)
    text(ax, x, 15, vals[i], 'resultat', 'l', weight='bold')
text(ax, 44, 6, 'chaque facteur de plus : × 2', 'varie', 's')
save(fig, '14-007')
