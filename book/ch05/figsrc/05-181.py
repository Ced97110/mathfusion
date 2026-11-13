import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
D = 8
box(ax, 2, 68+D, 38, 12, 'autre', label='grands premiers\n(théorème d’Euclide)', size='s')
box(ax, 48, 68+D, 38, 12, 'sujet', label=r'$a\times u+b\times v=1$', size='m')
text(ax, 67, 63+D, r'$u$ et $v$ entiers', 'sujet', 's')
box(ax, 22, 46+D, 44, 10, 'resultat', label='clé de chiffrement', size='m', weight='bold')
text(ax, 44, 42+D, 'les deux outils la fabriquent', 'resultat', 's')
arrow(ax, (21, 67.7+D), (34, 56.3+D), 'varie')
arrow(ax, (67, 67.7+D), (54, 56.3+D), 'varie')
text(ax, 44, 35+D, r'exemple : $a=3$, $b=7$', 'fixe', 's')
yl = 20+D
f = numberline(ax, 8, 77, yl, 0, 15, 1, labels=False)
for k in range(5):
    arrow(ax, (f(3 * k), yl + 2.4), (f(3 * k + 3), yl + 2.4), 'varie', curve=-0.6)
arrow(ax, (f(15), yl - 2.4), (f(8), yl - 2.4), 'autre', curve=-0.6)
arrow(ax, (f(8), yl - 2.4), (f(1), yl - 2.4), 'autre', curve=-0.6)
ax.add_patch(Circle((f(0), yl), 2.2, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, zorder=4.6)); text(ax, f(0), yl, '0', 'fixe', 's')
ax.add_patch(Circle((f(15), yl), 2.2, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=4.6)); text(ax, f(15), yl, '15', 'varie', 's')
ax.add_patch(Circle((f(1), yl), 2.2, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=4.6)); text(ax, f(1), yl, '1', 'resultat', 's')
text(ax, f(7.5), yl + 10, r'$3\times5=15$', 'varie', 's')
text(ax, f(8), yl - 11, r'$7\times(-2)=-14$', 'autre', 's')
text(ax, 44, 4, r'$3\times5+7\times(-2)=1$', 'resultat', 'm', weight='bold')
save(fig, '05-181')
