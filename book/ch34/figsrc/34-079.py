import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 72, r'on veut $\cos 90° = 0$', 'encre', 'm')
def row(y, tag, sign, res, role):
    text(ax, 4, y + 12, tag, role, 's', ha='left')
    box(ax, 2, y - 7, 30, 14, 'sujet', True, label='cos 60° cos 30°\n≈ 0,433', size='s')
    text(ax, 37, y, sign, role, 'xl', weight='bold')
    box(ax, 42, y - 7, 30, 14, 'sujet', True, label='sin 60° sin 30°\n≈ 0,433', size='s')
    text(ax, 76, y, res, role, 'm', ha='left')
row(48, 'signe du sinus : faux', '+', '= 0,866', 'limite')
row(14, 'signe opposé : vrai', r'$-$', '= 0', 'resultat')
save(fig, '34-079')
