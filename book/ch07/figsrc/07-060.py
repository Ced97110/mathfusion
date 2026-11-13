import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def case(y, b, d, last, com):
    s, o = 3.0, 12.0
    X = lambda v: o + v * s
    line(ax, [(o, y), (X(last), y)], 'fixe', lw=0.9)
    for v in range(b, last + 1, b): disc(ax, X(v), y + 4, 1.1, 'sujet')
    for v in range(d, last + 1, d): disc(ax, X(v), y - 4, 1.1, 'autre')
    text(ax, 6, y + 4, str(b), 'sujet', 'm'); text(ax, 6, y - 4, str(d), 'autre', 'm')
    return X
X = case(66, 3, 5, 15, 15)
line(ax, [(X(15), 58), (X(15), 74)], 'resultat', lw=1.3, dash=True)
text(ax, X(15) + 2, 78, 'PPCM = 15 = 3 × 5', 'resultat', 's', ha='left')
text(ax, 44, 86, 'multiples de b (haut) et de d (bas)', 'fixe', 's')
X = case(30, 4, 6, 24, 12)
line(ax, [(X(12), 22), (X(12), 38)], 'resultat', lw=1.3, dash=True)
line(ax, [(X(24), 22), (X(24), 38)], 'varie', lw=1.3, dash=True)
text(ax, X(12), 42, 'PPCM = 12', 'resultat', 's')
text(ax, X(24), 16, '4 × 6 = 24', 'varie', 's', ha='right')
save(fig, '07-060')
