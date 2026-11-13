import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def dot(x, y, role, full=True, r=1.6):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL["encre"], lw=0.9, zorder=4))
box(ax, 14, 66, 60, 10, 'fixe', label='compare deux nombres')
box(ax, 2, 6, 41, 42, 'autre', fill=False)
box(ax, 45, 6, 41, 42, 'sujet', fill=False)
arrow(ax, (30, 66), (22, 48), 'fixe'); arrow(ax, (58, 66), (66, 48), 'fixe')
# égalité
text(ax, 22.5, 41, 'égalité', 'autre', 'm', weight='bold')
text(ax, 22.5, 33, r'$7 = 7$', 'autre', 'l')
line(ax, [(8, 22), (37, 22)], 'fixe'); dot(22.5, 22, 'autre'); text(ax, 22.5, 17, '7', 'autre', 's')
text(ax, 22.5, 10.5, 'même point', 'autre', 's')
# inégalité
text(ax, 65.5, 41, 'inégalité', 'sujet', 'm', weight='bold')
text(ax, 65.5, 33, r'$3 < 7$', 'sujet', 'l')
line(ax, [(51, 22), (80, 22)], 'fixe'); dot(56, 22, 'sujet'); dot(75, 22, 'sujet')
text(ax, 56, 17, '3', 'sujet', 's'); text(ax, 75, 17, '7', 'sujet', 's')
text(ax, 65.5, 10.5, '3 à gauche de 7', 'sujet', 's')
save(fig, '17-019')
