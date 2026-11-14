import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cxs = (28, 52, 76)
text(ax, 44, 77, 'coefficient de chaque racine', 'fixe', 's')
for c, r in zip(cxs, (r'$y_1$', r'$y_2$', r'$y_3$')):
    box(ax, c - 10, 62, 20, 9, 'fixe', label=r, size='s')
text(ax, 7, 46.5, r'$z_1$', 'sujet', 'm')
text(ax, 7, 20.5, r'$\sigma(z_1)$', 'autre', 's')
top = (r'$1$', r'$w$', r'$w^2$')
bot = (r'$w^2$', r'$1$', r'$w$')
for c, a, b in zip(cxs, top, bot):
    box(ax, c - 10, 42, 20, 9, 'sujet', label=a, size='s')
    arrow(ax, (c, 42), (c, 30), 'varie')
    box(ax, c - 10, 16, 20, 9, 'autre', label=b, size='s')
text(ax, cxs[1] + 2, 35, r'$\times w^2$', 'varie', 's', ha='left')
box(ax, 6, 3, 76, 9, 'resultat', label=r'$\sigma(z_1)=w^2z_1$', size='m')
save(fig, '65-115')
