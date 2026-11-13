import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(70)
ax.add_patch(Ellipse((22, 38), 38, 46, fc=FILL['sujet'], ec=COL['sujet'], lw=0.9, zorder=1))
ax.add_patch(Ellipse((66, 38), 32, 46, fc=FILL['resultat'], ec=COL['resultat'], lw=0.9, zorder=1))
text(ax, 22, 66, r'$GL_n(F)$', 'sujet', 'm'); text(ax, 66, 66, r'$F^*$', 'resultat', 'm')
def dot(x, y, role):
    ax.add_patch(Circle((x, y), 1.1, fc=COL[role], ec=COL[role], zorder=6))
for y, a, b in [(52, 'A', '2'), (40, 'B', '3'), (28, 'AB', '6')]:
    dot(24, y, 'sujet'); dot(64, y, 'resultat')
    text(ax, 20, y, a if len(a) == 1 else a, 'sujet', 's', ha='right', weight='bold')
    text(ax, 68, y, b, 'resultat', 's', ha='left', weight='bold')
    arrow(ax, (26, y), (62, y), 'varie', lw=0.9)
text(ax, 44, 55, 'det', 'varie', 's')
dot(24, 8, 'limite'); dot(64, 8, 'limite')
text(ax, 20, 8, 'écrasement', 'limite', 's', ha='right')
text(ax, 68, 8, '0', 'limite', 's', ha='left')
arrow(ax, (26, 8), (62, 8), 'limite', lw=0.9)
text(ax, 44, 11.5, 'det', 'limite', 's')
text(ax, 44, 3.5, '0 hors de F*', 'limite', 's') if False else None
save(fig, '73-031')
