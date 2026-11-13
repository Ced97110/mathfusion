import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u, ox, oy = 9.0, 8.0, 17.0
P = lambda a, b: (ox + a * u, oy + b * u)
for a in range(6):
    for b in range(3):
        r = 'sujet' if a % 2 == 0 else 'varie'
        disc(ax, *P(a, b), 1.4, r)
    text(ax, P(a, 0)[0], oy - 5, str(a), 'fixe', 's')
text(ax, 53, 5, 'première coordonnée', 'fixe', 's', ha='right')
text(ax, 20, 52, 'paire : classe 0', 'sujet', 's')
text(ax, 62, 52, 'impaire : classe 1', 'varie', 's')
text(ax, 44, 43, r'$\Delta_1=1,\ \Delta_2=2$', 'encre', 's')
text(ax, 76, 24, r'$M\cong\mathbb{Z}/2$', 'resultat', 'm', weight='bold')
text(ax, 76, 17, '2 classes', 'resultat', 's')
save(fig, '59-133')
