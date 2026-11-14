import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(58)
f = numberline(ax, 6, 78, 24, 0, 90, step=15, every=2, arrow_right=False, size='s')
for v, role, lab in [(15, 'autre', 'Q = 15°'), (45, 'resultat', 'A = 45°'), (75, 'sujet', 'P = 75°')]:
    disc(ax, f(v), 24, 1.9, role)
    text(ax, f(v), 29.5, lab, role, 's')
for v in (15, 45, 75): line(ax, [(f(v), 32.5), (f(v), 37)], 'fixe', 0.6, True)
arrow(ax, (f(45), 36), (f(75), 36), 'varie', lw=1.1)
arrow(ax, (f(45), 36), (f(15), 36), 'varie', lw=1.1)
text(ax, (f(45) + f(75)) / 2, 40, 'B = 30°', 'varie', 's')
text(ax, (f(45) + f(15)) / 2, 40, 'B = 30°', 'varie', 's')
text(ax, 44, 11, 'A = (P + Q) / 2 : milieu de P et Q', 'resultat', 's') if False else None
text(ax, 4, 17, 'on pose P = A + B et Q = A − B', 'encre', 's', ha='left')
text(ax, 4, 11, 'A = (P + Q) / 2 = 45°', 'resultat', 's', ha='left')
text(ax, 4, 5, 'B = (P − Q) / 2 = 30°', 'varie', 's', ha='left')
save(fig, '35-058')
