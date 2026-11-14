import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$f=3x^2+x$, $g=2x-1$', 'sujet', 'm')
xs = [2, 33, 64]; w, y0, h = 22, 36, 11
labs = [r'$3x^2+x$', r'$6x^2+2x$', r'$5x$']
roles = ['sujet', 'fixe', 'resultat']
for x, l, r in zip(xs, labs, roles):
    box(ax, x, y0, w, h, r, label=l, size='s')
arrow(ax, (xs[0] + w, y0 + h / 2), (xs[1], y0 + h / 2), 'varie')
text(ax, (xs[0] + w + xs[1]) / 2, y0 + h + 3, r'$\times2$', 'varie', 's')
arrow(ax, (xs[1] + w, y0 + h / 2), (xs[2], y0 + h / 2), 'varie', lw=1.8)
text(ax, (xs[1] + w + xs[2]) / 2, y0 + h + 3, r'$-3x\,g$', 'varie', 's')
for x, d in zip(xs, ['degré 2', 'degré 2', 'degré 1']):
    text(ax, x + w / 2, y0 - 5, d, 'sujet' if d.endswith('1') is False else 'resultat', 's')
text(ax, 44, 17, r'$3x\,g=6x^2-3x$ : le terme en $x^2$ disparaît', 'varie', 's')
text(ax, 44, 8, 'on recommence sur le résultat', 'fixe', 's')
save(fig, '54-156')
