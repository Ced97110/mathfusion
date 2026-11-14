import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 52, 63, r'$\sqrt{2}$', 'sujet', 'l')
text(ax, 74, 63, r'$-\sqrt{2}$', 'autre', 'l')
text(ax, 2, 49, r'$x+x^2=x+2$', 'encre', 'm', ha='left')
text(ax, 2, 41, 'phrase de calcul', 'fixe', 's', ha='left')
text(ax, 2, 24, r'$x>0$', 'encre', 'm', ha='left')
text(ax, 2, 16, 'phrase d’ordre', 'fixe', 's', ha='left')
for j, role in enumerate(['resultat', 'resultat']):
    box(ax, 42 + 22 * j, 38, 20, 14, role, label='vrai')
box(ax, 42, 14, 20, 14, 'resultat', label='vrai')
box(ax, 64, 14, 20, 14, 'limite', label='faux')
save(fig, '63-004')
