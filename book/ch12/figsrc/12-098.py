import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u, x0, y, h = 8, 8, 28, 8
x = x0
for n, r in [(2, 'sujet'), (6, 'autre'), (1, 'fixe')]:
    box(ax, x, y, n * u, h, r, label=str(n), r=0.5); x += n * u
brace(ax, x0, x0 + 8 * u, y + h + 0.5, 'varie', '(2 + 6) + 1 = 9', down=False)
brace(ax, x0 + 2 * u, x0 + 9 * u, y - 0.5, 'varie', '2 + (6 + 1) = 9', down=True)
arrow(ax, (x0, 14), (x0 + 9 * u, 14), 'resultat', both=True)
text(ax, 44, 8.5, 'même trajet : de 0 à 9', 'resultat', 's')
save(fig, '12-098')
