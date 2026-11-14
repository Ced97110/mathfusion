import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(64)
def ball(cx, cy, w, role):
    ax.add_patch(Ellipse((cx, cy), w, 17, ec=COL[role], fc='none', lw=0.9, ls='--', zorder=1))
# panneau A : distance 3
yA = 50
ball(22, yA, 32, 'sujet'); ball(62, yA, 32, 'varie')
for x, w, r in zip([12, 32, 52, 72], ['000', '100', '110', '111'], ['sujet', 'sujet', 'varie', 'varie']):
    disc(ax, x, yA, 4.6, r, label=w, size='s')
text(ax, 44, 36, '000 et 111 : 3 arêtes, boules séparées', 'resultat', 's')
# panneau B : distance 2
yB = 20
ball(29, yB, 42, 'sujet'); ball(59, yB, 42, 'varie')
disc(ax, 14, yB, 4.6, 'sujet', label='000', size='s')
disc(ax, 44, yB, 4.6, 'limite', label='001', size='s')
disc(ax, 74, yB, 4.6, 'varie', label='011', size='s')
text(ax, 44, 6, '000 et 011 : 2 arêtes, 001 est dans les deux', 'limite', 's')
save(fig, '68-020')
