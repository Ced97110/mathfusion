import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(62)
cx, cy, u = 26, 26, 14
for i in range(-1, 3):
    for j in range(-1, 3):
        disc(ax, cx + i*u, cy + j*u, 0.7, 'fixe')
P = lambda a, b: (cx + a*u, cy + b*u)
ax.add_patch(Arc((cx, cy), 2*u*0.7, 2*u*0.7, theta1=0, theta2=80, ec=COL['varie'], lw=1.0, zorder=3))
t = math.radians
arrow(ax, (cx + 0.7*u*math.cos(t(70)), cy + 0.7*u*math.sin(t(70))), (cx + 0.7*u*math.cos(t(90)), cy + 0.7*u*math.sin(t(90))), 'varie')
arrow(ax, P(0, 0), P(1, 0), 'sujet', lw=1.4)
arrow(ax, P(0, 0), P(0, 1), 'resultat', lw=1.4)
disc(ax, *P(0, 0), 0.9, 'encre')
text(ax, cx + 0.5*u, cy - 3.2, r'$v$', 'sujet', 'm')
text(ax, cx - 6, cy + 0.5*u, 'v tourné', 'resultat', 's', ha='center')
text(ax, 54, 46, 'le papier glisse', 'sujet', 's', ha='left')
text(ax, 54, 42.5, 'de 1 vers la droite', 'sujet', 's', ha='left')
text(ax, 54, 32, 'il tourne d’un', 'varie', 's', ha='left')
text(ax, 54, 28.5, 'quart de tour', 'varie', 's', ha='left')
text(ax, 54, 18, 'il glisse donc de 1', 'resultat', 's', ha='left')
text(ax, 54, 14.5, 'vers le haut', 'resultat', 's', ha='left')
save(fig, '74-083')
