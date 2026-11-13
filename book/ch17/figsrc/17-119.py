import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 84, r'$x > 5$', 'sujet', 'l')
specs = [(68, '5,1', '6'), (44, '5,01', '5,1'), (20, '5,001', '5,01')]
for y, d, e in specs:
    arrow(ax, (12, y), (78, y), 'fixe', lw=0.9)
    disc(ax, 12, y, 1.3, 'limite', fill=False)
    disc(ax, 18, y, 1.3, 'resultat')
    ax.add_patch(Circle((18, y), 1.3, ec=COL['resultat'], fc=COL['resultat'], zorder=3))
    text(ax, 18, y + 4, d, 'resultat', 's')
    text(ax, 12, y - 4, '5', 'limite', 's')
    text(ax, 72, y - 4, e, 'fixe', 's')
for y in (68, 44):
    line(ax, [(18, y - 1.5), (72, y - 22 + 1.5)], 'varie', dash=True)
    text(ax, 56, y - 6, 'on agrandit', 'varie', 's')
text(ax, 44, 6, 'toujours une autre solution', 'resultat', 'm', weight='bold')
save(fig, '17-119')
