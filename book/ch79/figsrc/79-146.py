import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cols = [(2, 'essai 1', '8, 12, 18', 'gauche : 36, puis 4', 'droite : 4 et 2', '4 = 4'),
        (46, 'essai 2', '6, 10, 15', 'gauche : 30, puis 6', 'droite : 2 et 3', '6 = 6')]
for x, t, abc, g, d, r in cols:
    text(ax, x + 20, 74, t, 'fixe', 's')
    box(ax, x, 58, 40, 10, 'varie', label=abc)
    box(ax, x, 42, 40, 10, 'varie', label=g, size='s')
    box(ax, x, 26, 40, 10, 'varie', label=d, size='s')
    box(ax, x, 10, 40, 10, 'resultat', label=r, weight='bold')
    arrow(ax, (x + 20, 58), (x + 20, 52), 'fixe'); arrow(ax, (x + 20, 42), (x + 20, 36), 'fixe'); arrow(ax, (x + 20, 26), (x + 20, 20), 'fixe')
text(ax, 44, 3, "même égalité, deux valeurs", 'fixe', 's')
save(fig, '79-146')
