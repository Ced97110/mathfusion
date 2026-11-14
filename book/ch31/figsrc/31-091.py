import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, r'$\cos^2 x = 1 - \sin x$', 'sujet', 'l')
f = numberline(ax, 8, 76, 26, 0, 360, step=45, arrow_right=False, every=1)
for a in (0, 90, 180, 360):
    disc(ax, f(a), 26, 1.8, 'resultat')
for a in (45, 270):
    disc(ax, f(a), 26, 1.8, 'limite')
disc(ax, 20, 40, 1.8, 'resultat'); text(ax, 24, 40, 'égalité vraie', 'resultat', 'm', ha='left')
box(ax, f(45) - 12, 40, 24, 0.1, 'fixe', fill=False) if False else None
text(ax, f(45) + 2, 14, '0,5 ≠ 0,2929', 'limite', 's', ha='center')
text(ax, f(270), 14, '0 ≠ 2', 'limite', 's')
disc(ax, 54, 40, 1.8, 'limite'); text(ax, 58, 40, 'égalité fausse', 'limite', 'm', ha='left')
text(ax, 44, 4, 'angle en degrés', 'fixe', 's')
save(fig, '31-091')
