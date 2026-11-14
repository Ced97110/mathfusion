import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))
fig, ax = canvas(74)
f = numberline(ax, 6, 70, 52, -2, 4, labels=True)
for v, lab, role in [(-2, '', 'sujet'), (0.5, '1/2', 'sujet'), (3, '', 'sujet'), (3.14159, 'π', 'autre')]:
    dot(ax, f(v), 52, role, 0.8)
    if lab: text(ax, f(v), 57, lab, role, 'm')
dot(ax, 10, 70, 'sujet', 1.3); text(ax, 14, 70, 'rationnel', 'sujet', 's', ha='left')
dot(ax, 40, 70, 'autre', 1.3); text(ax, 44, 70, 'irrationnel', 'autre', 's', ha='left')
text(ax, 38, 41, 'chaque point a une des deux couleurs', 'resultat', 's')
box(ax, 22, 12, 44, 20, 'limite', dash=True)
text(ax, 44, 26, '5/0', 'limite', 'l')
text(ax, 44, 17, 'pas un point de la droite', 'limite', 's')
save(fig, '12-084')
