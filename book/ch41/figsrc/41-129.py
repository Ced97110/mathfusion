import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(52)
k = 0.18
wind = (50 * k, 86.6 * k)
# gauche : cap vers l'est
O = (3, 24)
A = (O[0] + 180 * k, O[1])
R = (A[0] + wind[0], A[1] + wind[1])
line(ax, [O, (R[0], O[1])], 'fixe', dash=True)
arrow(ax, O, A, 'sujet', lw=1.3)
arrow(ax, A, R, 'varie', lw=1.3)
arrow(ax, O, R, 'resultat', lw=1.6)
text(ax, 22, 48, 'cap vers l’est', 'sujet', 'm')
text(ax, 19, 20.5, 'avion', 'sujet', 's')
text(ax, 43, 28.5, 'vent', 'varie', 's')
text(ax, 16, 35.5, 'résultat', 'resultat', 's')
# droite : cap un peu vers le sud
O2 = (48, 28)
ax_ = math.sqrt(180 ** 2 - 86.6 ** 2) * k
A2 = (O2[0] + ax_, O2[1] - 86.6 * k)
R2 = (A2[0] + wind[0], A2[1] + wind[1])
arrow(ax, O2, A2, 'sujet', lw=1.3)
arrow(ax, A2, R2, 'varie', lw=1.3)
arrow(ax, O2, R2, 'resultat', lw=1.6)
text(ax, 66, 48, 'cap un peu vers le sud', 'sujet', 'm')
text(ax, 56, 17.5, 'avion', 'sujet', 's')
text(ax, 74, 22, 'vent', 'varie', 's')
text(ax, 66, 31.5, 'résultat', 'resultat', 's')
save(fig, '41-129')
