import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
PT = 16
adv = 0.636 * PT * 25.4 / 72
fig, ax = canvas(56)
xc = 42
X, Y = '10101', '11010'
text(ax, xc, 44, X, 'sujet', PT)
text(ax, xc, 22, Y, 'autre', PT)
text(ax, 24, 44, r'$x$', 'sujet', 'l')
text(ax, 24, 22, r'$y$', 'autre', 'l')
for i in range(5):
    cx = xc + (i - 2) * adv
    if X[i] != Y[i]:
        arrow(ax, (cx, 39.5), (cx, 27), 'varie', both=True)
    else:
        line(ax, [(cx, 39.5), (cx, 27)], 'fixe', dash=True)
text(ax, 71, 33, r'$d(x,y)=4$', 'resultat', 'l')
text(ax, 44, 10, '4 positions qui diffèrent', 'varie', 's')
save(fig, '68-069')
