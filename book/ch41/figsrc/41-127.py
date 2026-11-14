import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(70)
k = 0.3
O = (6, 36)
A = (O[0] + 180 * k, O[1])
R = (O[0] + 230 * k, O[1] + 86.6 * k)
B = (R[0], O[1])
arrow(ax, O, A, 'sujet', lw=1.3)
arrow(ax, A, R, 'varie', lw=1.3)
arrow(ax, O, R, 'resultat', lw=1.6)
line(ax, [A, B], 'fixe', dash=True)
line(ax, [B, R], 'fixe', dash=True)
ang = math.degrees(math.atan2(86.6, 230))
ax.add_patch(Arc(O, 30, 30, theta1=0, theta2=ang, color=COL['varie'], lw=1.0, zorder=3))
text(ax, 33, 40, r'$a$', 'sujet', 's')
text(ax, 62, 50, r'$v$', 'varie', 's')
text(ax, 34, 55, r'$r$', 'resultat', 's')
disc(ax, 79, 49, 2.6, 'fixe', label='1', size='s')
disc(ax, 45, 44, 2.6, 'fixe', label='2', size='s')
disc(ax, 26, 39.5, 2.6, 'fixe', label='3', size='s')
bw = 27
for i, (x, lab, role) in enumerate([
        (2, '1 · additionner\n' + r'$\langle 230\,;\,86{,}60\rangle$', 'fixe'),
        (30.5, '2 · norme\n' + r'$\sqrt{52\,900+7\,500}$' + '\n' + r'$\approx 245{,}76$', 'fixe'),
        (59, '3 · direction\n' + r'$\arctan(86{,}60/230)$' + '\n' + r'$\approx 20{,}63°$', 'fixe')]):
    box(ax, x, 4, bw, 21, role, label=lab, size='s')
save(fig, '41-127')
