import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for cx, f, role, v in [(22, r'$x^2 + y^2$', 'sujet', r'dim. 0 : $\nu = 0$'), (66, r'$x^2 - y^2$', 'autre', r'dim. 1 : $\nu = 1$')]:
    cy = 34
    line(ax, [(cx - 17, cy), (cx + 17, cy)], 'fixe', 0.6); line(ax, [(cx, cy - 17), (cx, cy + 17)], 'fixe', 0.6)
    text(ax, cx, 60, f, role, 'm'); text(ax, cx, 6, v, 'resultat', 'm')
disc(ax, 22, 34, 1.2, 'sujet'); text(ax, 22, 14, 'aucun vecteur nul', 'sujet', 's')
text(ax, 22, 21, '', 'sujet', 's')
line(ax, [(66 - 14, 34 - 14), (66 + 14, 34 + 14)], 'resultat', 1.6)
arrow(ax, (66, 34), (66 + 8, 34 + 8), 'resultat', 1.2)
text(ax, 80, 49, '(1, 1)', 'resultat', 's'); text(ax, 66, 14, 'une droite de valeur 0', 'resultat', 's')
text(ax, 44, 76, r'$\nu$ : plus grande dimension', 'sujet', 'm')
text(ax, 44, 70.5, r'd’un sous-espace où $Q$ vaut 0', 'sujet', 'm')
save(fig, '73-134')
