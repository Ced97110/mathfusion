import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
k = 34.0; a = math.radians(30); hyp = 1.732
K = (10, 12); F = (K[0] + hyp * math.cos(a) * k, 12); P = (F[0], 12 + hyp * math.sin(a) * k)
poly(ax, [K, F, P], 'sujet')
line(ax, [K, P], 'sujet', lw=1.8)
s = 3.0
line(ax, [(F[0] - s, 12), (F[0] - s, 12 + s), (F[0], 12 + s)], 'sujet')
t = [math.radians(d) for d in range(0, 31, 3)]
line(ax, [(K[0] + 11 * math.cos(x), 12 + 11 * math.sin(x)) for x in t], 'varie')
text(ax, 25, 14.6, '30°', 'varie', 's')
text(ax, K[0] - 3, 12, '$K$'); text(ax, F[0] + 3, 12, '$F$'); text(ax, P[0] + 3, P[1] + 1, '$P$')
text(ax, 24, 33, '$KP$ = 1,732', 'sujet', 's')
text(ax, 35, 7, '$KF$ = 1,732 × 0,866 = 1,5', 'resultat', 's')
text(ax, F[0] - 2, 20, '$FP$ = 1,732 × 0,5 = 0,866', 'resultat', 's', ha='right')
save(fig, '34-097')
