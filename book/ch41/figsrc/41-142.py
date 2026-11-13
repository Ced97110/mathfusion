import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig, ax = canvas(52)
A = (8, 30); B = (64, 30)
arrow(ax, A, B, 'fixe', lw=1.3)
tip = (A[0] + 30 * math.cos(math.radians(30)), A[1] + 30 * math.sin(math.radians(30)))
arrow(ax, A, tip, 'sujet', lw=1.5)
ax.add_patch(Arc(A, 26, 26, theta1=0, theta2=30, color=COL['varie'], lw=1.3, zorder=3))
text(ax, 4, 30, 'A', 'encre', 'm')
text(ax, 68, 30, 'B', 'encre', 'm')
text(ax, 15, 41.5, '50 N', 'sujet', 's')
text(ax, 36, 26, '20 m', 'fixe', 's')
text(ax, 27, 33.5, r'$\theta$', 'varie', 'm')
xs = [2, 24, 46, 68]
labs = [r'$\|F\|$' + '\n50', r'$\|AB\|$' + '\n20', r'$\cos\theta$' + '\n0,866', r'$W$' + '\n866,0 J']
roles = ['sujet', 'fixe', 'varie', 'resultat']
for x, lab, role in zip(xs, labs, roles):
    box(ax, x, 4, 17, 12, role, label=lab, size='s')
for x, sg in zip([21.5, 43.5, 65.5], [r'$\times$', r'$\times$', '=']):
    text(ax, x, 10, sg, 'encre', 'l')
save(fig, '41-142')
