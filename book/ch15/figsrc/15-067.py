import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 58, r'$4x^{2}y^{5}$', 'encre', 'xl')
xs = [9.5 + 11.5 * i for i in range(7)]
for i, x in enumerate(xs):
    disc(ax, x, 42, 4.2, 'sujet' if i < 2 else 'autre', label=r'$x$' if i < 2 else r'$y$')
brace(ax, xs[0] - 4, xs[1] + 4, 36, 'sujet', label='2')
brace(ax, xs[2] - 4, xs[6] + 4, 36, 'autre', label='5')
box(ax, 14, 8, 60, 10, 'resultat', label=r'$2+5=7$ lettres : degré 7')
arrow(ax, (44, 26), (44, 18.5), 'resultat')
save(fig, '15-067')
