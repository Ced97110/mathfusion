import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 78, 'but : $x$ et $x′$ de même classe\n⇒ $ax$ et $ax′$ de même classe', 'fixe', 's')
# ligne du haut : deux représentants d'une même classe
box(ax, 6, 52, 30, 10, 'sujet', label=r'$x=(0\,;\,0)$', size='s')
box(ax, 52, 52, 30, 10, 'sujet', label=r'$x′=(1\,;\,0)$', size='s')
line(ax, [(38, 58), (50, 58)], 'resultat', lw=1.2)
line(ax, [(38, 56), (50, 56)], 'resultat', lw=1.2)
text(ax, 44, 68, r'différence $\in\mathbb{Z}^2$ : même classe', 'resultat', 's')
# on applique a = 1/2
arrow(ax, (21, 51.5), (21, 33.5), 'varie', lw=1.3)
arrow(ax, (67, 51.5), (67, 33.5), 'varie', lw=1.3)
text(ax, 11, 42.5, r'$\times\frac{1}{2}$', 'varie', 's')
text(ax, 77, 42.5, r'$\times\frac{1}{2}$', 'varie', 's')
# ligne du bas : deux classes différentes
box(ax, 6, 22, 30, 10, 'sujet', label=r'$\frac{1}{2}x=(0\,;\,0)$', size='s')
box(ax, 52, 22, 30, 10, 'limite', label=r'$\frac{1}{2}x′=(\frac{1}{2}\,;\,0)$', size='s')
line(ax, [(38, 28), (50, 28)], 'limite', lw=1.2)
line(ax, [(38, 26), (50, 26)], 'limite', lw=1.2)
line(ax, [(42.4, 24.2), (45.6, 29.8)], 'limite', lw=1.2)
text(ax, 44, 14, r'différence $(\frac{1}{2}\,;\,0)\notin\mathbb{Z}^2$', 'limite', 's')
text(ax, 44, 6, 'autre classe : l’action casse', 'limite', 's', weight='bold')
save(fig, '57-143')
