import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 73, 'unités de ℤ : 1 et −1', 'encre', 'm')
f = numberline(ax, 10, 70, 34, -2, 2, step=1)
for v in (-2, -1, 0, 1, 2):
    disc(ax, f(v), 34, 1.6, 'resultat' if abs(v) == 1 else 'limite')
for v, s in [(1, '1 × 1 = 1'), (-1, '(−1) × (−1) = 1')]:
    line(ax, [(f(v), 36), (f(v), 42)], 'resultat', lw=0.5, dash=True)
    text(ax, f(v), 45, s, 'resultat', 's')
for v, s in [(0, '0 × v = 0, jamais 1'), (2, '2 × v = 1 → v = ½')]:
    line(ax, [(f(v), 36), (f(v), 52)], 'limite', lw=0.5, dash=True)
    text(ax, f(v), 55, s, 'limite', 's')
box(ax, 2, 6, 84, 12, 'autre', label='dans ℚ : 2 × ½ = 1, unité')
save(fig, '56-030')
