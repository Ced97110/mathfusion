import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u, ox, oy = 7.0, 16, 16
box(ax, ox, oy, 4 * u, 3 * u, 'sujet', r=0.3)
box(ax, ox, oy, 8 * u, 6 * u, 'autre', fill=False, r=0.3)
disc(ax, ox, oy, 1.2, 'varie')
text(ax, ox + 3.5, oy + 3.5, r'$O$', 'varie', 'l', weight='bold')
arrow(ax, (ox, oy - 3), (ox + 4 * u, oy - 3), 'sujet'); arrow(ax, (ox, oy - 8), (ox + 8 * u, oy - 8), 'autre')
arrow(ax, (ox - 3, oy), (ox - 3, oy + 3 * u), 'sujet'); arrow(ax, (ox - 8, oy), (ox - 8, oy + 6 * u), 'autre')
text(ax, ox + 2 * u, oy - 5.5 + 0.0, '4', 'sujet', 's', ); text(ax, ox + 6 * u, oy - 10.5, '8', 'autre', 's')
text(ax, ox - 5.5, oy + 1.5 * u, '3', 'sujet', 's'); text(ax, ox - 10.5, oy + 4.5 * u, '6', 'autre', 's')
text(ax, 70, 54, 'mesures depuis', 'encre', 's'); text(ax, 70, 50, r'le même point $O$', 'encre', 's')
save(fig, '09-015')
