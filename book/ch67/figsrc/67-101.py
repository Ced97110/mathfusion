import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
rows = [('départ', r'à contredire : $\eta^k=$ id, $k<n$', 'fixe'),
        ('étape décisive', r'tous les $q^n$ éléments racines', 'varie'),
        ('arrivée', r'contradiction : $q^n>q^k$', 'limite')]
ys = [90, 72, 54]
for (t, s, r), y in zip(rows, ys):
    text(ax, 3, y, t, r, 's', ha='left')
    box(ax, 28, y - 6, 58, 12, r, label=s, size='s', lw=1.6 if r == 'varie' else 0.8)
for y in ys[:2]: arrow(ax, (57, y - 7), (57, y - 11), 'fixe')
text(ax, 44, 40, r'cas $q=2$, $n=3$, $k=1$ : $x^2=x$', 'sujet', 's')
for i in range(8): disc(ax, 8 + i * 10.3, 28, 3.6, 'resultat' if i < 2 else 'limite')
brace(ax, 4, 22.6, 22, 'resultat', label='au plus 2 racines', down=True)
brace(ax, 25, 84, 22, 'limite', label='6 de trop : impossible', down=True)
text(ax, 44, 7, '8 éléments de $E$', 'encre', 's')
save(fig, '67-101')
