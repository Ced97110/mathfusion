import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(84)
cx, cy, U = 44, 46, 17.0
arrow(ax, (3, cy), (84, cy), 'fixe', lw=0.8)
arrow(ax, (cx - 14, 16), (cx - 14, 78), 'fixe', lw=0.8)
rts = np.roots([1, 0, 0, 0, -4, 2])
for z in rts:
    X, Y = cx + z.real * U, cy + z.imag * U
    if abs(z.imag) < 1e-6:
        disc(ax, X, Y, 1.8, 'fixe')
    else:
        disc(ax, X, Y, 1.8, 'varie')
zc = [z for z in rts if z.imag > 1e-6][0]
X = cx + zc.real * U
arrow(ax, (X, cy + zc.imag * U - 3), (X, cy - zc.imag * U + 3), 'varie', both=True)
text(ax, X + 3, cy + zc.imag * U + 4, r'$r_1$', 'varie', 's', ha='left')
text(ax, X + 3, cy - zc.imag * U - 4, r'$r_2$', 'varie', 's', ha='left')
text(ax, 62, 32, '3 racines fixées', 'fixe', 's')
text(ax, 62, 76, 'échangées', 'varie', 's')
text(ax, 44, 8, r'conjugaison : $(r_1\ r_2)$', 'resultat', 's')
save(fig, '65-136')
