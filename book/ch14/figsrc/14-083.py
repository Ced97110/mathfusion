import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [8 + i * 10.5 for i in range(8)]
for i, x in enumerate(xs):
    disc(ax, x, 48, 4, 'sujet' if i < 5 else 'autre', label='2')
for a, b in zip(xs, xs[1:]):
    ax.plot([(a + b) / 2], [48], marker='x', ms=3.5, mew=1, color=COL['varie'], zorder=4)
brace(ax, xs[0] - 4, xs[4] + 4, 42, 'sujet', r'$2^5$')
brace(ax, xs[5] - 4, xs[7] + 4, 42, 'autre', r'$2^3$')
text(ax, 44, 24, r'7 multiplications $\times$', 'varie', 'm')
box(ax, 8, 4, 34, 11, 'resultat', label=r'$5 + 3 = 8$', size='m')
box(ax, 48, 4, 32, 11, 'resultat', label=r'$2^8 = 256$', size='m')
arrow(ax, (42, 9.5), (48, 9.5), 'resultat')
text(ax, 25, 19, '1 addition', 'resultat', 's')
save(fig, '14-083')
