import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
ox, oy = 22, 42
arrow(ax, (4, oy), (44, oy), 'fixe', lw=0.9)
arrow(ax, (ox, 18), (ox, 70), 'fixe', lw=0.9)
text(ax, 38, oy + 4, 'réels', 'fixe', 's')
for v, lab in ((0, '0'), (1, '1')):
    px = ox + v * 14
    ax.plot([px], [oy], 'o', color=COL['fixe'], ms=2.5, zorder=4)
text(ax, ox - 3, oy - 3, '0', 'fixe', 's')
text(ax, ox + 14, oy - 3, '1', 'fixe', 's')
line(ax, [(ox, oy), (ox, oy + 14)], 'sujet', dash=True)
disc(ax, ox, oy + 14, 2.2, 'sujet')
text(ax, ox + 6, oy + 14, r'$i$', 'sujet', 'l')
text(ax, 34, 66, 'pas un réel', 'limite', 's')
arrow(ax, (31, 64.5), (ox + 2, oy + 16), 'limite', lw=0.6, curve=0.2)
box(ax, 48, 46, 36, 22, 'sujet', label=None)
text(ax, 66, 63, r'$i^2=-1$', 'sujet', 'l')
text(ax, 66, 55, r'$x^2+1$ vaut', 'sujet', 's')
text(ax, 66, 50, r'$-1+1=0$', 'resultat', 'm')
box(ax, 48, 14, 36, 14, 'resultat', label='algébrique', size='m')
arrow(ax, (66, 46), (66, 28), 'varie')
save(fig, '61-070')
