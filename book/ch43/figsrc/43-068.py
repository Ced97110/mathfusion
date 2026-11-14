import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def dots(x, y, pts, role):
    for dx, dy in pts: disc(ax, x + dx, y + dy, 1.1, role)
def panel(x, title, trole, formula):
    box(ax, x, 12, 27, 32, 'fixe', fill=False, dash=True)
    text(ax, x + 13.5, 49, title, trole, 'm'); text(ax, x + 13.5, 6, formula, trole, 's')
panel(2, 'partition', 'resultat', 'les deux vraies')
box(ax, 4, 28, 11, 14, 'sujet'); dots(4, 28, [(3, 4), (8, 4), (5.5, 10)], 'sujet')
box(ax, 17, 28, 10, 14, 'autre'); dots(17, 28, [(3, 4), (7, 4), (5, 10)], 'autre')
box(ax, 4, 14, 23, 11, 'varie'); dots(4, 14, [(5, 5.5), (11.5, 5.5), (18, 5.5)], 'varie')
panel(31, 'chevauchement', 'limite', r'$X_i\cap X_j\neq\emptyset$')
box(ax, 33, 26, 16, 16, 'sujet', fill=False); box(ax, 40, 22, 16, 16, 'autre', fill=False)
dots(33, 26, [(3, 3), (3, 11)], 'sujet'); dots(40, 22, [(12, 11), (12, 3)], 'autre')
disc(ax, 44.5, 31, 1.3, 'limite'); box(ax, 36, 16, 18, 4, 'fixe', fill=False) if False else None
panel(60, 'oubli', 'limite', r'$\bigcup X_k\neq X$')
box(ax, 62, 28, 11, 14, 'sujet'); dots(62, 28, [(3, 4), (8, 4), (5.5, 10)], 'sujet')
box(ax, 75, 28, 10, 14, 'autre'); dots(75, 28, [(3, 4), (7, 4), (5, 10)], 'autre')
for p in [(66, 19), (72, 17), (79, 20)]: disc(ax, p[0], p[1], 1.2, 'limite', fill=False)
save(fig, '43-068')
