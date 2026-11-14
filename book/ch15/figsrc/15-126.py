import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
rows = [(44, r'$x=5$', r'$5^0=1$', r'$8\times1=8$', 'resultat'),
        (26, r'$x=2$', r'$2^0=1$', r'$8\times1=8$', 'resultat'),
        (8, r'$x=0$', r'$0^0$', 'pas de sens', 'limite')]
for y, a, b, c, r in rows:
    box(ax, 3, y, 18, 10, 'varie', label=a, size='m')
    box(ax, 28, y, 24, 10, 'sujet', label=b, size='m')
    box(ax, 59, y, 26, 10, r, label=c, size='m')
    arrow(ax, (21.5, y + 5), (27.5, y + 5), 'fixe'); arrow(ax, (52.5, y + 5), (58.5, y + 5), 'fixe')
text(ax, 44, 57, r'$8x^0$ pour trois valeurs de $x$', 'encre', 's')
save(fig, '15-126')
