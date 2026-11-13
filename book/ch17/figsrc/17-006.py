import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
f = lambda v: 8 + v / 18 * 66
def axis(y):
    arrow(ax, (8, y), (84, y), 'fixe', lw=0.9)
    for v in (0, 11, 15):
        ax.plot([f(v)] * 2, [y - 1.2, y + 1.2], color=COL['fixe'], lw=0.8, zorder=1.5)
        text(ax, f(v), y - 4.5, f'{v} €', 'fixe', 's')
text(ax, 25, 74, r'$3 + 2d = 15$', 'autre', 'm')
axis(60)
disc(ax, f(15), 60, 1.8, 'autre')
text(ax, f(15), 68, 'exactement 15 €', 'autre', 's')
text(ax, 25, 42, r'$3 + 2d \leq 15$', 'sujet', 'm')
axis(28)
line(ax, [(f(0), 28), (f(15), 28)], 'sujet', lw=2.4)
disc(ax, f(11), 28, 1.8, 'sujet'); disc(ax, f(15), 28, 1.8, 'sujet')
line(ax, [(f(15), 26), (f(15), 36)], 'limite', lw=1.4)
line(ax, [(f(15) + 0.5, 28), (84, 28)], 'limite', lw=2.4)
text(ax, f(15), 39, 'limite', 'limite', 's')
text(ax, 77, 21, 'interdit', 'limite', 's')
save(fig, '17-006')
