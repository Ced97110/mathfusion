import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
ox, oy, sc = 8, 6, 6.0
P = lambda a, b: (ox + a * sc, oy + b * sc)
line(ax, [P(0, 0), P(10.8, 0)], 'fixe', lw=0.5)
line(ax, [P(0, 0), P(0, 10.8)], 'fixe', lw=0.5)
arrow(ax, P(0, 0), P(4, 6), 'sujet', lw=1.4)
arrow(ax, P(0, 0), P(10, 10), 'autre', lw=1.0)
for k in range(1, 11):
    disc(ax, *P(k, k), 0.8, 'autre')
for k in (1, 2):
    disc(ax, *P(2 * k, 3 * k), 1.1, 'sujet')
text(ax, 32, 54, 'f₁ = (4, 6) = 2e′₁', 'sujet', 's', ha='right')
text(ax, 86, 78, 'f₁ + f₂ = (10, 10) = 10e′₂', 'autre', 's', ha='right')
text(ax, 62, 22, 'f₂ ← f₂ + f₁', 'varie', 's')
save(fig, '59-118')
