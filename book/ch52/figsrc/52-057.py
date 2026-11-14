import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 8, 76, 16, 0, 24, step=1, arrow_right=False, every=3)
text(ax, 2, 52, '(3) : multiples de 3', 'sujet', 's', ha='left')
text(ax, 2, 38, '(12) : multiples de 12', 'varie', 's', ha='left')
for v in range(0, 25, 3): disc(ax, f(v), 46, 1.6, 'sujet')
for v in (0, 12, 24):
    disc(ax, f(v), 32, 1.6, 'varie')
    line(ax, [(f(v), 33.6), (f(v), 44.4)], 'fixe', dash=True)
text(ax, 44, 4, r'$(3) \supseteq (12)$ car 3 divise 12', 'resultat', 's')
save(fig, '52-057')
