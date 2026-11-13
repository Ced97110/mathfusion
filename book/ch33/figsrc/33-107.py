import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 18
f = numberline(ax, 8, 68, y, 0, 180, step=30, every=3)
ax.add_patch(Rectangle((f(0), y - 1.2), f(90) - f(0), 2.4, fc=FILL['resultat'], ec=COL['resultat'], lw=0.8, zorder=1))
line(ax, [(f(90), y - 1.4), (f(90), y + 14)], 'fixe', lw=0.8, dash=True)
text(ax, f(45), 8, 'dans l’intervalle', 'resultat', 's')
disc(ax, f(150), y, 1.8, 'sujet'); disc(ax, f(30), y, 1.8, 'resultat')
text(ax, f(150), y + 5.5, '150°', 'sujet', 'm'); text(ax, f(30), y + 5.5, '30°', 'resultat', 'm')
arrow(ax, (f(150) - 2, y + 10), (f(30) + 2, y + 10), 'varie', curve=0.3)
text(ax, f(90), y + 22, r'$\pi - x$', 'varie', 'm')
text(ax, f(90), y + 29, 'même sinus : 0,5', 'encre', 's')
save(fig, '33-107')
