import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [6 + i*10.8 for i in range(8)]
names = ['1', r'$r^2$', r'$r$', r'$r^3$', r'$s$', r'$r^2s$', r'$rs$', r'$r^3s$']
for i, (x, l) in enumerate(zip(xs, names)):
    disc(ax, x, 26, 4.2, 'resultat' if i < 2 else 'fixe', label=l, size='s')
for k in range(3):
    a, b = 2 + 2*k, 3 + 2*k
    line(ax, [(xs[a], 31.5), (xs[b], 31.5)], 'fixe', lw=1.0)
box(ax, xs[0]-5.5, 19, xs[1]-xs[0]+11, 14, 'resultat', fill=False)
brace(ax, xs[0]-5, xs[1]+5, 17, 'resultat', label=r'$|C|=2$')
brace(ax, xs[2]-5, xs[7]+5, 17, 'fixe', label='3 paires : 6 (pair)')
text(ax, 44, 46, r'8 = 2 $\times$ 2 $\times$ 2', 'sujet', 'l')
text(ax, 44, 38, r'$|C|=8-6=2$ : multiple de 2', 'resultat', 's')
save(fig, '49-279')
