import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, '4', 'encre', 'xl', weight='bold')
text(ax, 54, 55, '?', 'limite', 'xl', weight='bold')
text(ax, 44, 46, 'combien de morceaux ?', 'fixe', 's')
cm = 4.0; po = 4.0 * 2.54
for k in range(4):
    box(ax, 8 + k * cm, 30, cm, 6, 'autre', r=0.3, lw=0.6)
text(ax, 8 + 4 * cm + 3, 33, '4 cm', 'autre', 'm', ha='left')
for k in range(4):
    box(ax, 8 + k * po, 14, po, 8, 'sujet', r=0.3, lw=0.6)
text(ax, 8 + 4 * po + 3, 18, '4 po', 'sujet', 'm', ha='left')
text(ax, 44, 5, 'le nom dit la taille du morceau', 'resultat', 's')
save(fig, '11-003')
