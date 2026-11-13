import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
L = 24; c, s = 0.8192, 0.5736
x0, y0 = 6, 76
Pp = (x0 + L * c, y0 + L * s); Hh = (Pp[0], y0)
poly(ax, [(x0, y0), Hh, Pp], 'sujet')
line(ax, [(x0, y0), Pp], 'sujet', lw=1.6)
line(ax, [(Hh[0] - 1.8, y0), (Hh[0] - 1.8, y0 + 1.8), (Hh[0], y0 + 1.8)], 'fixe', lw=0.6)
text(ax, x0 + 9, y0 - 3, '0,8192', 'autre', 's'); text(ax, Hh[0] + 6.5, y0 + 7, '0,5736', 'varie', 's')
text(ax, x0 + 7.5, y0 + 10.5, '1', 'sujet', 's', weight='bold')
text(ax, 62, 91, 'départ : triangle OHP,', 'encre', 's'); text(ax, 62, 86, 'angle droit en H, OP = 1', 'encre', 's')
box(ax, 4, 52, 80, 11, 'fixe', label=r'$OH^2+HP^2=OP^2$', size='l')
arrow(ax, (44, 70), (44, 64), 'fixe'); text(ax, 46, 67, '1. Pythagore', 'fixe', 's', ha='left')
arrow(ax, (44, 51), (44, 36), 'varie', lw=2.4)
text(ax, 47, 46.5, '2. OP devient 1', 'varie', 's', ha='left', weight='bold')
text(ax, 47, 41, 'étape qui porte le poids', 'varie', 's', ha='left')
box(ax, 4, 22, 80, 12, 'resultat', label=r'$\cos^2\theta+\sin^2\theta=1$', size='l')
text(ax, 44, 14, '0,6710 + 0,3290 = 1', 'resultat', 's')
save(fig, '31-068')
