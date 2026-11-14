import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

Ds = [-2, 2, -2]
fig, ax = canvas(66)
bw = 20.0
xs = [8 + k * 27 for k in range(3)]
for x, d in zip(xs, Ds):
    sq = d * d
    assert sq == 4
    box(ax, x, 40, bw, 14, 'varie', label=('D = %d' % d) if d > 0 else 'D = −%d' % -d, size='m')
    arrow(ax, (x + bw / 2, 40), (44 + (x + bw / 2 - 44) * 0.25, 27), 'fixe', lw=0.9)
text(ax, 44, 59, 'trois états des racines', 'fixe', 's')
text(ax, 44, 33, 'on élève au carré', 'fixe', 's')
box(ax, 28, 10, 32, 14, 'resultat', label=r'$D^2=4$', size='l', weight='bold')
text(ax, 44, 4, r'toujours 4 : $D^2\in F$', 'resultat', 's')
save(fig, '65-040')
