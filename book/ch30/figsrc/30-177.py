import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
k = 76 / (2 * math.pi); f = lambda t: 6 + t * k
y0, u = 36, 8.0
ts = [i * 2 * math.pi / 120 for i in range(121)]
line(ax, [(5, y0), (84, y0)], 'fixe', lw=0.6)
line(ax, [(f(t), y0 + u * math.sin(t)) for t in ts], 'sujet')
line(ax, [(f(t), y0 + u * math.cos(t)) for t in ts], 'autre')
line(ax, [(f(t), y0 + u * (math.sin(t) + math.cos(t))) for t in ts], 'resultat', lw=1.6)
disc(ax, f(0), y0 + u, 1.2, 'resultat')
disc(ax, f(math.pi / 4), y0 + u * math.sqrt(2), 1.2, 'resultat')
text(ax, 3.2, y0 + u + 3, '1', 'resultat', 's')
text(ax, f(math.pi / 4) + 2, y0 + u * math.sqrt(2) + 4, '1,414', 'resultat', 's')
text(ax, f(math.pi / 4), y0 - 3, r'$\pi/4$', 'fixe', 's')
for x, role, s in [(2, 'sujet', r'$\sin x$'), (22, 'autre', r'$\cos x$'), (42, 'resultat', r'somme : $\sqrt{2}\sin(x+\pi/4)$')]:
    line(ax, [(x, 9), (x + 6, 9)], role, lw=1.6)
    text(ax, x + 8, 9, s, role, 's', ha='left')
save(fig, '30-177')
