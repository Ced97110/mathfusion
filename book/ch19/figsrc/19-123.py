import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# the two lines
text(ax, 27, 74, r'horizontale : $y=3$', 'sujet', 's', weight='bold')
line(ax, [(8, 66), (46, 66)], 'sujet', lw=1.8)
text(ax, 70, 77, r'verticale : $x=4$', 'autre', 's', weight='bold')
line(ax, [(70, 50), (70, 72)], 'autre', lw=1.8)
# the number line of slopes
f = numberline(ax, 8, 60, 30, -2, 3, 1)
disc(ax, f(0), 30, 1.7, 'resultat'); disc(ax, f(2), 30, 1.7, 'sujet')
arrow(ax, (f(0), 64), (f(0), 32.5), 'resultat', lw=1.2)
text(ax, f(0) + 2, 48, 'pente 0', 'resultat', 's', ha='left', weight='bold')
text(ax, f(2), 36, 'pente 2', 'sujet', 's')
# no place for the vertical line
arrow(ax, (70, 49), (70, 35), 'limite', lw=1.2); text(ax, 70, 31.5, r'$\times$', 'limite', 'l')
line(ax, [(70, 28), (70, 15.5)], 'limite', dash=True)
text(ax, 68, 22, 'aucune place', 'limite', 's', ha='right')
box(ax, 52, 6, 34, 9.5, 'limite', label='non définie', size='s')
save(fig, '19-123')
