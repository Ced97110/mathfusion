import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
k = 4.5
x0 = 20
H = 6
def seg(x, n, y, role, dash=False):
    box(ax, x, y, n * k, H, role, r=0.01, lw=0.7, dash=dash, fill=not dash)
assert (8 + 3) + 1 == 8 + (3 + 1) == 12 and (8 - 3) - 1 == 4 and 8 - (3 - 1) == 6
text(ax, 2, 72, 'addition', 'resultat', 'm', ha='left', weight='bold')
text(ax, 2, 36, 'soustraction', 'limite', 'm', ha='left', weight='bold')
text(ax, x0, 72, '8', 'sujet', 's', ha='left'); text(ax, x0 + 8 * k + 1, 72, '3', 'autre', 's', ha='left'); text(ax, x0 + 11 * k + 1, 72, '1', 'varie', 's', ha='left')
# lignes : regroupement en tête de ligne
y = 60
for lab, grp in (('(8+3)+1', (0, 11)), ('8+(3+1)', (8, 12))):
    text(ax, 2, y + 3, lab, 'encre', 's', ha='left')
    seg(x0, 8, y, 'sujet'); seg(x0 + 8 * k, 3, y, 'autre'); seg(x0 + 11 * k, 1, y, 'varie')
    brace(ax, x0 + grp[0] * k, x0 + grp[1] * k, y - 0.5, 'fixe', None, down=True, depth=1.4)
    text(ax, 80, y + 3, '= 12', 'resultat', 's', ha='left')
    y -= 12
y = 24
text(ax, 2, y + 3, '(8−3)−1', 'encre', 's', ha='left')
seg(x0, 4, y, 'sujet'); seg(x0 + 4 * k, 3, y, 'autre', True); seg(x0 + 7 * k, 1, y, 'varie', True)
text(ax, 80, y + 3, '= 4', 'limite', 's', ha='left')
y = 12
text(ax, 2, y + 3, '8−(3−1)', 'encre', 's', ha='left')
seg(x0, 6, y, 'sujet'); seg(x0 + 6 * k, 2, y, 'autre', True)
text(ax, 80, y + 3, '= 6', 'limite', 's', ha='left')
save(fig, '41-061')
