import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 52, 58, 10, 'sujet', label=r'$a=b$ : 2 $\times$ 3 = 6'); box(ax, 66, 52, 20, 10, 'fixe', label=r'$c\neq 0$')
text(ax, 41, 44, r'$a\times c=b\times c$', 'varie', 's'); text(ax, 71, 44, r'$a/c=b/c$', 'varie', 's')
rows = (('2', ('12 = 12', '3 = 3')), ('-3', ('-18 = -18', '-2 = -2')))
for i, (c, cells) in enumerate(rows):
    y = 26 - 20 * i
    box(ax, 2, y, 22, 10, 'varie', label=r'$c=%s$' % c)
    for x, t in zip((28, 58), cells):
        box(ax, x, y, 26, 10, 'resultat', label=r'$%s$' % t.replace(' = ', '=') if False else t.replace('-', '−'))
save(fig, '16-052')
