import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
c = 14; x0 = 16; g = 5
xs = [x0, x0 + c, x0 + 2*c + g, x0 + 3*c + g]
names = [r"$x_1$", r"$x_1'$", r"$x_2$", r"$x_2'$"]
bas = [r'$e_1$', r'$f_1$', r'$e_2$', r'$f_2$']
vals = [3, 2, 5, 2]
for k in range(4):
    r = 'sujet' if k < 2 else 'autre'
    text(ax, xs[k] + c/2, 44, names[k], r, 'm')
    box(ax, xs[k], 22, c, c, r, label=str(vals[k]), size='l', r=0.6)
    arrow(ax, (xs[k] + c/2, 21), (xs[k] + c/2, 12), 'fixe', lw=0.9)
    text(ax, xs[k] + c/2, 8, bas[k], r, 'm')
text(ax, 7, 29, r'$x$', 'encre', 'l')
text(ax, 7, 8, 'base', 'fixe', 's')
save(fig, '75-038')
