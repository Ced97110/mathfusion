import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 22, 31, 15
P = lambda k, rad=R: (cx + rad * math.sin(math.radians(30 * k)), cy + rad * math.cos(math.radians(30 * k)))
for k in range(12):
    role = 'sujet' if k == 9 else ('resultat' if k == 2 else 'fixe')
    disc(ax, P(k)[0], P(k)[1], 1.7, role)
for k in (0, 3, 6, 9, 2):
    x, y = P(k, R + 5)
    text(ax, x, y, str(k), 'resultat' if k == 2 else ('sujet' if k == 9 else 'encre'), 's')
for k in (9, 10, 11, 0, 1):
    a, b = P(k), P((k + 1) % 12)
    d = math.hypot(b[0] - a[0], b[1] - a[1]); u = ((b[0] - a[0]) / d, (b[1] - a[1]) / d)
    arrow(ax, (a[0] + u[0] * 2.2, a[1] + u[1] * 2.2), (b[0] - u[0] * 2.2, b[1] - u[1] * 2.2), 'varie', lw=1.1)
text(ax, 46, 52, r'$\mathbb{Z}/n$ : $n$ heures', 'sujet', 'm', ha='left', weight='bold')
text(ax, 46, 42, r'$9+5=14\ \to\ 2$', 'varie', 'm', ha='left')
text(ax, 46, 35, r'$5+9=14\ \to\ 2$ aussi', 'varie', 'm', ha='left')
text(ax, 46, 24, 'ajouter 1 : on passe partout', 'encre', 's', ha='left')
text(ax, 46, 17, 'abélien : l’ordre est libre', 'encre', 's', ha='left')
save(fig, '64-050')
