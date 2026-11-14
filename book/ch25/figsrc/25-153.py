import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax, c, r, a0, a1, role, lw=1.0):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
fig, ax = canvas(52)
cs = [11, 33, 55, 77]
labs = [(r'$\tan A$', 'sujet'), (r'$A$', 'fixe'), (r'$2A$', 'fixe'), (r'$\tan 2A$', 'resultat')]
subs = ['connu :\n0,5774', 'un seul\nangle', 'son\ndouble', 'cherché']
for c, (l, role), s in zip(cs, labs, subs):
    box(ax, c-9, 16, 18, 10, role, label=l, dash=(role == 'fixe'))
    text(ax, c, 9, s, role, 's')
for a, b in zip(cs[:-1], cs[1:]):
    arrow(ax, (a+9.4, 21), (b-9.4, 21), 'encre', lw=0.9)
ax.add_patch(FancyArrowPatch((cs[0], 27), (cs[3], 27), arrowstyle='-|>', mutation_scale=7, lw=1.2, ls='--', color=COL['varie'], connectionstyle='arc3,rad=-0.3', zorder=4))
text(ax, 44, 43, 'règle directe à trouver', 'varie', 'm')
text(ax, 44, 1.5, 'un seul résultat à chaque étape', 'resultat', 's')
save(fig, '25-153')
