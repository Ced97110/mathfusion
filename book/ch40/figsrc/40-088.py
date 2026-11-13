import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# ligne du paramètre t : trois instants de la roue
xs = [30, 52, 74]
text(ax, 44, 53, 'x = f(t)  et  y = g(t) : même t', 'sujet', 'm')
text(ax, 10, 40, 't', 'varie', 'l', weight='bold')
arrow(ax, (20, 40), (84, 40), 'varie', lw=1.1)
for x, lab in zip(xs, ['départ', 'demi-tour', 'tour']):
    disc(ax, x, 40, 1.3, 'varie')
    text(ax, x, 45.5, lab, 'varie', 's')
    line(ax, [(x, 37.5), (x, 31.5)], 'varie', lw=0.7, dash=True)
    line(ax, [(x, 24.5), (x, 17.5)], 'varie', lw=0.7, dash=True)
text(ax, 10, 28, 'x = f(t)', 'sujet', 's')
text(ax, 10, 14, 'y = g(t)', 'sujet', 's')
for x, vx, vy in zip(xs, ['0', '1,10', '2,20'], ['0', '0,70', '0']):
    box(ax, x - 7, 24.5, 14, 7, 'sujet', label=vx, size='s')
    box(ax, x - 7, 10.5, 14, 7, 'sujet', label=vy, size='s')
text(ax, 44, 4, 'valeurs en mètres', 'fixe', 's')
save(fig, '40-088')
