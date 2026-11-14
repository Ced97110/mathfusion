import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'ordre du groupe de $g$  →  $G_f$', 'encre', 'm')
rows = [(6, r'$G_f = S_4$', 'resultat'), (3, r'$G_f = A_4$', 'resultat'), (1, r'$G_f = V$', 'resultat'), (2, r'$G_f = D$ ou $C$', 'varie')]
for j, (n, lab, role) in enumerate(rows):
    y = 48 - j * 15
    text(ax, 12, y + 4.5, f'ordre {n}', 'autre', 's')
    for i in range(n):
        disc(ax, 26 + i * 5.2, y + 4.5, 1.7, 'autre')
    arrow(ax, (55, y + 4.5), (60, y + 4.5), 'fixe')
    box(ax, 62, y, 24, 9, role, label=lab, size='s')
save(fig, '65-093')
