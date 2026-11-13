import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = lambda v: 46 + v * 8.5
yA, yB = 44, 22
text(ax, 44, 60, r'$u$ unité $\Leftrightarrow$ ($u$) = ℤ', 'encre', 'm')
text(ax, 2, yA, '(−1)', 'resultat', 's', ha='left')
text(ax, 2, yB, '(2)', 'sujet', 's', ha='left')
for v in range(-4, 5):
    disc(ax, f(v), yA, 1.2, 'resultat')
    if v % 2 == 0:
        disc(ax, f(v), yB, 1.2, 'sujet')
    elif v == 1:
        disc(ax, f(v), yB, 1.2, 'limite', fill=False)
    else:
        disc(ax, f(v), yB, 1.2, 'fixe', fill=False)
text(ax, f(1), yA + 4.5, '1', 'resultat', 's')
text(ax, f(1), yB + 4.5, '1', 'limite', 's')
text(ax, 46, 34, '(−1) contient tous les entiers', 'resultat', 's')
text(ax, 46, 12, "(2) : 1 n'y est pas", 'limite', 's')
save(fig, '56-093')
