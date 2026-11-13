import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 24, 48, 40, 10, 'sujet', label=r'$x=-9,\ y=-4$')
arrow(ax, (38, 48), (23, 35), 'fixe'); arrow(ax, (50, 48), (65, 35), 'fixe')
box(ax, 3, 23, 40, 12, 'limite', label=r'$\sqrt{-9}\,/\,\sqrt{-4}$')
box(ax, 45, 23, 40, 12, 'resultat', label=r'$\sqrt{9/4}=3/2$')
text(ax, 23, 17, "n'a pas de sens", 'limite', 's')
text(ax, 65, 17, 'existe', 'resultat', 's')
save(fig, '22-096')
