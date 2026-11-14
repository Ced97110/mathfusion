import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
s = 4.6; ox, oy = 40, 20
P = lambda a: (ox + a * 2 * s, oy + a * s)
xs = {a: ox + a * 2 * s for a in range(-2, 4)}
text(ax, 4, 70, 'coefficients  R = ℤ', 'fixe', 's', ha='left', weight='bold')
text(ax, 84, 8, 'module  M = Rx', 'sujet', 's', ha='right', weight='bold')
line(ax, [(P(-2.5)[0], P(-2.5)[1]), (P(3.5)[0], P(3.5)[1])], 'sujet', lw=0.8, dash=True)
for a in range(-2, 4):
    used = a in (-2, 3)
    disc(ax, xs[a], 62, 3.0, 'varie' if used else 'fixe', label=str(a).replace('-', '−'), size='s')
    disc(ax, *P(a), 1.6 if used else 1.1, 'sujet')
    arrow(ax, (xs[a], 58.8), (P(a)[0], P(a)[1] + 2.6), 'varie' if used else 'fixe', lw=1.0 if used else 0.6)
text(ax, P(3)[0] - 2, P(3)[1] - 5, r'$(6\,;\,3)$', 'sujet', 's')
text(ax, P(-2)[0] + 3, P(-2)[1] - 5, r'$(-4\,;\,-2)$', 'sujet', 's')
text(ax, 80, 46, r'$\mu_x : a \mapsto a\,x$', 'varie', 's', ha='right')
save(fig, '57-162')
