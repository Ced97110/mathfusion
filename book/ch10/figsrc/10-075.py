import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
f = lambda v: 8 + (v - 350000) / 60000 * 68
text(ax, 3, 42, r'$87 \times 4\,316$ g', 'sujet', 'm', ha='left')
ax.add_patch(Rectangle((8, 19), f(400000) - 8, 10, ec='none', fc=FILL['resultat'], zorder=1))
line(ax, [(8, 24), (76, 24)], 'fixe')
line(ax, [(f(400000), 16), (f(400000), 34)], 'limite', lw=1.4)
text(ax, f(400000), 38, 'limite 400 000', 'limite', 'm')
disc(ax, f(360000), 24, 1.5, 'varie'); text(ax, f(360000), 33, 'estimation 360 000', 'varie', 'm')
disc(ax, f(375492), 24, 1.5, 'resultat'); text(ax, f(375492), 15, 'vrai poids 375 492', 'resultat', 'm')
text(ax, 36, 8, 'même côté de la limite', 'resultat', 'm')
save(fig, '10-075')
