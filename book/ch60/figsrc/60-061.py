import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 10, 78, 8, 0, 12, step=1, arrow_right=False, every=2)
for v in range(0, 13, 2):
    disc(ax, f(v), 26, 1.8, 'sujet')
for v in (0, 6, 12):
    disc(ax, f(v), 42, 1.8, 'autre')
    line(ax, [(f(v), 40), (f(v), 28)], 'fixe', dash=True)
    line(ax, [(f(v), 24), (f(v), 10)], 'fixe', dash=True)
text(ax, 27, 47, 'multiples de 6', 'autre', 's')
text(ax, 27, 31, 'multiples de 2', 'sujet', 's')
text(ax, 44, 58, 'd₁ = 2 divise d₂ = 6', 'resultat', 'l')
save(fig, '60-061')
