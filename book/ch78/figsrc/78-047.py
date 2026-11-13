import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
prods = ['xyz', 'yxz', 'zxy', 'zyx', 'yzx', 'xzy']
text(ax, 44, 41, 'Les 12 produits des trois termes', 'sujet', 'm')
for k, p in enumerate(prods):
    x = 3 + k * 14.2
    box(ax, x, 22, 13, 9, 'resultat', label=r'$+%s$' % p, size='s', r=0.5)
    box(ax, x, 6, 13, 9, 'limite', label=r'$-%s$' % p, size='s', r=0.5)
    line(ax, [(x + 6.5, 15), (x + 6.5, 22)], 'fixe')
save(fig, '78-047')
