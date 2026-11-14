import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 3, 83, 'départ', 'sujet', 's', ha='left')
box(ax, 24, 76, 62, 14, 'sujet', label=r'$\eta$ : transformation linéaire de $E$' + '\n' + r'$\eta^3=1$ ($x\mapsto x^2$ sur $\mathbb{F}_8$)', size='s')
arrow(ax, (55, 75.5), (55, 69.5), 'fixe')
text(ax, 3, 58, 'pas décisif', 'varie', 's', ha='left')
box(ax, 24, 48, 62, 20, 'varie', label=r'Dedekind : $1,\eta,\eta^2$ sans relation' + '\n' + 'plus courte, donc' + '\n' + r'polynôme minimal : $x^3-1$', size='s')
arrow(ax, (55, 47.5), (55, 41.5), 'fixe')
text(ax, 3, 33, 'arrivée', 'resultat', 's', ha='left')
box(ax, 24, 26, 62, 14, 'resultat', label=r'$z=\alpha+1$ : $z,\ \eta(z),\ \eta^2(z)$' + '\n' + 'forment une base', size='s')
for k, lab in enumerate([r'$\alpha+1$', r'$\alpha^2+1$', r'$\alpha^2+\alpha+1$']):
    box(ax, 6 + 27 * k, 6, 24, 10, 'resultat', label=lab, size='s')
text(ax, 44, 20.5, 'la base', 'resultat', 's')
save(fig, '67-134')
