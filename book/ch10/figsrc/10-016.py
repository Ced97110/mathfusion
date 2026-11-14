import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def row(y, a, b, r, role):
    box(ax, 4, y, 16, 10, role, label=a); text(ax, 25, y + 5, r'$\times$', 'encre', 'm')
    box(ax, 30, y, 16, 10, role, label=b); text(ax, 51, y + 5, '=', 'encre', 'm')
    box(ax, 56, y, 20, 10, role, label=r)
text(ax, 4, 62, 'calcul exact', 'sujet', 'm', ha='left')
row(46, '28', '31', '868', 'sujet')
row(16, '30', '30', '900', 'autre')
text(ax, 4, 8, 'estimation : mêmes calculs', 'autre', 'm', ha='left')
for xc in (12, 38): arrow(ax, (xc, 45), (xc, 27), 'varie')
arrow(ax, (66, 45), (66, 27), 'fixe')
text(ax, 72, 36, '+ 32', 'fixe', 's', ha='left')
save(fig, '10-016')
