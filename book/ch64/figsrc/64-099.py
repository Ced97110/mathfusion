import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
sizes = [60, 20, 4, 2, 1]
ys = [70, 55, 40, 25, 10]
text(ax, 2, 84, r'rapports premiers $\Rightarrow$ simples', 'resultat', 's', ha='left', weight='bold')
for y, s in zip(ys, sizes):
    box(ax, 5, y - 4, 14, 8, 'sujet', label=str(s))
for k in range(4):
    arrow(ax, (12, ys[k] - 4.3), (12, ys[k + 1] + 4.3), 'resultat', lw=1.3)
    text(ax, 16, (ys[k] + ys[k + 1]) / 2, r'$\div %d$' % (sizes[k] // sizes[k + 1]), 'resultat', 's', ha='left')
# A5 : 60 points exacts (6 lignes x 10 colonnes)
text(ax, 65, 72, r'$A_5$ : 60 éléments', 'autre', 's')
for r in range(6):
    for c in range(10):
        disc(ax, 48 + c * 3.8, 64 - r * 3.8, 1.1, 'autre')
text(ax, 65, 40, 'simple', 'resultat', 'm')
text(ax, 65, 31, "60 n'est pas premier", 'limite', 's')
text(ax, 65, 23, 'la réciproque est fausse', 'limite', 's', weight='bold')
save(fig, '64-099')
