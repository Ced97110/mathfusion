import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 8, 76, 10, 0, 24, step=1, arrow_right=False, every=6)
text(ax, 2, 50, '(4) : multiples de 4', 'sujet', 's', ha='left')
text(ax, 2, 38, '(6) : multiples de 6', 'autre', 's', ha='left')
text(ax, 2, 26, 'les deux : multiples de 12', 'resultat', 's', ha='left')
for v in range(0, 25, 4): disc(ax, f(v), 44, 1.6, 'sujet')
for v in range(0, 25, 6): disc(ax, f(v), 32, 1.6, 'autre')
for v in (0, 12, 24):
    disc(ax, f(v), 20, 1.6, 'resultat')
    line(ax, [(f(v), 21.6), (f(v), 42.4)], 'fixe', dash=True)
text(ax, f(12), 15, 'PPCM = 12', 'resultat', 's')
save(fig, '52-062')
