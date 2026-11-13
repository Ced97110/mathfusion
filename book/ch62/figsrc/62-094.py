import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 2, 50, r'$(x+h)^2$', 'encre', 's', ha='left')
for x, w, lab, role in [(20, 12, r'$x^2$', 'fixe'), (34, 16, r'$2xh$', 'varie'), (52, 10, r'$h^2$', 'fixe')]:
    box(ax, x, 45, w, 10, role, label=lab, size='s')
box(ax, 68, 45, 18, 10, 'resultat', label=r'$2x$', size='s')
text(ax, 86, 58.5, 'coefficient de $h$', 'resultat', 's', ha='right')
text(ax, 2, 32, r'$(x+h)^3$', 'encre', 's', ha='left')
for x, w, lab, role in [(20, 10, r'$x^3$', 'fixe'), (32, 14, r'$3x^2h$', 'varie'), (48, 14, r'$3xh^2$', 'fixe'), (64, 8, r'$h^3$', 'fixe')]:
    box(ax, x, 27, w, 10, role, label=lab, size='s')
box(ax, 74, 27, 12, 10, 'resultat', label=r'$3x^2$', size='s')
text(ax, 2, 12, r'$(x+h)^k$', 'encre', 's', ha='left')
box(ax, 20, 7, 66, 10, 'fixe', dash=True, label=r'$k$ quelconque : pas montré', size='s')
save(fig, '62-094')
