import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
w, g, x0 = 15.0, 2.0, 18.0
xs = [x0 + i * (w + g) for i in range(4)]
vals = [r'$-109$', r'$72$', r'$-11$', r'$9/4$']
for i in range(4):
    box(ax, xs[i], 32, w, 14, 'sujet', label=rf'$f_{i}$' + '\n' + vals[i], size='m')
    box(ax, xs[i], 16, w, 9, 'sujet', label='+', size='l')
text(ax, 9, 39, r'$x=-5$' + '\n' + r'$V=3$', 'encre', 'm')
text(ax, 9, 20.5, r'$x=5$' + '\n' + r'$V=0$', 'encre', 'm')
box(ax, 8, 2, 72, 9, 'resultat', label=r'$\mu=5$ : $3-0=3$ racines en tout', size='m')
save(fig, '69-106')
