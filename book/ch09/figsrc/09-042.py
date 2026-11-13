import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def group(cx, y):
    box(ax, cx - 7, y, 14, 17, 'fixe', fill=False, dash=True, r=0.5)
    ax.add_patch(Rectangle((cx - 2.5, y + 11), 5, 4, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    for j in range(3):
        disc(ax, cx - 4 + j * 4, y + 5, 1.6, 'autre')
text(ax, 44, 83, '4 téléviseurs pour 12 personnes', 'encre', 's', weight='bold')
for i in range(4):
    group(11 + i * 22, 58)
arrow(ax, (44, 55), (44, 42), 'varie')
text(ax, 50, 48.5, r'$\div 4$', 'varie', 'm', ha='left')
text(ax, 44, 36, '1 téléviseur pour 3 personnes', 'resultat', 's', weight='bold')
group(44, 15)
ax.add_patch(Rectangle((60, 24), 5, 4, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
text(ax, 67, 26, 'téléviseur', 'sujet', 's', ha='left')
disc(ax, 62.5, 16, 1.6, 'autre')
text(ax, 67, 16, 'personne', 'autre', 's', ha='left')
save(fig, '09-042')
