import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cx = [32 + 14 * i for i in range(4)]
box(ax, cx[1] - 7.5, 15, 15, 53, 'varie', fill=False, dash=True)
text(ax, 44, 72, 'chaque degré a sa colonne', 'varie', 's')
text(ax, 12, 62, 'dividende', 'sujet', 's')
for c, s, r in zip(cx, [r'$2x^3$', r'$0x^2$', r'$-4x$', r'$1$'], ['sujet', 'varie', 'sujet', 'sujet']):
    box(ax, c - 6.5, 57, 13, 10, r, label=s, size='s')
text(ax, 12, 42, r'$2x^2\times(x+6)$', 'fixe', 's')
box(ax, cx[0] - 6.5, 37, 13, 10, 'fixe', label=r'$2x^3$', size='s')
box(ax, cx[1] - 6.5, 37, 13, 10, 'fixe', label=r'$12x^2$', size='s')
text(ax, 12, 22, 'on soustrait', 'resultat', 's')
line(ax, [(cx[0] - 7, 29.5), (cx[3] + 7, 29.5)], 'fixe')
box(ax, cx[0] - 6.5, 17, 13, 10, 'resultat', label=r'$0$', size='s')
box(ax, cx[1] - 6.5, 17, 13, 10, 'resultat', label=r'$-12x^2$', size='s')
text(ax, 44, 8, r'$2x^3 \div x = 2x^2$', 'encre', 's')
arrow(ax, (cx[0], 56), (cx[0], 48.5), 'fixe', lw=0.6)
arrow(ax, (cx[1], 56), (cx[1], 48.5), 'varie', lw=0.6)
save(fig, '21-117')
