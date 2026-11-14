import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 72, r'$\mathbb{F}_p$', 'sujet', 26)
text(ax, 14, 72, 'un corps', 'sujet', 's')
arrow(ax, (24, 72), (34, 72), 'sujet')
text(ax, 72, 72, 'p éléments', 'varie', 's')
arrow(ax, (63, 72), (54, 70), 'varie')
text(ax, 44, 59,r'$p$ termes égaux à 1 donnent 0', 'encre', 's')
for k, (p, labs) in enumerate([(2, ['0', '1']), (3, ['0', '1', r'$1+1$'])]):
    y = 40 - 24 * k
    text(ax, 14, y + 6, r'$\mathbb{F}_%d$' % p, 'sujet', 'l')
    for i, l in enumerate(labs):
        box(ax, 30 + 13 * i, y, 11, 12, 'sujet', label=l, size='s')
    text(ax, 77, y + 6, '%d éléments' % p, 'varie', 's')
save(fig, '67-025')
