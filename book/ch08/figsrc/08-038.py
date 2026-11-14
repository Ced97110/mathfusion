import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 4, 56, 20, 12, 'sujet', label='0,6', size='l')
box(ax, 34, 56, 20, 12, 'sujet', label=r'$\frac{6}{10}$', size='l')
box(ax, 64, 56, 20, 12, 'resultat', label=r'$\frac{3}{5}$', size='l')
arrow(ax, (24, 62), (34, 62), 'varie'); arrow(ax, (54, 62), (64, 62), 'varie')
text(ax, 29, 72, 'dixièmes', 'varie', 's'); text(ax, 59, 72, r'$\div 2$ haut et bas', 'varie', 's')
x0, L = 8, 72
text(ax, 8, 42, '6 parts sur 10', 'sujet', 's', ha='left')
for i in range(10):
    ax.add_patch(Rectangle((x0 + L / 10 * i, 30), L / 10, 8, ec=COL['sujet'], fc=FILL['sujet'] if i < 6 else FILL['fixe'], lw=0.6, zorder=2))
text(ax, 8, 24, '3 parts sur 5', 'resultat', 's', ha='left')
for i in range(5):
    ax.add_patch(Rectangle((x0 + L / 5 * i, 12), L / 5, 8, ec=COL['resultat'], fc=FILL['resultat'] if i < 3 else FILL['fixe'], lw=0.6, zorder=2))
line(ax, [(x0 + .6 * L, 12), (x0 + .6 * L, 38)], 'fixe', dash=True)
save(fig, '08-038')
