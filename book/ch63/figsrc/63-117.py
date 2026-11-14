import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 31, 50, 26, 11, 'sujet', label=r'$E$', size='m')
mids = [(16, r'$\mathbb{Q}(\sqrt{2})$'), (44, r'$\mathbb{Q}(\sqrt{6})$'), (72, r'$\mathbb{Q}(\sqrt{3})$')]
for cx, l in mids:
    box(ax, cx - 12, 28, 24, 11, 'fixe', label=l, size='s')
    line(ax, [(cx, 39), (44, 50)], 'fixe')
    line(ax, [(cx, 28), (44, 17)], 'fixe')
box(ax, 34, 6, 20, 11, 'fixe', label=r'$\mathbb{Q}$', size='s')
text(ax, 16, 76, r'$\gamma=\sqrt{2}$', 'varie', 's')
text(ax, 70, 76, r'$\gamma=\sqrt{2}+\sqrt{3}$', 'resultat', 's')
arrow(ax, (16, 72), (16, 40), 'varie')
arrow(ax, (66, 72), (55, 62), 'resultat')
text(ax, 8, 47, 'seulement', 'varie', 's', ha='left')
text(ax, 62, 66, 'tout $E$', 'resultat', 's', ha='left')
save(fig, '63-117')
