import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$f_5=x(x-1)(x+1)(x+2)(x^2+2)$', 'encre', 'm')
xs = [10, 22, 34, 46, 64, 76]
for i, x in enumerate(xs):
    disc(ax, x, 40, 3.6, 'fixe' if i < 4 else 'varie')
for x, s in zip(xs[:4], [r'$x$', r'$x-1$', r'$x+1$', r'$x+2$']):
    text(ax, x, 32, s, 'fixe', 's')
text(ax, 70, 32, r'$x^2+2$', 'varie', 's')
arrow(ax, (65, 44), (75, 44), 'varie', both=True, curve=-0.6)
brace(ax, 6.5, 49.5, 27, 'fixe', label='4 points fixes')
brace(ax, 60.5, 79.5, 27, 'varie', label='un échange')
save(fig, '67-212')
