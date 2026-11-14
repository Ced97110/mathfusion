import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 44, 45, r'$[[x,y],z]+[[y,z],x]+[[z,x],y]$', 'sujet', 'm')
words = ['xyz', 'yxz', 'zxy', 'zyx', 'yzx', 'xzy']
for i, w in enumerate(words):
    x = 2.5 + i * 14
    box(ax, x, 18, 13, 10, 'resultat', label=f'$+{w}$', size='s')
    box(ax, x, 4, 13, 10, 'limite', label=f'$-{w}$', size='s')
    line(ax, [(x + 6.5, 14), (x + 6.5, 18)], 'fixe')
text(ax, 44, 36, '3 doubles crochets : 12 produits', 'fixe', 's')
text(ax, 44, 32, 'chaque produit : + puis −', 'fixe', 's')
save(fig, '78-055')
