import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 16, 60, r'$x$', 'sujet', 'l', weight='bold'); text(ax, 42, 60, r'$\bar y$', 'autre', 'l', weight='bold')
text(ax, 70, 60, 'produit', 'varie', 'm')
for k, (a, b) in enumerate([('1', '1'), ('$i$', r'$-i$')]):
    y = 42 - k * 15
    box(ax, 6, y, 20, 11, 'sujet', label=a)
    text(ax, 32, y + 5.5, r'$\times$', 'fixe', 'm')
    box(ax, 36, y, 20, 11, 'autre', label=b)
    arrow(ax, (58, y + 5.5), (63, y + 5.5), 'fixe')
    box(ax, 64, y, 18, 11, 'varie', label='1', weight='bold')
text(ax, 20, 21, r'$\Sigma$', 'fixe', 'l')
box(ax, 36, 4, 46, 11, 'resultat', label=r'$1+1=2$', size='l', weight='bold')
arrow(ax, (73, 26.5), (73, 15.5), 'fixe')
save(fig, '75-147')
