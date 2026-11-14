import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
box(ax, 6, 66, 76, 13, 'sujet', label=r'$x=\frac{1}{2}t_1\pm\frac{1}{2}\sqrt{t_1^2-4t_2}$', size='m')
for cx in (22, 66):
    arrow(ax, (cx, 66), (cx, 59.5), 'varie')
    arrow(ax, (cx, 48), (cx, 41.5), 'varie')
    arrow(ax, (cx, 28), (cx, 20.5), 'varie')
box(ax, 3, 48, 38, 11, 'varie', label=r'$t_1=5,\ t_2=6$', size='s')
box(ax, 47, 48, 38, 11, 'varie', label=r'$t_1=0,\ t_2=-2$', size='s')
box(ax, 3, 28, 38, 13, 'fixe', label=r'$2{,}5\pm\frac{1}{2}\sqrt{25-24}$', size='s')
box(ax, 47, 28, 38, 13, 'fixe', label=r'$0\pm\frac{1}{2}\sqrt{0+8}$', size='s')
box(ax, 3, 8, 38, 12, 'resultat', label=r'$3$ et $2$', size='m')
box(ax, 47, 8, 38, 12, 'resultat', label=r'$\pm\sqrt{2}$', size='m')
save(fig, '65-099')
