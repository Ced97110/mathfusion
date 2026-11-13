import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
k = 40; K = (10, 16); F = (K[0] + 1.5 * k, 16); P = (F[0], 16 + 0.866 * k)
poly(ax, [K, F, P], 'fixe')
line(ax, [K, F], 'sujet', lw=2.2); line(ax, [F, P], 'sujet', lw=2.2)
s = 3.0
line(ax, [(F[0] - s, 16), (F[0] - s, 16 + s), (F[0], 16 + s)], 'fixe')
t = [math.radians(d) for d in range(0, 31, 3)]
line(ax, [(K[0] + 16 * math.cos(x), 16 + 16 * math.sin(x)) for x in t], 'resultat', lw=1.2)
text(ax, 34, 19.4, '$\\theta/2$ = 30°', 'resultat', 's')
text(ax, K[0] - 3, 16, '$K$'); text(ax, F[0] + 3, 16, '$F$'); text(ax, P[0] + 3, P[1] + 1, '$P$')
text(ax, 40, 10, '1 + cos $\\theta$ = 1,5', 'sujet', 's')
text(ax, F[0] - 2, 30, 'sin $\\theta$ = 0,866', 'sujet', 's', ha='right')
text(ax, 6, 53, 'tan 30° = 0,866 ÷ 1,5', 'resultat', 'm', ha='left')
text(ax, 6, 47.5, '= 0,5774', 'resultat', 'm', ha='left')
save(fig, '34-106')
