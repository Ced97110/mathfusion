import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, ux, uy = 12, 30, 20, 7
arrow(ax, (ox, oy), (ox + 2.4 * ux, oy), 'fixe', lw=0.8); arrow(ax, (ox, oy), (ox, oy + 4.5 * uy), 'fixe', lw=0.8)
xs = [i / 40 * 2 for i in range(41)]
line(ax, [(ox + x * ux, oy + x * x * uy) for x in xs], 'sujet', lw=1.3)
line(ax, [(ox, oy), (ox + 2.2 * ux, oy + 2.2 * uy)], 'varie', lw=1.3)
line(ax, [(ox + 2 * ux, oy), (ox + 2 * ux, oy + 4 * uy)], 'fixe', lw=0.5, dash=True)
disc(ax, ox + 2 * ux, oy + 4 * uy, 1.0, 'sujet'); disc(ax, ox + 2 * ux, oy + 2 * uy, 1.0, 'varie')
line(ax, [(ox + 2 * ux + 3, oy + 2 * uy), (ox + 2 * ux + 3, oy + 4 * uy)], 'limite', lw=1.2)
text(ax, ox + 2 * ux, oy - 3, r'$x = 2$', 'fixe', 's')
text(ax, ox + 6, oy + 4.2 * uy, r'$x^2$', 'sujet', 'm'); text(ax, ox + 2.2 * ux + 1, oy + 1.2 * uy, r'$a+bx$', 'varie', 's', ha='left')
text(ax, ox + 2 * ux + 5, oy + 4 * uy, '4', 'sujet', 'm', ha='left'); text(ax, ox + 2 * ux + 5, oy + 2 * uy - 1, '2', 'varie', 'm', ha='left')
text(ax, 72, oy + 3 * uy, 'écart', 'limite', 's')
for i, l in enumerate(['1', r'$x$', r'$x^2$', r'$x^3$']):
    box(ax, 6 + i * 11, 8, 10, 8, 'limite' if i == 2 else 'fixe', label=l, size='s')
arrow(ax, (51, 12), (66, 12), 'fixe'); text(ax, 78, 12, 'sans fin', 'fixe', 's')
save(fig, '76-025')
