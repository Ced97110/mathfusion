import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(54)
# left : h(x) = 4x^2 touches the axis at 0
text(ax, 23, 50, 'h = 4x² a la racine réelle 0', 'sujet', 's', weight='bold')
line(ax, [(5, 16), (41, 16)], 'fixe')
t = np.linspace(-1, 1, 60)
line(ax, [(23 + 11 * a, 16 + 14 * a * a) for a in t], 'sujet', lw=1.5)
disc(ax, 23, 16, 1.4, 'resultat')
text(ax, 23, 9, 'racine 0', 'resultat', 's')
text(ax, 36, 36, r'$h(x)=4x^2$', 'sujet', 's')
# right : above position 0 there is no real height
text(ax, 66, 50, 'f = y² + 1 : pas de point réel', 'limite', 's', weight='bold')
line(ax, [(48, 16), (84, 16)], 'fixe')
line(ax, [(66, 16), (66, 26)], 'varie', dash=True)
disc(ax, 66, 16, 1.4, 'varie')
text(ax, 66, 9, 'position 0', 'varie', 's')
text(ax, 66, 31, 'aucune hauteur réelle', 'limite', 's')
text(ax, 66, 38, r'$y^2+1=0$', 'limite', 's')
save(fig, '70-156')
