import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 60, r'$10\div0$', 'autre', 'm'); text(ax, 22, 54, r'$0\cdot x=10$', 'autre', 's')
box(ax, 4, 38, 36, 11, 'limite', dash=True, label='aucune réponse', size='s')
text(ax, 66, 60, r'$0\div0$', 'sujet', 'm'); text(ax, 66, 54, r'$0\cdot x=0$', 'sujet', 's')
for i, (lab) in enumerate([r'$x=4$', r'$x=28$', 'tout $x$']):
    box(ax, 46, 38 - i * 12, 38, 10, 'resultat', label=lab, size='s')
text(ax, 22, 18, 'aucun nombre', 'limite', 's')
text(ax, 65, 7, 'tous conviennent', 'resultat', 's')
line(ax, [(44, 4), (44, 64)], 'fixe', dash=True)
save(fig, '12-123')
