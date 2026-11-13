import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))
fig, ax = canvas(52)
text(ax, 14, 42, 'ℝ', 'sujet', 40, weight='bold')
text(ax, 54, 47, 'se lit « grand R »', 'sujet', 'm')
text(ax, 54, 39, 'nom du groupe de tous', 'encre', 's')
text(ax, 54, 34.5, 'les points de la droite', 'encre', 's')
f = numberline(ax, 6, 70, 20, -2, 4, labels=True, arrow_right=True)
for v, lab, above in [(-2, '', 0), (0.5, '1/2', 1), (3, '', 0), (3.14159, 'π', 1)]:
    dot(ax, f(v), 20, 'sujet', 0.8)
    if above: text(ax, f(v), 25, lab, 'sujet', 'm')
text(ax, 40, 6, 'chaque nombre de ℝ a son point', 'sujet', 's')
save(fig, '12-083')
