import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx, cy, R = 28, 30, 20
disc(ax, cx, cy, R, 'fixe', fill=False)
disc(ax, cx + R, cy, 1.8, 'resultat')
text(ax, cx + R + 4.5, cy, '1', 'resultat', 'm')
text(ax, 72, 48, 'φ(1) = 1', 'resultat', 'm')
text(ax, 72, 40, 'Φ₁(x) = x − 1', 'sujet', 'm')
text(ax, 72, 31, 'racine : 1', 'resultat', 's')
text(ax, 72, 23, 'rien à relier', 'fixe', 's')
save(fig, '66-109')
