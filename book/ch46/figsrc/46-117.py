import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
X = lambda v: 44 + v * 4.6
R = list(range(-8, 9))
text(ax, 44, 74, r'chaque $s$ ≥ 0 : un ensemble différent', 'encre', 'm')
def row(y, s, lab):
    line(ax, [(X(-8), y), (X(8), y)], 'fixe', lw=0.5)
    for v in R:
        if s == 0:
            if v == 0: disc(ax, X(v), y, 1.6, 'sujet')
            else: disc(ax, X(v), y, 0.5, 'fixe')
        elif v % s == 0:
            disc(ax, X(v), y, 1.6, 'varie' if v == s else 'sujet')
        else: disc(ax, X(v), y, 0.5, 'fixe')
    text(ax, 2, y + 5, lab, 'sujet', 'm', ha='left')
row(60, 0, '0ℤ')
row(46, 2, '2ℤ')
row(32, 3, '3ℤ')
row(18, 4, '4ℤ')
disc(ax, 8, 6, 1.6, 'varie')
text(ax, 12, 6, r'plus petit entier positif : $s$', 'varie', 's', ha='left')
save(fig, '46-117')
