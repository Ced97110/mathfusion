import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 59, r'$M=\{0\}$', 'sujet', 'm')
box(ax, 8, 28, 28, 26, 'sujet', dash=True)
disc(ax, 22, 41, 4.0, 'sujet', label='0', size='m')
box(ax, 44, 38, 12, 8, 'varie', label='a', size='m')
arrow(ax, (44, 42), (27, 42.5), 'varie', lw=1.2)
text(ax, 66, 42, r'$a\cdot 0=0$', 'resultat', 'm')
text(ax, 50, 52, 'tout coefficient a', 'varie', 's')
for i in range(4):
    y = 22 - i * 5.2
    text(ax, 48, y, f'règle {i + 1} :  0 = 0', 'resultat', 's')
text(ax, 22, 22, 'un seul élément', 'sujet', 's')
text(ax, 22, 17, 'convient à tout R', 'sujet', 's')
save(fig, '57-203')
