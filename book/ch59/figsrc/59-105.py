import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
sc, x0 = 3.4, 14.0
X = lambda v: x0 + v * sc
def row(y, step, upto, role, name):
    text(ax, 6, y, name, role, 's')
    line(ax, [(X(0) - 1, y), (X(upto) + 1, y)], 'fixe', lw=0.5)
    return [v for v in range(0, upto + 1, step)]
# panneau 1 : 2 divise 10
text(ax, 44, 86, '2 divise 10', 'resultat', 'm', weight='bold')
for v in row(74, 2, 20, 'sujet', '(2)'):
    disc(ax, X(v), 74, 1.2, 'sujet')
for v in row(62, 10, 20, 'autre', '(10)'):
    disc(ax, X(v), 62, 1.2, 'autre')
for v in (10, 20):
    line(ax, [(X(v), 63.5), (X(v), 72.5)], 'resultat', lw=0.7, dash=True)
text(ax, 44, 54, '(2) ⊇ (10)', 'resultat', 's')
# panneau 2 : 3 ne divise pas 4
text(ax, 44, 42, '3 ne divise pas 4', 'limite', 'm', weight='bold')
for v in row(30, 3, 12, 'sujet', '(3)'):
    disc(ax, X(v), 30, 1.2, 'sujet')
for v in row(18, 4, 12, 'autre', '(4)'):
    disc(ax, X(v), 18, 1.2, 'limite' if v in (4, 8) else 'autre')
for v in (4, 8):
    line(ax, [(X(v), 19.5), (X(v), 28.5)], 'limite', lw=0.7, dash=True)
text(ax, 62, 24, '4 et 8 : hors de (3)', 'limite', 's')
text(ax, 44, 8, '(4) n’est pas dans (3)', 'limite', 's')
save(fig, '59-105')
