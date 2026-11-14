import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Circle
fig, ax = canvas(70)
ax.add_patch(Circle((32, 36), 24, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=1, alpha=0.8))
ax.add_patch(Circle((56, 36), 24, ec=COL['autre'], fc=FILL['autre'], lw=1.0, zorder=1, alpha=0.8))
lens = Circle((32, 36), 24, transform=ax.transData)
ov = Circle((56, 36), 24, ec=COL['resultat'], fc=FILL['resultat'], lw=0, zorder=1.5)
ax.add_patch(ov); ov.set_clip_path(lens)
text(ax, 19, 46, r'$G_2$', 'sujet', 'l'); text(ax, 19, 38, 'ordre 12', 'sujet', 's'); text(ax, 19, 31, 'multiples de 5', 'sujet', 's')
text(ax, 69, 46, r'$H_2$', 'autre', 'l'); text(ax, 69, 38, 'ordre 30', 'autre', 's'); text(ax, 69, 31, 'multiples de 2', 'autre', 's')
text(ax, 44, 46, r'$G_2\cap H_2$', 'resultat', 's'); text(ax, 44, 38, 'ordre 6', 'resultat', 's'); text(ax, 44, 31, '0, 10, …, 50', 'resultat', 's')
text(ax, 44, 4, r'pgcd$(12\,;\,30)=6$', 'resultat', 's')
save(fig, '79-182')
