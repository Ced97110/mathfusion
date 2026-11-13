import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
c = [3, 4, 5]
polys = [r'$1$', r'$x$', r'$x^2$']
xs = [18, 44, 70]
text(ax, 44, 65, r'polynômes de départ $(1,\,x,\,x^2,\ldots,x^n)$', 'sujet', 's')
for k, (x, pl) in enumerate(zip(xs, polys)):
    box(ax, x - 11, 36, 22, 12, 'sujet', label=pl, size='l')
    text(ax, x, 55, rf'$\times\,{c[k]}$', 'varie', 'm')
    text(ax, x, 30, rf'$c_{k}={c[k]}$', 'varie', 's')
text(ax, 31, 42, '+', 'encre', 'l')
text(ax, 57, 42, '+', 'encre', 'l')
brace(ax, 7, 81, 26, 'encre', depth=2.0)
arrow(ax, (44, 17), (44, 12), 'resultat')
box(ax, 14, 1, 60, 10, 'resultat', label=r'$3+4x+5x^2$', size='l')
save(fig, '58-144')
