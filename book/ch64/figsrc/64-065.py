import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 2, 62, 84, 9, 'fixe', label=r'$gK$, $hK$ : classes de $g$, $h$', size='s')
rows = [('départ', r'$(gK)(hK)=(hK)(gK)$', 'sujet', 44, 11),
        ('étape clé', r'$gh$ et $hg$ : même classe' + '\n' + r'à $(g,h)$ près', 'varie', 24, 14),
        ('arrivée', r'$(g,h)\in K$, donc $K\supset G^{\prime}$', 'resultat', 6, 11)]
for tag, lab, role, y, h in rows:
    text(ax, 2, y + h / 2, tag, 'fixe', 's', ha='left')
    box(ax, 20, y, 66, h, role, label=lab, size='s')
arrow(ax, (53, 62), (53, 55.5), 'fixe')
for i in range(2):
    arrow(ax, (53, rows[i][3]), (53, rows[i + 1][3] + rows[i + 1][4]), 'fixe')
save(fig, '64-065')
