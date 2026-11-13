import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
w0, x0 = 15, 6.5
heads = ['centaines', 'dizaines', 'unités', 'dixièmes', 'centièmes']
vals = ['100', '10', '1', r'$\frac{1}{10}$', r'$\frac{1}{100}$']
digs = [None, None, '2', '3', '5']
roles = ['fixe', 'fixe', 'sujet', 'varie', 'resultat']
for i in range(5):
    x = x0 + w0 * i
    text(ax, x + w0 / 2, 50, heads[i], roles[i], 's')
    box(ax, x, 28, w0, 16, roles[i], fill=digs[i] is not None, label=digs[i], size='xl', dash=digs[i] is None)
    text(ax, x + w0 / 2, 19, vals[i], roles[i], 's')
fx = x0 + 3 * w0
line(ax, [(fx, 26), (fx, 46)], 'encre', dash=True, lw=0.7)
disc(ax, fx, 30, 1.0, 'encre')
save(fig, '08-009')
