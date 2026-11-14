import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, 'Huit éléments des quaternions', 'sujet', 's')
labs = ['1', '−1', 'i', '−i', 'j', '−j', 'k', '−k']
xs = [8 + i * 10.3 for i in range(8)]
for i, (x, l) in enumerate(zip(xs, labs)):
    if i < 2:
        disc(ax, x, 62, 4.3, 'fixe', label=l, size='s')
    else:
        disc(ax, x, 62, 4.3, 'sujet', label=(r'$' + l.replace('−', '-') + r'$'), size='s')
brace(ax, xs[0] - 4.3, xs[1] + 4.3, 56.5, 'fixe', label=r'carré $=1$')
brace(ax, xs[2] - 4.3, xs[7] + 4.3, 56.5, 'sujet', label=r'carré $=-1$')
box(ax, 4, 38, 80, 11, 'limite', label='aucun n’engendre les huit', size='m')
box(ax, 4, 22, 80, 11, 'limite', label=r'$x^2+1$ : 6 racines ($>2$)', size='m')
text(ax, 44, 45, r'±i, ±j, ±k sont racines de $x^2+1$', 'limite', 's') if False else None
save(fig, '54-268')
