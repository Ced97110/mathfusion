import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r"$\nu:\ a\mapsto aK$", 'varie', 'm')
labs = ["0, 4, 8, …", "1, 5, 9, …", "2, 6, 10, …", "3, 7, 11, …"]
for i in range(4):
    x = 3 + 21.5 * i
    disc(ax, x + 9.5, 46, 4, 'fixe', label=str(i), size='s')
    arrow(ax, (x + 9.5, 41.6), (x + 9.5, 29), 'varie')
    box(ax, x, 18, 19, 10, 'sujet', label=labs[i], size='s')
text(ax, 44, 8, "aucun paquet n'est oublié", 'resultat', 's')
save(fig, '48-079')
