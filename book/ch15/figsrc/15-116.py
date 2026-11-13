import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [(62, r'$(3x^2+x-12)-(8x^2-5x+2)$', '1. écrire la différence', 'sujet'),
        (42, r'$3x^2+x-12-8x^2+5x-2$', '2. changer les signes', 'varie'),
        (22, r'$-5x^2+6x-14$', '3. regrouper', 'resultat')]
for y, s, lab, r in rows:
    box(ax, 6, y - 5, 76, 10, r, label=s, size='m')
    text(ax, 44, y + 7, lab, 'encre', 's')
arrow(ax, (44, 52.2), (44, 49.5), 'varie'); arrow(ax, (44, 32.2), (44, 29.5), 'varie')
text(ax, 44, 9, 'plus de parenthèses, plus de semblables', 'resultat', 's')
text(ax, 44, 4, r'pour $x=1$ : $-8-5=-13$', 'resultat', 's')
save(fig, '15-116')
