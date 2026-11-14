import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
box(ax, 3, 3, 82, 68, 'fixe', dash=True)
text(ax, 44, 66, r'$\mathbb{R}^{*}$ : réels non nuls', 'fixe', 'm')
box(ax, 8, 22, 72, 36, 'sujet')
text(ax, 44, 53, r'$\mathbb{Q}^{*}$ : fractions non nulles', 'sujet', 'm')
text(ax, 22, 40, '3/4', 'sujet', 'l'); text(ax, 42, 40, '2/5', 'sujet', 'l'); text(ax, 66, 40, '3/10', 'resultat', 'l')
text(ax, 32, 40, r'$\times$', 'varie', 'l')
text(ax, 52, 40, r'$=$', 'varie', 'l')
text(ax, 44, 28, r'le produit reste dans $\mathbb{Q}^{*}$', 'resultat', 's')
text(ax, 44, 12, 'des réels ne sont pas des fractions', 'fixe', 's')
save(fig, '46-037')
