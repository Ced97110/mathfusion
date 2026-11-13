import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, 'entiers plus grands que 0', 'encre', 's')
f = numberline(ax, 6, 82, 48, 0, 3, step=1, labels=True, arrow_right=False)
for v in (1, 2, 3):
    disc(ax, f(v), 48, 1.2, 'sujet')
disc(ax, f(1), 48, 2.4, 'resultat', fill=False)
text(ax, f(1), 55, 'plus petit : 1', 'resultat', 'm')
text(ax, 44, 34, 'fractions plus grandes que 0', 'encre', 's')
numberline(ax, 6, 82, 18, 0, 1, step=1, labels=False, arrow_right=False)
g = lambda k: 6 + 76 / 2 ** k
xs = [g(k) for k in range(1, 6)]
for x in xs:
    disc(ax, x, 18, 0.9, 'autre')
for x, s in [(6, '0'), (g(3), '1/8'), (g(2), '1/4'), (g(1), '1/2'), (82, '1')]:
    text(ax, x, 13, s, 'autre' if s not in ('0', '1') else 'fixe', 's')
for a, b in zip(xs[:-1], xs[1:]):
    arrow(ax, (a, 19), (b, 19), 'varie', curve=0.4)
disc(ax, 6, 18, 1.2, 'limite', fill=False)
text(ax, 56, 26, "aucune n'est la plus petite", 'limite', 's')
save(fig, '01-155')
