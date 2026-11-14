import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

rows = [('sujet', 'Départ : $l$ minorant\n$l\\wedge a=l$ et $l\\wedge b=l$', 'fixe', 'l = 2\n2 ≤ 12 et 2 ≤ 20'), ('varie', 'Étape clé : L2\n$l\\wedge(a\\wedge b)=(l\\wedge a)\\wedge b$', 'fixe', 'PGCD(2, PGCD(12, 20)) =\nPGCD(PGCD(2, 12), 20)'), ('fixe', 'Puis $l\\wedge a=l$, $l\\wedge b=l$', 'fixe', 'PGCD(2, 12) = 2\nPGCD(2, 20) = 2'), ('resultat', 'Arrivée\n$l\\leq a\\wedge b$', 'fixe', '2 ≤ 4 = PGCD(12, 20)')]
rh, gap = 13, 6.5
n = len(rows)
H = 10 + n * rh + (n - 1) * gap + 2
fig, ax = canvas(H)
text(ax, 26, H - 4, 'Preuve', 'fixe', 's', weight='bold')
text(ax, 70, H - 4, 'Avec les nombres', 'fixe', 's', weight='bold')
for i, (role, left, rrole, right) in enumerate(rows):
    y = H - 10 - i * (rh + gap) - rh
    box(ax, 2, y, 48, rh, role, label=left, size='s')
    box(ax, 54, y, 32, rh, rrole, label=right, size='s')
    if i < n - 1:
        arrow(ax, (26, y - 0.3), (26, y - gap + 0.3), 'fixe')
save(fig, '79-106')
