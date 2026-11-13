import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'$\mathbb{Z}$ : aucune règle entre les pas', 'sujet', 'm')
xs = [9 + 10 * i for i in range(8)]
line(ax, [(2, 52), (86, 52)], 'fixe')
cx = [22 + 15 * j for j in range(4)]
for i, x in enumerate(xs):
    disc(ax, x, 52, 3.6, 'sujet' if i < 4 else 'varie', label=str(i), size='s')
    arrow(ax, (x, 48.2), (cx[i % 4], 22.5), 'fixe' if i < 4 else 'varie', lw=0.7)
for j, x in enumerate(cx):
    disc(ax, x, 18, 4.2, 'resultat', label=str(j))
text(ax, 44, 36, 'règle : 4 pas = 0', 'varie', 'm', weight='bold')
text(ax, 44, 7, r'$\mathbb{Z}/4\mathbb{Z}$ : horloge à 4 positions', 'resultat', 'm')
save(fig, '48-194')
