import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 2, 54, 18, 12, 'sujet', label=r'$\alpha$', size='l'); text(ax, 24, 60, '=', 'encre', 'l')
box(ax, 28, 54, 30, 12, 'autre', label='arcsin', size='l'); box(ax, 62, 54, 18, 12, 'varie', label=r'$k$', size='l')
text(ax, 11, 46, 'angle\nprincipal', 'sujet', 's'); text(ax, 43, 46, 'l’angle dont\nle sinus vaut…', 'autre', 's'); text(ax, 71, 46, 'la hauteur\n(un nombre)', 'varie', 's')
text(ax, 44, 36, 'se lit : « alpha égale arcsinus de k »', 'encre', 's')
box(ax, 4, 18, 80, 10, 'sujet', label='α = arcsin 0,5 = 30°')
box(ax, 4, 3, 80, 10, 'sujet', label='α = arcsin 0,4 ≈ 23,58°')
save(fig, '32-032')
