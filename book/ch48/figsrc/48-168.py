import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 14, 94, r'$\mathbb{Z}/7\mathbb{Z}$', 'sujet', 'm')
text(ax, 72, 94, r'$\mathbb{Z}/12\mathbb{Z}$', 'resultat', 'm')
tgt = (68, 84)
for i in range(7):
    y = 82 - i * 10
    disc(ax, 14, y, 3.2, 'sujet', label=str(i), size='s')
    arrow(ax, (17.5, y + (0.3 if i else 0)), (68.9, 84), 'varie', lw=0.8)
for i in range(12):
    y = 84 - i * 6
    if i == 0: disc(ax, 72, y, 3.2, 'resultat', label='0', size='s')
    else: disc(ax, 72, y, 2.2, 'fixe', fill=False, lw=0.6)
text(ax, 72, 8, 'rien d’autre que 0', 'resultat', 's')
save(fig, '48-168')
