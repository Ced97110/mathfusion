import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

rows = [('sujet', 'Départ\n$a\\vee b=b$ et $b\\vee c=c$', 'fixe', 'PPCM(4, 12) = 12\nPPCM(12, 60) = 60'), ('varie', 'Étape clé : L2\n$a\\vee(b\\vee c)=(a\\vee b)\\vee c$', 'fixe', 'PPCM(4, PPCM(12, 60))\n= PPCM(PPCM(4, 12), 60)'), ('resultat', 'Arrivée\n$a\\vee c=c$', 'fixe', 'PPCM(4, 60) = 60')]
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
save(fig, '79-099')
