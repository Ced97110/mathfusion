import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def hollow(ax, p, role='sujet', r=1.3):
    ax.add_patch(Circle(p, r, ec=COL[role], fc='white', lw=0.9, zorder=6))

fig, ax = canvas(66)
plt.rcParams['hatch.linewidth'] = 0.6
for x0 in (2, 31, 60): box(ax, x0, 26, 26, 34, 'fixe', fill=False)
line(ax, [(5, 30), (24, 55)], 'autre', lw=1.5)
line(ax, [(33, 43), (56, 43)], 'fixe', lw=0.8)
line(ax, [(41, 43), (56, 43)], 'autre', lw=2.2); hollow(ax, (41, 43), 'autre', 1.4)
_tri = Polygon([(63, 30), (85, 57), (63, 57)], closed=True, ec='none', fc=FILL['sujet'], lw=0, zorder=2)
ax.add_patch(_tri)
for _k in range(-30, 30):
    _l, = ax.plot([60, 90], [30 + _k * 2.2 - 3, 30 + _k * 2.2 + 27], color=COL['sujet'], lw=0.6, zorder=2.5)
    _l.set_clip_path(_tri)
line(ax, [(63, 30), (85, 57)], 'sujet', lw=1.2, dash=True)
text(ax, 15, 15, 'droite :\ndes couples\nd’une équation', 'autre', 's')
text(ax, 44, 15, 'demi-droite :\ndes nombres\nd’une inéquation', 'autre', 's')
text(ax, 73, 15, 'zone hachurée :\ndes couples\nd’une inéquation', 'sujet', 's')
save(fig, '20-013')
