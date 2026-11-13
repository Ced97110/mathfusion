import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
xs = [2, 31.5, 61]; wd = 25; y = 28; h = 22
data = [('sujet', 'Départ', r'$a$ dans $U(n)$', r'9 dans $U(10)$'),
        ('varie', 'Étape clé', r'Lagrange sur $\langle a\rangle$', r'ordre 2 divise 4'),
        ('resultat', 'Arrivée', r'$a^{\varphi(n)}\equiv 1$', r'$9^4=(9^2)^2=1$')]
for x, (r, t1, t2, t3) in zip(xs, data):
    box(ax, x, y, wd, h, r, lw=2.0 if r == 'varie' else 0.8)
    text(ax, x + wd/2, y + 15, t1, r, 'm', weight='bold')
    text(ax, x + wd/2, y + 8, t2, r, 's')
    text(ax, x + wd/2, y - 5, t3, r, 's')
for i in range(2):
    arrow(ax, (xs[i] + wd + 0.3, y + h/2), (xs[i+1] - 0.3, y + h/2), 'encre')
text(ax, 44, 13, 'l’étape du milieu porte la preuve', 'varie', 's')
save(fig, '47-193')
