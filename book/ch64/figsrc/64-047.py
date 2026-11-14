import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 24, 50, r'$G$', 'sujet', 'xl', weight='bold')
text(ax, 44, 50, r'$\supset$', 'varie', 'xl', weight='bold')
text(ax, 64, 50, r'$H$', 'autre', 'xl', weight='bold')
for x, role, lab in [(24, 'sujet', 'groupe de gauche'), (44, 'varie', 'contient'), (64, 'autre', 'groupe de droite')]:
    arrow(ax, (x, 56 - 12), (x, 40 - 0), role)
    text(ax, x, 36, lab, role, 's')
text(ax, 44, 20, r'$24\supset12\supset4\supset1$', 'encre', 'l')
text(ax, 44, 12, 'toute la suite sur une ligne', 'fixe', 's')
text(ax, 44, 3.5, r'normale : $H$ normal dans $G$', 'resultat', 's')
save(fig, '64-047')
