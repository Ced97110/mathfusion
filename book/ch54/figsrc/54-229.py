import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
heads = [r'$x^2$', r'$x$', r'$1$']
top = ['2', '5', '7']
bot = ['2', '2', '1']
x0, w = 22.0, 20.0
text(ax, 10, 64, r'$f$', 'fixe', 'l')
text(ax, 10, 36, r'$\bar{f}$', 'sujet', 'l')
text(ax, 11, 50, 'modulo 3', 'varie', 's')
for i in range(3):
    cx = x0 + i * w
    text(ax, cx + 8.5, 79, heads[i], 'fixe', 's')
    box(ax, cx, 59, 17, 10, 'fixe', label=top[i], size='m')
    box(ax, cx, 31, 17, 10, 'sujet', label=bot[i], size='m')
    arrow(ax, (cx + 8.5, 58), (cx + 8.5, 42), 'varie')
text(ax, 44, 18, r'$\bar{f}=2x^2+2x+1$', 'sujet', 'l')
text(ax, 44, 8, 'chaque coefficient : reste modulo 3', 'fixe', 's')
save(fig, '54-229')
