import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
line(ax, [(8, 48), (74, 48)], 'sujet', lw=1.6)
text(ax, 44, 53, r'$f$ constante : $f(x+p)=f(x)$', 'sujet', 's')
yl = 26
arrow(ax, (4, yl), (80, yl), 'fixe', lw=0.8)
xp = {1: 70, 2: 44, 4: 26, 8: 15}
ax.add_patch(Circle((8, yl), 1.4, ec=COL['limite'], fc='white', lw=0.9, zorder=3))
text(ax, 8, yl - 4.2, '0', 'limite', 's')
for k, x in xp.items():
    disc(ax, x, yl, 1.3, 'varie' if k > 1 else 'sujet')
text(ax, 70, yl - 4.2, '0,001', 'sujet', 's')
text(ax, 44, yl - 4.2, '0,0005', 'varie', 's')
text(ax, 26, yl - 4.2, r'$p/4$', 'varie', 's')
text(ax, 15, yl + 4.2, r'$p/8$', 'varie', 's')
arrow(ax, (69, yl + 2.5), (45, yl + 2.5), 'varie', curve=0.35)
arrow(ax, (43, yl + 2.5), (27, yl + 2.5), 'varie', curve=0.35)
text(ax, 57, yl + 13, 'moitié : plus petit', 'varie', 's')
text(ax, 44, 9, 'toujours un plus petit : pas de période', 'limite', 's')
save(fig, '30-143')
