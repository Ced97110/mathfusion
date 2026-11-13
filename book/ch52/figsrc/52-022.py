import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
CL = {0: 'sujet', 1: 'varie', 2: 'resultat', 3: 'limite'}
fig, ax = canvas(66)
cx = [12, 34, 56, 78]
for i in range(4):
    box(ax, cx[i] - 8.5, 6, 17, 10, CL[i], label=r'$\bar{%d}$' % i, size='l')
tops = [(12, 8), (4, 16), (5, 34), (-1, 72), (7, 84)]
for n, x in tops:
    r = n % 4
    line(ax, [(x, 55), (cx[r] + (x - cx[r]) * 0.15, 16.5)], 'fixe', lw=1.0)
for n, x in tops:
    disc(ax, x, 58, 3.2, CL[n % 4], label=str(n).replace('-', '−'), size='s')
text(ax, 48, 36, 'le trait gris :\nle reste par 4', 'fixe', 's')
save(fig, '52-022')
