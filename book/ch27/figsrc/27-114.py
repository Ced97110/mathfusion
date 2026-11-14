import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(52)
L = 76; th = math.radians(20); h = L*math.tan(th)
line(ax, [(4, 6), (4+L, 6)], 'fixe', lw=1.2); line(ax, [(4, 6), (4+L, 6+h)], 'fixe', lw=1.2)
arrow(ax, (4, 6), (4+L*0.8, 6+h*0.8), 'varie', lw=1.6)
ax.add_patch(Arc((4, 6), 36, 36, theta1=0, theta2=20, color=COL['sujet'], lw=1))
text(ax, 44, 9.2, 'θ = 20°', 'sujet', 's')
text(ax, 40, 3, 'sol', 'fixe', 's')
text(ax, 50, 36, 'chemin = ligne de plus grande pente', 'varie', 's')
text(ax, 20, 46, 'φ = 0°', 'autre', 'l')
box(ax, 50, 42, 34, 8, 'resultat', label='α = θ = 20°')
save(fig, '27-114')
