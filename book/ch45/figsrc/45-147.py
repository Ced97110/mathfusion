import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, bw, g = 4, 9, 1.5
xs = [x0 + i * (bw + g) for i in range(5)]
for i, x in enumerate(xs): box(ax, x, 24, bw, 11, 'sujet' if i < 2 else 'varie', label=r'$a$', size='l')
brace(ax, xs[0], xs[1] + bw, 37, 'sujet', label=r'$2a$', down=False)
brace(ax, xs[2], xs[4] + bw, 37, 'varie', label=r'$3a$', down=False)
brace(ax, xs[0], xs[4] + bw, 22, 'encre', label=r'$(2+3)a=5a$', size='m')
arrow(ax, (xs[4] + bw + 3, 29.5), (68, 29.5), 'encre')
box(ax, 70, 23, 14, 13, 'resultat', label='1', size='l')
text(ax, 77, 18, 'reste 1', 'resultat', 's')
text(ax, 77, 42, r'$a=1$', 'fixe', 's')
save(fig, '45-147')
