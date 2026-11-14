import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 14, 74, 8, -3, 3, 1, arrow_right=False)
B, k = 16, 4.0
pts = [(f(t / 10), B + (t / 10) ** 2 * k) for t in range(-30, 31)]
line(ax, pts, 'sujet', lw=1.6)
line(ax, [(8, B + 4 * k), (80, B + 4 * k)], 'varie', lw=1.6)
for v in (-2, 2):
    line(ax, [(f(v), 8), (f(v), B + 4 * k)], 'resultat', dash=True)
    disc(ax, f(v), B + 4 * k, 1.6, 'resultat')
text(ax, 40, 62, r'$x$ · $x$', 'sujet', 'm'); text(ax, 44, B + 4 * k + 3.5, '4', 'varie', 'm')
text(ax, 44, 24, 'deux rencontres', 'resultat', 's')
save(fig, '16-134')
