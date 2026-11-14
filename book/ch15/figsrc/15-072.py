import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 72, r'$9x^{2}-50x-13$', 'encre', 'm'); text(ax, 66, 72, r'$4x^{3}+x^{2}$', 'encre', 'm')
for i, (lab, role) in enumerate([(r'$9x^{2}$', 'sujet'), (r'$-50x$', 'fixe'), (r'$-13$', 'fixe')]):
    box(ax, 2 + i * 14.5, 52, 13.5, 9, role, label=lab, size='s')
for i, (lab, role) in enumerate([(r'$4x^{3}$', 'limite'), (r'$x^{2}$', 'fixe')]):
    box(ax, 48 + i * 17, 52, 16, 9, role, label=lab, size='s')
text(ax, 22, 46, 'le plus haut : 2', 'sujet', 's'); text(ax, 66, 46, 'le plus haut : 3', 'limite', 's')
arrow(ax, (22, 42), (22, 32), 'resultat'); arrow(ax, (66, 42), (66, 32), 'limite')
box(ax, 4, 20, 36, 11, 'resultat', label='degré 2', size='l')
box(ax, 48, 20, 36, 11, 'limite', label='degré 3', size='l')
text(ax, 22, 12, 'quadratique', 'resultat', 'm'); text(ax, 66, 12, 'pas quadratique', 'limite', 'm')
save(fig, '15-072')
