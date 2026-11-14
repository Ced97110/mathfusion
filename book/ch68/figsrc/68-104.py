import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'mots non nuls du code', 'encre', 'm')
for y, w, n in [(46, '00111', 3), (32, '11100', 3), (18, '11011', 4)]:
    low = n == 3
    box(ax, 2, y - 6, 84, 12, 'resultat' if low else 'fixe', fill=False, dash=not low)
    text(ax, 16, y, w, 'sujet', 'm')
    for k in range(n):
        disc(ax, 34 + 7 * k, y, 2.4, 'sujet')
    text(ax, 76, y, f'poids {n}', 'resultat' if low else 'fixe', 'm')
text(ax, 44, 6, r'$d = 3$ : le plus petit poids', 'resultat', 'm')
save(fig, '68-104')
