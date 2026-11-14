import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = lambda t: 5 + 11 * t
y0, u = 30, 12
line(ax, [(3, y0), (86, y0)], 'fixe', lw=0.6)
line(ax, [(f(i * 7 / 140), y0 + u * math.sin(i * 7 / 140)) for i in range(141)], 'sujet')
line(ax, [(f(math.pi / 2), 14), (f(math.pi / 2), 43)], 'fixe', dash=True)
text(ax, f(math.pi / 2), 46.5, r'$x=\pi/2$', 'fixe', 's')
disc(ax, f(math.pi), y0, 1.3, 'fixe'); text(ax, f(math.pi), y0 + 3.5, r'$(\pi,0)$', 'fixe', 's')
P, Q, R, S = 0.524, 2.618, 5.760, 0.524 + 2 * math.pi
disc(ax, f(P), y0 + 6, 1.5, 'sujet'); text(ax, f(P) - 3.5, y0 + 9, 'P', 'sujet', 's')
disc(ax, f(Q), y0 + 6, 1.5, 'varie'); text(ax, f(Q) + 1.5, 41, 'retournement', 'varie', 's', ha='left')
disc(ax, f(R), y0 - 6, 1.5, 'varie'); text(ax, f(R), 16, 'demi-tour', 'varie', 's')
disc(ax, f(S), y0 + 6, 1.5, 'varie')
line(ax, [(f(P), y0 + 6), (f(P), 51)], 'fixe', dash=True); line(ax, [(f(S), y0 + 6), (f(S), 51)], 'fixe', dash=True)
arrow(ax, (f(P), 51), (f(S), 51), 'varie'); text(ax, (f(P) + f(S)) / 2, 55, r'translation de $2\pi$', 'varie', 's')
save(fig, '30-182')
