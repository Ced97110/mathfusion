import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 44, 50, 'Restes par 6 : un entier agit en multipliant', 'encre', 's')
w, g, x0, y = 11, 2.2, 5.4, 16
cx = {}
for r in range(6):
    x = x0 + r * (w + g); cx[r] = x + w / 2
    box(ax, x, y, w, 11, 'sujet' if r % 2 == 0 else 'fixe', label=str(r), size='l')
arrow(ax, (cx[5], y + 12), (cx[2], y + 12), 'varie', curve=0.45)
text(ax, (cx[5] + cx[2]) / 2, y + 25, r'$\times 4$ : 5 donne 20, reste 2', 'varie', 's')
text(ax, 44, 9, "0, 2, 4 (bleu) : l'action les laisse dedans", 'sujet', 's')
text(ax, 44, 3.5, 'les restes 1, 3, 5 sont en gris', 'fixe', 's')
save(fig, '52-288')
