import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

rows = [('sujet', 'Départ : $u$ majorant\n$a\\vee u=u$ et $b\\vee u=u$', 'fixe', 'u = 60\n4 ≤ 60 et 6 ≤ 60'), ('varie', 'Étape clé : L2 seule\n$(a\\vee b)\\vee u=a\\vee(b\\vee u)$', 'fixe', 'PPCM(12, 60) =\nPPCM(4, PPCM(6, 60))'), ('fixe', 'Puis $b\\vee u=u$, $a\\vee u=u$', 'fixe', 'PPCM(6, 60) = 60\nPPCM(4, 60) = 60'), ('resultat', 'Arrivée\n$a\\vee b\\leq u$', 'resultat', '12 ≤ 60')]
rh, gap = 15, 8
n = len(rows)
H = 10 + n * rh + (n - 1) * gap + 2
fig, ax = canvas(H)
text(ax, 26, H - 4, 'Preuve', 'fixe', 's', weight='bold')
text(ax, 70, H - 4, 'Avec les nombres', 'fixe', 's', weight='bold')
for i, (role, left, rrole, right) in enumerate(rows):
    y = H - 10 - i * (rh + gap) - rh
    last = i == n - 1
    box(ax, 2, y, 48, rh, role, label=left, size='s', weight='bold' if role == 'varie' else 'normal')
    box(ax, 54, y, 32, rh, rrole, label=right, size='l' if last else 's', weight='bold' if last else 'normal')
    if i < n - 1:
        arrow(ax, (26, y - 0.3), (26, y - gap + 0.3), 'fixe')
save(fig, '79-102')
