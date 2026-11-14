import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
gx = lambda a: 18 + 16 * a
gy = lambda b: 8 + 8.5 * b
text(ax, 26, 62, '(ℤ/2, ℤ/6)', 'fixe', 'm')
for a in range(2):
    for b in range(6):
        r, rad = 'fixe', 1.6
        if (a, b) in ((1, 0), (0, 1)): r, rad = 'sujet', 2.6
        if (a, b) == (1, 3): r, rad = 'autre', 2.6
        disc(ax, gx(a), gy(b), rad, r)
text(ax, gx(0) - 5, gy(1), '(0, 1)', 'sujet', 's', ha='right')
text(ax, gx(1) + 5, gy(0), '(1, 0)', 'sujet', 's', ha='left')
text(ax, gx(1) + 5, gy(3), '(1, 3)', 'autre', 's', ha='left')
text(ax, 47, 52, 'A : (1, 0) et (0, 1)', 'sujet', 's', ha='left')
text(ax, 47, 45, 'annulateurs : 2 et 6', 'sujet', 's', ha='left')
text(ax, 47, 32, 'B : (1, 3) et (0, 1)', 'autre', 's', ha='left')
text(ax, 47, 25, 'annulateurs : 2 et 6', 'autre', 's', ha='left')
text(ax, 47, 12, 's = t = 2 morceaux', 'resultat', 's', ha='left')
save(fig, '60-056')
