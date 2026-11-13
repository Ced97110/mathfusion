import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Circle
fig, ax = canvas(60)
top = [23, 37, 51, 65]; bot = [16, 30, 44, 58, 72]
for x, s in zip(top, '1331'):
    disc(ax, x, 48, 3.5, 'sujet', label=s)
for x, s in zip(bot, '14641'):
    if x in (30, 44):
        disc(ax, x, 30, 3.5, 'resultat'); text(ax, x, 30, s, 'resultat', 'm', weight='bold')
    elif x == 58:
        disc(ax, x, 30, 3.5, 'fixe', label=s)
    else:
        ax.add_patch(Circle((x, 30), 3.5, ec=COL['limite'], fc=FILL['fixe'], lw=0.8, zorder=2))
        text(ax, x, 30, s, 'fixe', 'm')
for a, b in [(37, 44), (51, 44), (23, 30), (37, 30)]:
    arrow(ax, (a, 44.5), (b, 33.5), 'varie', lw=1.3)
for a, b in [(51, 58), (65, 58)]:
    arrow(ax, (a, 44.5), (b, 33.5), 'fixe', lw=0.6)
text(ax, 30, 20, '1 + 3 = 4', 'resultat', 'm')
text(ax, 44, 12, '3 + 3 = 6', 'resultat', 'm')
arrow(ax, (23, 44.5), (16, 33.5), 'limite', lw=0.6)
arrow(ax, (65, 44.5), (72, 33.5), 'limite', lw=0.6)
text(ax, 72, 20, 'bord : un seul voisin', 'limite', 's')
save(fig, '01-170')
