import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
parts = [(4, 22, 'sujet', r'$D$', 'tout l’anneau'), (33, 22, 'varie', r'$\setminus$', 'privé de'),
         (62, 22, 'fixe', r'$\{0\}$', 'le seul élément 0')]
for x, w, role, sym, mean in parts:
    box(ax, x, 44, w, 13, role, label=sym, size='xl')
    arrow(ax, (x + w / 2, 44), (x + w / 2, 37), role)
    text(ax, x + w / 2, 33, mean, role, 's')
y = 14
text(ax, 4, y + 9, r'dans $\mathbb{Z}$ :', 'fixe', 's', ha='left')
for i, v in enumerate(range(-2, 3)):
    x = 22 + i * 12
    if v == 0:
        disc(ax, x, y, 3.6, 'fixe', fill=False, label='0')
    else:
        disc(ax, x, y, 3.6, 'sujet', label=f'{v}'.replace('-', '−'))
text(ax, 84, y, r'$=D^*$', 'resultat', 's', ha='right')
save(fig, '56-135')
