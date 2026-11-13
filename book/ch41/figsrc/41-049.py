import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'trois carrés, une somme, une racine', 'encre', 'm')
k = 1.3
rows = [((1, 2, 2), '1 + 4 + 4 = 9', 3), ((2, 3, 6), '4 + 9 + 36 = 49', 7), ((3, 4, 0), '9 + 16 + 0 = 25', 5)]
for r, (v, s, n) in enumerate(rows):
    assert sum(c * c for c in v) == int(s.split('=')[1]) and n * n == int(s.split('=')[1])
    y = 50 - r * 18
    text(ax, 2, y, r'$\langle %d,\ %d,\ %d\rangle$' % v, 'sujet', 'm', ha='left')
    for i, c in enumerate(v):
        cx = 21 + i * 10.5
        if c == 0:
            disc(ax, cx + 3, y, 0.5, 'fixe')
        else:
            box(ax, cx, y - c * k / 2, c * k, c * k, 'sujet' if i < 2 else 'varie', r=0.01, lw=0.6)
    text(ax, 50, y, s, 'encre', 's', ha='left')
    text(ax, 86, y, 'norme %d' % n, 'resultat', 's', ha='right', weight='bold')
text(ax, 24, 8, 'chaque carré a pour côté a, b ou c', 'fixe', 's', ha='left')
save(fig, '41-049')
