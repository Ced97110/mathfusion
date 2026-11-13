import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

rows = [('sujet', 'Départ\n$a\\vee b$ et les lois L1 à L4', 'fixe', 'PPCM(4, 6) = 12'), ('fixe', 'Temps 1 : $a\\vee b$ est un majorant', 'fixe', '4 ≤ 12 et 6 ≤ 12'), ('varie', 'Temps 2 : le plus petit\n$a\\vee b\\leq u$ pour tout majorant $u$', 'fixe', 'autre majorant : 60\n12 ≤ 60'), ('resultat', 'Arrivée\n$a\\vee b$ est le sup', 'fixe', '12 est le sup\nde 4 et 6')]
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
save(fig, '79-100')
