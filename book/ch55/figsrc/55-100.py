import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
q = 10.0
y0 = 22
text(ax, 44, 66, r'plus haut : $x_1^2$ , exposants $(2,\,0)$', 'sujet', 'm')
# k1 = 2 : deux carrés ; k2 = 0 : rien
x1, x2 = 6, 36
for i in range(2):
    ax.add_patch(Rectangle((x1, y0 + i * q), q, q, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
line(ax, [(x2 - 2, y0), (x2 + q + 2, y0)], 'sujet', dash=True)
line(ax, [(2, y0), (50, y0)], 'fixe', lw=0.6)
text(ax, x1 + q / 2, y0 + 2 * q + 4, r'$k_1=2$', 'sujet', 'm')
text(ax, x2 + q / 2, y0 + 4, r'$k_2=0$', 'sujet', 'm')
arrow(ax, (27, y0), (27, y0 + 2 * q), 'varie', both=True)
text(ax, 30, y0 + q, r'$d_1$', 'varie', 'm', ha='left')
text(ax, 54, 48, r'$d_1=2-0=2$', 'varie', 'm', ha='left')
text(ax, 54, 40, r'$d_2=k_2=0$', 'fixe', 'm', ha='left')
arrow(ax, (70, 35), (70, 28), 'varie')
box(ax, 52, 15, 34, 12, 'resultat', label=r'on retire $e_1^2\,e_2^0$', size='m')
text(ax, 69, 8, r'reste : $-2x_1x_2$', 'varie', 'm')
save(fig, '55-100')
