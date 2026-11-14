import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, L = 8, 72
text(ax, 8, 63, '0,7 = 7 dixièmes', 'sujet', 'm', ha='left')
for i in range(10):
    ax.add_patch(Rectangle((x0 + L / 10 * i, 46), L / 10, 10, ec=COL['sujet'], fc=FILL['sujet'] if i < 7 else FILL['fixe'], lw=0.6, zorder=2))
text(ax, 8, 36, '0,70 = 70 centièmes', 'autre', 'm', ha='left')
for i in range(100):
    ax.add_patch(Rectangle((x0 + L / 100 * i, 20), L / 100, 10, ec=COL['autre'], fc=FILL['autre'] if i < 70 else FILL['fixe'], lw=0.25, zorder=2))
xe = x0 + 0.7 * L
line(ax, [(xe, 20), (xe, 56)], 'resultat', dash=True)
text(ax, xe + 2, 41, 'même longueur', 'resultat', 's', ha='left')
text(ax, 44, 12, r'$\times 10$ parts, taille $\div 10$', 'varie', 's')
save(fig, '08-035')
