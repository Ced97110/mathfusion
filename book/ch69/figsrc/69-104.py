import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
w, g = 19.0, 2.0
x0 = (88 - 4 * w - 3 * g) / 2
xs = [x0 + i * (w + g) for i in range(4)]
cx = [x + w / 2 for x in xs]
text(ax, 44, 74, r'coefficients de $x^3-3x+1$', 'encre', 'm')
top = [r'$1\,x^3$', r'$0\,x^2$', r'$-3\,x$', '1']
bot = ['1', r'$|0|=0$', r'$|-3|=3$', r'$|1|=1$']
for i in range(4):
    box(ax, xs[i], 56, w, 10, 'fixe' if i == 0 else 'sujet', label=top[i], size='m')
    box(ax, xs[i], 34, w, 10, 'fixe' if i == 0 else 'varie', label=bot[i], size='m')
    arrow(ax, (cx[i], 55.5), (cx[i], 44.5), 'fixe' if i == 0 else 'varie')
    arrow(ax, (cx[i], 33.5), (cx[i], 20.5), 'resultat')
box(ax, 3, 8, 82, 12, 'resultat', label=r'$\mu=1+0+3+1=5$', size='l')
save(fig, '69-104')
